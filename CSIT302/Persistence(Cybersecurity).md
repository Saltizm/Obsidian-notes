---
index: true
course: "CSIT302"
chapter: "Malware and post-exploitation"
concept: "Persistence(Cybersecurity)"
---

# Persistence(Cybersecurity)

- Mechanisms that allow [[Malware]] to persist *Reboots, logoffs and reinstallations* 
### Advanced Persistent Threat
- threat that:
	- Possess sophisticated level of **expertise and significant resources**
		- Many attack vectors
	- Establishing and extending foothold 
		- Use it to exfiltrate, impede critical process, Persist
- Typically:
	- Government operation
	- [[MNC]] 
- Targets:
	- finance 
	- government 
	- energy
	- healthcare
- APT only attacks only focuses on its pre-defined goals, Limited attack range 
- APT can work for long periods (Continuous)
	- Long term campaigns, can wait for years to strike
	- Adapt to failed attempts 
	- Have access to government intel ( no need for diversion )
### Registry based persistence
### Cross platform persistence
- Persistence through [[Lateral movement]]
#### Cloud persistence
##### Malicious lambda functions
![[lambda functions]]
##### Backdoor IAM Roles
![[IAM roles]]
#### Living off the land (LOLBins)
![[LOLBins]]