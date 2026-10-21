---
index: true
course: "Independent study"
chapter: "Cybersecurity practice"
concept: "ARP Test and ARP Spoofing"
---

# ARP Test and ARP Spoofing

## Lab environment

![[Assignment 1 Lab environment]]

## Process

- Pinged target machine to check if it up
![[Pasted image 20260810003040.png]]
- Ran "arptest" scapy script to receive target's MAC address to use for arp spoofing and saved the received MAC address and ip under "clues.txt"
![[Pasted image 20260810002242.png]]
- received the gateway router ip.
![[Pasted image 20260810003126.png]]
- Wrote a script for arpspoofing name "arpspoof.py" and ran it with the command 
	- "sudo python3 arpspoof.py 10.0.2.3 10.0.2.1"
![[Pasted image 20260810004913.png]]
![[Pasted image 20260810004807.png]]
- Run the following command and check if the mac address has been updated while arpspoof.py runs in the background
	- tcpdump > dump.txt
- This is the result from grep 'ARP' 
![[Pasted image 20260810004622.png]]

## Summary
The Arp attack works by sending layer 2 packets (ARP) to both the gateway router and target. 

Packet to the target convinces the target that you are the gateway
Packet to the router convinces the router your are the target

This is a setup intercepts all network traffic between the two to set up for a MiTM attack.

After spoofing, the ARP table is restored to what it was by sending ARP packets to reassign the correct MAC address to each corresponding network address.