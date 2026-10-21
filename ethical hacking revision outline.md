---
index: true
course: "Independent study"
chapter: "Cybersecurity practice"
concept: "ethical hacking revision outline"
---

# ethical hacking revision outline

### Type of hacker
- White hat 
- black hat
- grey hat (activist)
#### Cyber threat
- Bot net 
- Malware
- Hacktivism
#### Cybercrime law
- ![[Cybercrime]]
### Pen testing
- enviroments
	- Black - obscured
	- Grey - some information
	- White - full information
- RMP ([[Risk mitigation plan]])
- permission for pentest - (Rules of engagement)
### Intelligence gathering method
#### active gathering 
- phishing and variation 
- social engineering
- network probing/auxillary scanning 
#### OSINT ( passive gathering )
- DNS (nslookup, **dig**)
- web domain enumeration - email and people
- google dorking
- IOT osint (shodan.io)
### DNS (web)
- subdomain takeover
- RFI/LFI
### Network
- network topology ( traceroute )
- OSI model
	- layer 2 (datalink)
		- ARP ( mac address translation )
		- routers 
	- layer 3 (network)
		- ip
			- CIDR notation xxx.xxx.xxx.xxx/y
				- y is subnet mask bits
		- tools: 
		- icmp
	- layer 4 ( transport )
		- tcp
		- udp (connectionless)
		- ports
- wireshark
- number of usable ip
	- 2^(n-1) 
- [[Nmap]]
- [[ARP]]
### MITM
- SSL strip - downgrade from https to http
- HSTS - protection against ssl strip (does not work on first visit. Only subsequent visits will enforce https)
- ARP poisoning
- **DNS**
	- DNS cache poisoning (dns spoofing)
	- DNS poisoning mitm (modifying ip packets)
	- DNS tunneling (firewall bypass as it does not check dns requests)
	- DNS flood attack (firewall bypass ddos attack)
### Vuln
- types:
	- design 
	- implementation
	- local ( insider attack )
	- remote
- CVE
- OWASP top 10
- searchsploit
- clientside, serverside
- metasploit framework 