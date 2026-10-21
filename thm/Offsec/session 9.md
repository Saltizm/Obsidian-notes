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
#### File inclusion
