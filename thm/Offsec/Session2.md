---
index: true
course: "thm"
chapter: "Offensive security"
concept: "Session2"
---

# Session2

cybersec assume an adversary 
- assume levers will be used to execute attacks -> gives insight into methods attacks will use to resort
prediction > prevention

### Threat actors 
insurance assumes reasonable security measures.

![[Risk quadrants drawing|500]]
**Vulnerability** - Threat/Flaws that cause harm
**Exploit** - to act on a vulnerability

![[Threat actors]]

![[CIA triad]]

#### managing risks
- strict adhesion to CIA triad can lead to unavailability due to it being troublesome  
- scarcity in resource and time may lead to compromise
#### Practices
- Principle of least privilege - grant as much as needed to provide service and destroy all data after
- zero trust (principle of no privilege) - assume no entity is who they claim to be. authenticate, authenticate and authenticate
	- [[just in time access(JITA)]] - limited time
	- [[just enough access(JEA)]] - limited scope
	- dynamic / adaptive [[access control]]
	- [[microsegmentation]]
- open security - even as a whitebox attack, system cannot be compromised
- Defense in Depth - protection on every stage of data
	- increasing scale
		- data
		- applicatoin
		- host
		- network
#### Security policy
- Bell-LaPadula model
- Brewer and Nash model (great wall model)
- Biba model
- Clark Wilson model - security through obfuscation through TP (encapsulation)
- RBAC
- ABAC
#### Left shift security
- build infrastructure to have security built in.
- issue: intense red tape
#### Administrative segmentation
- SSS (Shamir's shared secrets)

Threat modelling - study of how threat actors might act from real world data
Threat intelligence - actionable information gathered from threat models.

A possible exploit being spread in forums (threat modelling) might not be reported and acted upon. However once it is decided to it becomes (threat intelligence)

#### Table Top tactics
- Strategic planning of incident response/prevention
- TTP (tactic, technique, procedure) - describes how a threat will carry out an attack scenario

#### Loggin and chaos testing
- BCP/DR - business continuity plan/Disaster recovery) - security plan for prevention and recovery of/from incidents
- Chaos testing is part of BCP
	- unpredictable event to test infrastructure resilience 