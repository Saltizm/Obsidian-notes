---
index: true
course: "CSIT302"
chapter: "Security assessment"
concept: "Nmap"
---

# Nmap

### .
- Network mapping software ^e4c51b
- Uses packets to determine network architecture  ^70e000
- Uses slower scanning tool that are *less* detectable (can be caught through unusual network activities) ^297c8e

### Scan options
##### Informative Commands 
- [[OS]] details : -O
- Software version : -sV
#### scan type

| Type         | Command | Quirk                                             |                 |
| ------------ | ------- | ------------------------------------------------- | --------------- |
| TCP connect  | -sT     | Performs full 3 way handshake (SYN ACK/ RST NULL) |                 |
| TCP SYN      | -sS     | Doesn't ACK (Send SYN)                            |                 |
| TCP ACK      | -sA     | Send ACK                                          |                 |
| TCP NULL     | -sN     | Send NULL                                         |                 |
| [[TCP FIN]]  | -sF     | Send FIN                                          | bypass firewall |
| [[TCP Xmas]] | -sX     | Non 3 way handshake (FIN PSH URG)                 | bypass firewall |
#### scan port
- -p : defines port (range)
- -F : fast scan (100 ports)
- -r : scan in order 
- -top-ports N : where N is the top number of most common ports
#### scan timing
- Syntax : -TX

| type       | frequency                           | X=x |                  |
| ---------- | ----------------------------------- | --- | ---------------- |
| Paranoid   | 300s (5min)                         | 0   | Evading IDS      |
| Sneaky     | 15s                                 | 1   | Evading IDS      |
| Polite     | 0.4                                 | 2   | Fragile networks |
| Normal     | Sweeping ping                       | 3   |                  |
| Aggressive | Sweeping ping (1.25s response wait) | 4   | Local            |
| Insane     | Sweeping ping (0.3s response wait)  | 5   | Fast Local       |
#### scan output
- To Tli : default
- To greppable format : -oG
- To file : -oN file.txt
- To XML : -oX file.xml

#### Script
- -sC - default scripts
	- http-title : get webpage title
	- ssl-cert, ssl-enum-ciphers : get ssl cert data
		- valid dates 
		- common names
		- cipher type
	- smb-os-discovery : get SMB
		- OS ver
		- Work group name
	- ssh-hostkey : get public hostkey and _its' encryption method_
	- ftp-anon : check for anonymous login for ftp servers
	- dns-zone-transfer : dns config checks/**zone transfers**
### **Vuln**
- find [[Security Vulnerability]] in target