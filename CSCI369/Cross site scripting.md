---
index: true
course: "CSCI369"
chapter: "Web security"
concept: "Cross site scripting"
---

# Cross site scripting

### .
- XSS is a injection exploit
- Malicious code is injected into webpages 
### Types
#### Reflected XSS
- Exploit [[social engineering]]
	- payload in url
- Exploit server-side vulnerability to **execute** malicious code
#### DOM XSS
- [[DOM]] (document object model) 
- Exploit client-side vulnerability (javascript) to inject malicious code into local webpage
#### Stored XSS (persistent xss)
- Exploit server-side vulnerability to **inject** malicious code into files 
	- carried out in comments or forum posts ( persistent data )
- Infects the html file for webpage with malicious code 

| Type      | Use case                                                                                    | Persistence                                                                  |
| --------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Reflected | Single use, low impact                                                                      | Non-persistent, Single execution                                             |
| DOM       | To infect commonly used machines offering web services. (library computer etc). High impact | Persistent, until webpage is closed or refreshed                             |
| Stored    | To infect **WEB SERVER** html files. Very high impact                                       | Very persistent, whoever visits the website from any client will be affected |
### Prevention
- Escape any untrusted input 
	- Common special characters
		- <>'"{};
	- reflected xss
		- [[URL encoding]]
		- [[nonce]] (wordpress)
	- DOM
		-[[ html encoding]]
- Minimise manipulation of user input on html ()
### Privilege escalation
- stealing session cookies to auto login
- [[CSRF]]