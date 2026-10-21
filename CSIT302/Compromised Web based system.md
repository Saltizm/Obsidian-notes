---
index: true
course: "CSIT302"
chapter: "Application security"
concept: "Compromised Web based system"
---

# Compromised Web based system

- [[Cloud computing|Web based systems]] are easier to compromise because it is public and accessible  
### Types
#### LFI (local file inclusion)
- Reading **Local files** that are on the same server
- files **OUTSIDE** of the directory is exposed
	- i.e. ) /etc/password 
- Causes sensitive data exposure
##### Prevention
- static file inclusion ** : validate incoming files 
```php
<?php> 
$file = $_GET['page']; 
if ($file != "include.php"){
	echo "ERROR: File NOT FOUND!"; exit; 
	} 
?>
```
#### RFI (remote file inclusion)
- Reading files **Sent to** the server through [[Cross site scripting]] or [[social engineering]]
- a remote [[bind shell]] can be created 
- causes [[RCE]]
##### Prevention
- Disable ```allow_url_fopen``` and ```allow_url_include```
#### Methods
##### XSS
![[Cross site scripting#.]]
#### Cookie theft
![[Cookie theft#^427c11]]
#### IDOR
![[IDOR#^bbac9a]]
#### DDOS
![[DDOS#^9eade7]]