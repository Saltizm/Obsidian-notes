---
index: true
course: "CSIT302"
chapter: "Network security"
concept: "Packet filtering"
---

# Packet filtering

- done on the [[Network layer]] 
- Inspects and filter fields within packet against a set of rules:
	- **Source & Destination IP Addresses**
	- **Port Numbers** (e.g., TCP/UDP)
	- **Protocol Type** (e.g., HTTP, FTP, ICMP)
	- **Packet Flags** (e.g., SYN, ACK in TCP)
	- **Interface Direction** (incoming/outgoing)

### Operation
#### Drop
- Silently discard the packet
#### Allow(permit)
- Let the packet enter network
#### Block(deny)
- Deny the packet and alert system

### Types
#### Stateful packet filtering
![[Stateful packet filtering]]
#### Stateless Packet filtering 
![[Stateless packet filtering]]
