---
index: true
course: "thm"
chapter: "Offensive security"
concept: "Session 6"
---

# Session 6

### Vuln scanner
- Host discovery - determine host that are reachable and responsive/unresponsive
- [[CVE(Malware and exploits)]] - exploits
types:
- Manual - active threat discovery
- Auto
	- establishing baseline
	- scalar assessment
	- quickscan
	- low-hanging fruit
where:
- External - DMZ -> public facing services
	- to find possible entry points (attack surface)
- Internal - private services 
	- to audit security posture
	- requires a vpn to perform
with:
- unauthenticated (black box)
- authenticated (white box)
Scan factors:
- duration
- visibility - is target accessible
	- consider boundaries defined in ROE
- rate limiting 
- filtering - is the target really offline or are they blocking request 
	- ips
- 


### CVSS
common vulnerability scoring system is a **framework** for scoring vulnerability severity. A form of **Qualitative severity rating**
