---
index: true
course: "Independent study"
chapter: "Cybersecurity practice"
concept: "ARP Scanner"
---

# ARP Scanner

## Lab environment

![[Assignment 1 Lab environment]]

## Process

- Run both scripts using commands in two seperate terminals 
	- Commands
		- sudo python3 arpsniffer.py
		- sudo python3 arptest.py 
- ![[Pasted image 20260812104749.png]]

## Summary

Arp sniffer grabs all arp packets and seperate it into "op=1" (query) and "op=2" (answer) arp request types. The command sniff also has a built in error handler so there is no need for "except KeyboardInterupt" to print results after.
