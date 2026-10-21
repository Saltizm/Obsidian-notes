---
index: true
course: "thm"
chapter: "TryHackMe practice"
concept: "metasploit"
---

# metasploit

## Task  1
Introduction to the types of metasploit services.

- Metasploit pro - With gui, has automation
- Metasploit framework - in CLI
	- MsfConsole 
	- Modules 
		- Scanners 
		- Payload creation 
	- Tools
## Task 2
![[Pasted image 20260109025427.png]]
## Auxiliary
![[Pasted image 20260109025548.png]]
## encoding 
To encode payload using defined encoder
![[Pasted image 20260109025722.png]]
## evasion
Used to evade system/antivirus detection 
![[Pasted image 20260109025855.png]]
## exploit
arranged by system
![[Pasted image 20260109030013.png]]
## NOPs (no operations)
do nothings. Used as buffer for payload to ensure consistent size. Arranged by cpu architecture
![[Pasted image 20260109030127.png]]
## Payloads

- Singles - Self contained payload. No need for external components to run (executables etc)
	- generic/shell==\_==reverse_tcp
- Stagers and Stages - Stagers establish connection and downloads Stages which is the rest of the payload.
	- Windows/x64/shell==/==reverse_tcp
- Adapter - wrapper for Singles. (eg powershell adaptors execute a powershell command that runs the payload)

### purpose
- Singles - small payloads
- Stagers and Stage - large payloads
- Adapters 

## Post
post exploitation. Usually for data expulsion or privilege escalation 
![[Pasted image 20260109031125.png]]
## Task 3
context - the current module used in the shell. Is shown as a directory
(eg. windows/smb/ms17_010_eternalblue)

