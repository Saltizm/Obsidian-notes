### Web application assessment methodology
- [[White-box testing]]
- [[Black-box testing]]
- [[Grey-box testing]]
- this session will cover black box
#### Finger printing
- nmap
	- http-enum script scans through directories and list interesting ones
	- `sudo nmap -p80 --script=http-enum 192.168.50.20`
- Wappalyzer 
	- check website tech stack
- Gobuster - bruteforce http-enum
	- `gobuster dir -u ipaddr -w /usr/shared/wordlist/common.txt -t 10`
- Burp suite
	- Proxy tool
		- used to modify packets to and fro
		- intercept all requests 
		- manual forwarding
		- Setting up browser:
			- navigate to "about:preference#general" or go thr setting and search for preference
			- scroll to bottom anc check connection settings
	- Intruder 
		- fuzzing tool
		- get packet from "proxy" and send to intruder
		- select portion to fuzz
		- enter wordlist and run
- Fuff
	- fuzzing post and get request
	- post
		- `ffuf -w /path/to/xss-payloads.txt -X POST -d "username=admin&comment=FUZZ" -u http://example.com -H "Content-Type: application/x-www-form-urlencoded"`
	- get 
		- `fuff -w /path/to/payloads.txt:FUZZ -u "http://example.com/login?name=FUZZ?password=password123`
- Http codes
	- 20X success
		- 200 OK
		- 201 Created 
		- 202 Accepted
		- 204 No content
	- 30X info -usually not visible 
	- 40X our fault
		- 400 bad request
		- 401 unauthorised 
		- 403 forbidden
		- 404 Not found
		- 409 conflict -desynced with server
			- usually unset automatic datetime
	- 50X their fault
		- 500 internal server error
		- 501 not implemented 
		- 502 bad gateway
		- 503 service unavailable 
		- 504 gateway timeout
		- 509 timeout
#### Webapp enum
- to discover technology stack to craft exploits for it
**file extensions**
- path in url might end in a file extension
- unlikely in modern websites due to [[url_routing|Routes]] 
**inspection**
- debugging - open webapp files
	- click on curly braces on bottom left to pretty print the minimised script
- inspect - drill down to selected html element
**robot.txt**
- list of disallowed directories and allowed directories for web spiders
- disallowed directories might be points of entry
- most case, can inform on webapp structure
#### Rest api
Representational State transfer (REST) api
used for authentication and session
directory names are very descriptive 
##### worked example
- generate a pattern file named "pattern"
	- 
```
{GOBUSTER}/v1
{GOBUSTER}/v2
```
- run script 
	- gobuster dir -u http://example.com -w path/to/wordlist -p pattern
- /user/v1 is available API
- receive /user API for api accounts
- run script
	- gobuster dir -u http://example.com/user/v1/admin/ -w path/to/wordlist
- 405 code flashed for /email and /password
- 405 METHOD NOT ALLOWED, meaning there is something but we are not allowed to enter
- password api may be interactible through PUT/POST
- attempt to find a login page 
	- curl -i http://example/user/v1/login
	- ![[Pasted image 20261011051537.png]]
	- api working. No user named "login". but also no login page
- 
