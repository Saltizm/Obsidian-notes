---
index: true
course: "CSIT 127"
chapter: "Addressing and routing"
concept: "DHCP"
---

# DHCP

Dynamic Host Configuration Protocol ( DHCP )  assign DHCP IP addresses are temporary and would expire after specific period of time. ( Default = 1hour ). 
Clients can negotiate for renewal before expiry.


## Function
- Assign Dynamic IP addresses to [[LAN]] devices
	- When client issue IP request:
		- Look at static table:
			- IF no entry:
				- select IP address from available pool 
			- IF has entry:
				- reject request


### Cybersecurity 
![[DHCP guard]]