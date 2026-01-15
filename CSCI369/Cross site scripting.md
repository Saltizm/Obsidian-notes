### .
- XSS is a injection exploit
- Malicious code is injected into webpages 
### Types
#### Reflected XSS
- Exploit [[social engineering]]
- Exploit server-side vulnerability to **execute** malicious code
#### DOM XSS
- DOM (document object model) 
- Exploit client-side vulnerability (javascript) to inject malicious code into local webpage
#### Stored XSS
- Exploit server-side vulnerability to **inject** malicious code into files 
- Infects the html file for webpage with malicious code 

| Type      | Use case                                                                                    | Persistence                                                                  |
| --------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Reflected | Single use, low impact                                                                      | Non-persistent, Single execution                                             |
| DOM       | To infect commonly used machines offering web services. (library computer etc). High impact | Persistent, until webpage is closed or refreshed                             |
| Stored    | To infect **WEB SERVER** html files. Very high impact                                       | Very persistent, whoever visits the website from any client will be affected |
### Prevention
- Escape any untrusted input 
- Minimise manipulation of user input on html ()
