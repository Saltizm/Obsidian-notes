---
index: true
course: "CSIT 127"
chapter: "Network architecture"
concept: "Packet switching"
---

# Packet switching

Packet switching is the transfer of small pieces of **fixed sized** data across various networks. These  “packets”(datagram) allow for faster, more efficient data transfer.

It is the premier connectionless network structure
## Mechanism
Packet switching works by sending packets down different routes in a network. The packet then arrives at different times and is reassembled using information in the **Trailer** of the packet.
![[packet switching.png]]

| pro                                  | con                                                  |
| ------------------------------------ | ---------------------------------------------------- |
| Lower bandwidth                      | Unsuitable for applications that can't afford delays |
| high affordance (can resent packets) | insecure                                             |
|                                      | variable speeds depending on traffic                                                     |
## Anatomy
The communication of one device to another relies on the [[OSI model]] which assemble and disassemble a packet(datagram).

A MTU consist of two main sections:
- [[payload]] (data)
- Header
- Trailer

![[packet.PNG]]

## The payload
This consist of a translated and compressed version of the original data for transfer. 

The data passes through layer 7-4.

## The header
This consist of all of the networking information. It determines the protocol for transfer (TCP/UDP) and information regarding the packet.

The data passes through 3-1. 

## The trailer
This consist information regarding the order of the packets and error correction protocols.

The trailer is added at layer 2.


