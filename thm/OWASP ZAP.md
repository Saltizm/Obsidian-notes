---
index: true
course: "thm"
chapter: "TryHackMe practice"
concept: "OWASP ZAP"
---

# OWASP ZAP

## Web crawling
- Spiders (web crawlers) usually brute force through 2 methods 
	- Link trailing : follow links through embeds (traditional)
	- url enum : go through possible urls to seek subdirectories 
## Active scans
## Quick scan 
utilise link trailing spiders to scan through a web directory 
process
-  click quick scan
-  results in "output" tab

## Manual scan
manually create a proxy between machine and web browser (application layer) to receive requests sent to and fro browser
process
- Copy and export root CA certificate  under tools > options > network > server certificate 
- Check proxy settings. Ensure:
	- TLS  version  
	- HTTP version 
- are both accepted by the browser
## Passive scans (scripts)
scripts that run with a proxy to automatically detect vulnerabilities 
- manage add-ons (3 cubes)
- install scripts ( hunt.py )
- besides "sites" add tab "scripts"
- go to appropriate section ( Hunt is a passive rule)
- enable script
## Fuzzing
Bruteforce using a wordlist 
- Select POST/GET request 
- click fuzzing and highlight section to be altered 
- add wordlist 
## Learning outcome
ZAP streamlines a lot of processes used in web penetration. Personally it feels like what kali is to pentesting. Although the tools are versatile it would be best to learn the base functions before proceeding to ensure there is no black boxs heading forward. 