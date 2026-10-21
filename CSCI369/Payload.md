---
index: true
course: "CSCI369"
chapter: "Exploitation techniques"
concept: "Payload"
---

# Payload

### .
- The actual code that executes on the target system after an exploit successfully executes
### Types of payloads
#### Singles
- Self-contained and standalone. (runs without other programs)**
- ===windows/shell/bind_tcp===
#### Stager
- Establish and maintain communication between attacking server and victim
- Stagers download stages **
- windows/shell/===bind_tcp===
#### Stages
- Payload components  
- windows/===shell===/bind_tcp
> [!example]- Example
>
> ##### Ransomware
> - Stager and stages
> ![[Ransomware#^7c991b]]
> #### Trojan
> - Singles
> ![[Trojan#.]]