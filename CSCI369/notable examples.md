---
index: true
course: "CSCI369"
chapter: "Ethical hacking foundations"
concept: "notable examples"
---

# notable examples

Mirai Botnet
- Botnet on IOT devices
- mirai worm infects cctv cameras by xiaomi
- Many varients hard to enforce countermeasures
Accolades 
- Took down twitter in October 2016 in 6 hours

Medibank dataleak
- Chap1 slide 27 (timeline)
- Ext recon - Received stolen password and username from third party IT contractor 
- Compromising - Exploited weak auth (no MFA)
- Lateral movement/privilege esc - Out of date infrastructure and poorly configured permissions 
- Conclusion - extortion of money through threat of releasing data
Lessons learned
- Proper risk management when hiring third party contractors
- Proper Auth procedures 
- Restrict permissions 

Ethernal blue
- Zero day exploit on the SMB protocol 
- DEVELOPED by the nsa 
- but sold to shadow breakers( hacker group )
- SMB - simple message block ( used for printers and file sharing between device )

Lockbit 3.0
- RAAS 
- wide spread petty ransomware attacks

GameOverZeus
- Zeus (Type of trojan sold as a MAAS)
- this is upgraded to avoid detection by avoiding central servers 
- Dropper utilise PTP protocols
Metasploit framework **
- Tool developed under the project created by 
- H.D. Moor
- Developed using Perl in 2003
- Rewritten in Ruby in 2007
- Acquired by Rapid7 in 2009
- [[Red team]] - use to intrude into remote system
- [[Blue team]] - use to test vulnerabilities 
OpenSSL heartbleed
- allow client to compromise sensitive data by sending a "heartbeat" request:
	- checks server status (up or down)
	- [[Buffer overflow]] exploit by sending a message longer than the defined request size
- "heartbeat" original purpose is to **maintain connection** for [[Document in transit]]
Dirty cow attack
- [[Virtualisation|VMs]] will copy memory if a process writes to memory. (Known as Copy On Write \<COW\>) 
- Increases performance process does not have to constantly read from memory
- ![[Pasted image 20250831013358.png|300]]
- error in code allow for 2 processes working closely to overlap their requests. (Race condition \*\*)
- First process request for COW
- Second process request to write while copy is delivered.
- No need to copy as first *write flag* is still up
Stuxnet
- Worm (APT malware)
- attack logic controller of nuclear centrifuges 
- design to halt nuclear development in iran
- Affected SCADA 
	- control system architecture 
	- High level management: computers, networked data coms, GUIs. 
	- Low level interface: PLC(controlling manufacturing processes )
	