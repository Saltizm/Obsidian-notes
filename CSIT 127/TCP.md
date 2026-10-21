---
index: true
course: "CSIT 127"
chapter: "Network protocols and layers"
concept: "TCP"
---

# TCP

Transmission control protocol( TCP ) is a [[network|connection based]] transfer protocol based in the [[Transport layer]]

![[TCP.PNG|500]]
Active open - Connects with only a ***predefined*** Address and port
Passive open - Connects to ***any*** address and port

- 3 way handshake:
	- Source -(SYN)-> Destination
	- Source <-(SYN_ACK)- Destination
	- Source -(ACK)-> Destination


### TCP flags
- SYN - Start session
- ACK - acknowledge request
- PSH - deliver data from transport -> application directly
- URG - signify urgent data
- RST - reset/drop connection
- FIN - indicate a connection is finished

![[Three way handshake|700]]