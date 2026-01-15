### .
- Sweeping ping (sends request to every [[Endpoints|endpoint]])
- Detectable 
### Types
#### Ping
- Send a [[ICMP]] packet over to 1 IP address
- Command:
	- ping 192.168.0.1
#### Fping
- Send many [[ICMP]] over to many IP address
- Command:
	- fping -h (help)
	- fping -g 192.168.0.1 192.168.0.1/24 (Specific IP) 1.0.0.1-1.0.0.10 (Range IP)
	- fping -f ip_addr.txt (import from file)