---
index: true
course: "CSIT302"
chapter: "Network security"
concept: "VLAN"
---

# VLAN

- Virtual Local Area network
- Logically separated networks in a larger network

![[Pasted image 20250516221403.png|300]]

| pros              | cons                       |
| ----------------- | -------------------------- |
| Low cost          | Complete network isolation |
| Easy maintainance |                            |
### Use cases 
- [[SME]] organisation
	- Smaller departments easier to separate documents to the own respective departments
	- Complete network isolation is fine
#### Factors to consider
- Business objective
	- yeah when the business is businessing or sm shit fuckass lecture
- Level of sensitivity 
	- How sensitive is the data stored/services available 
- Location
	- Is the business multinational? Is a [[LAN]] enough?
- Security Zone
	- Segmenting for public access 
### Varients
#### Mixed VLAN
- combination of [[VLAN]] and physical [[LAN]] 
### Best practices
- Disable unused ports
- Use SSH to manage your switches and routers.
- Restrict access to the management interface.
- Leverage security capabilities to prevent MAC flooding attacks.
- Leverage port-level security to prevent attacks, such as DHCP snooping.
- Make sure that you update the switch's and router's firmware and operating systems.