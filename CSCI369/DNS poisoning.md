### .
- Changing DNS records to redirect network traffic
- Make use of firewall leaving port 53 open for [[CSIT302/DNS]] queries to bypass firewall
- a [[Dropper]] method
### Process
#### Method 1
- prerequisite:
	- need to be in local DNS server network
---
- Modify DNS record in caching DNS server to redirect to attacking server
- ![[Pasted image 20250826003718.png|500]]
#### Method 2
- Leveraging [[MITM]], intercept DNS request response and modify it to redirect to attacking server 
- ![[Pasted image 20250826003705.png]]