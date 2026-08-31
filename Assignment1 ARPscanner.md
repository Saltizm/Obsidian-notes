### Outline
Targeted system : metasploitable2 virtual machine
Target IP: 10.0.2.3
Network type: Nat  network

Host system: kali linux
Host IP: 10.0.2.4
Network type: Nat network

Tools used: 
- Ping 
- Scapy

Process:
- Run both scripts using commands in two seperate terminals 
	- Commands
		- sudo python3 arpsniffer.py
		- sudo python3 arptest.py 
- ![[Pasted image 20260812104749.png]]

### summary
Arp sniffer grabs all arp packets and seperate it into "op=1" (query) and "op=2" (answer) arp request types. The command sniff also has a built in error handler so there is no need for "except KeyboardInterupt" to print results after.

