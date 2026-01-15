Dynamic Host Configuration Protocol ( DHCP )  assign DHCP IP addresses are temporary and would expire after specific period of time. ( Default = 1hour ). 
Clients can negotiate for renewal before expiry.


<h2>Function</h2>
- Assign Dynamic IP addresses to [[LAN]] devices
	- When client issue IP request:
		- Look at static table:
			- IF no entry:
				- select IP address from available pool 
			- IF has entry:
				- reject request


### Cybersecurity 
![[DHCP guard]]