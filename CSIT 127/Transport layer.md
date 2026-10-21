---
index: true
course: "CSIT 127"
chapter: "Network protocols and layers"
concept: "Transport layer"
---

# Transport layer

Originally a part of the TCP/IP layer in the TCP model. The [[OSI model]] has adapted it into 2 separate layers. The [[Network layer]] and the [[Transport layer]].

Transport layer is responsible for creating a "virtual connection" between devices to establish a reliable data stream.

## Function
- To establish connection between 2 devices using [[Network port|port numbers]]
- Flow control 
- Reliability
	- end to end correction
		- Checksum
	- Resent packets when packets are:
		- Lost
		- Corrupted
- Manage packet order
- Priority transfer of high priority Data (Urgent Pointer)

Features:
Transport Layer can handle multiple application's transfer over a single IP line (network connection) using [[Time division multiplexing( TDM )]].

### Anatomy
***TCP header***
![[TCP segment.PNG]]

### Security
- Transport layer security 
- Consist of various protocols that ensure data streams are secure  ^749942
- Protocols: ^83a259
	- [[TCP]] (connection based)
	- [[UDP]] (connectionless)
### Port numbers
![[Network port]]