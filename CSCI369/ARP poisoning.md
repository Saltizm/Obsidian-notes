---
index: true
course: "CSCI369"
chapter: "Ethical hacking foundations"
concept: "ARP poisoning"
---

# ARP poisoning

### .
- Also know as ARP spoofing
- [[MITM]] attack that involves impersonating the router and victim
- Better than [[ICMP]] for network mapping 
	- Cannot be filtered by firewall (Uses datalink layer)
- Dangers: **
	- Full control too packets 
	- preparation for more serious attack
### Setup
- This is a [[White-box testing|White-box attack]]
- uses [[Kali linux]]
#### Command
- arp -a : display host IP and MAC
- netdiscover -i \[interface\] -p/-r \[if -r: {CIDR IP}\]
	- -i : which network interface to use (i.e. eth0, eth1)
	- -p : passive mode, sniffs arp request in current network
	- -r : range/active mode, find hosts by sending arp request
- arpspoof -i \[interface\] -t \[target\] \[default gateway\]
- echo1 > /proc/sys/net/ipv4/ip_forward : IP forward to make packets go through attacker's device
#### Process
- Attacker receives packet addressed to router 
- modify it to contain the attackers MAC addr
- send response from router to host after spoof
![[Pasted image 20250825224546.png]]
### Prevention
- difficult  to prevent as it **exploit the insecure way that ARP work** 
- Static ARP tables (unscalable)
- regular auditing
	- Checking default gateway mac address
	- checking for duplicate IP address ([[Wireshark]])