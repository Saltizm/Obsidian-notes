A system to prevent unauthorised access from entering a private network. ^9a30f9

### *purpose*
- prevent malicious activity from spreading
- filters infomation(packets) from the internet ^f94ea8
	- this is done through an ![[Access Control List]]
	- The filtering is done through: ^e7d30a
		- Port and/or Proxy filtering (application blocking)
		- Mac filtering (device blocking)
		- Ip/[[Packet filtering]] (network blocking)
		- Content filtering (Censorship)
		- [[Dynamic filtering|Dynamic/Stateful filtering]] (Contextual blocking)


### Types of firewalls *implementation*
#### host-based firewall (software)
- examples:  *window defender firewall, zone alarm firewall, antivirus firewalls*
#### network-based firewall (software and hardware)
 - examples: *built in firewall, stand-alone firewall, cloud infrastructure firewall*
#### web application based firewall (WAF)
- example: *AWS WAF*
- Generally Hardware-based 
- Used to filter network traffic to web applications ([[IaaS]])

<h5>note: corporation used a combination of both to have more than one point of failure</h5>

Drawbacks of firewalls:
- single point of failure
- vulnerable to *internal attacks*



