---
index: true
course: "CSIT 127"
chapter: "Addressing and routing"
concept: "NAT"
---

# NAT

NAT let router represent entire local area network to internet as a single [[IP|IP address]] (Public IP).
A very important part of implementation of the internet( subnetting ).

## Function
- Encapsulate all devices in a [[LAN]]
	- all interaction in a network is done through the public IP
	- secure and private
- Assign a [[IP|public IP address]] for the whole network

### Translation
The host wants to send a packet to the [[internet]].
[[NAT]] provides the host with the next ***public IP*** in the available pool.
the router stores this as cache in the [[NAT|NAT table]] 

The receiver sends a packet back.
[[NAT]] look through the [[NAT|NAT table]] for the corresponding field with the ***host public IP*** and retrieves it's ***private IP***.
the packet is sent to the host.

