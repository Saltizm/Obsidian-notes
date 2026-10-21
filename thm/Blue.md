---
index: true
course: "thm"
chapter: "TryHackMe practice"
concept: "Blue"
---

# Blue

nmap -sV -vv --script vuln TARGET_IP
- sV : version scan
- --script (new) 
	- vuln : check for common vulnerabilities 
	- exploit : exploit common vuln
	- safe : run all that are safe
	- intrusive : run all that IDS will catch/ affect target
	- brute : bruteforce attack


## Notes
Attack process
- nmap scan
- metasploit payload and exploit