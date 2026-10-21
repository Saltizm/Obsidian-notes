---
index: true
course: "CSIT302"
chapter: "Detection and response"
concept: "IoC (indicator of compromise)"
---

# IoC (indicator of compromise)

>[!note]+
>A intrusion with many artifacts indicate high confidence from the attacks possible nearing the end of  the [[Kill Chain]]

| IOC                                                 | Description                                                                                                            | Signs                                             |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| [[Unusual outbound traffic]]                        | Compromised systems will often perform a [[reverse shell]] attack to connect to external (command and control) servers | >Increased network traffic                        |
|                                                     |                                                                                                                        | >Mismatched [[Network layer\|packet]] information |
|                                                     |                                                                                                                        |                                                   |
| [[Anomalies in privileged user account activities]] | Attackers has compromised privileged user. Potential [[Access and privilege Escalation]]                               | >Changes in time of activity                      |
|                                                     |                                                                                                                        | >Changes in volume of info accessed               |
|                                                     |                                                                                                                        | >Changes in systems accessed                      |

^68f411

^e761d2
### Prevention
#### IDS and IPS
![[IDS and IPS#^352b9f]]
![[IDS and IPS#^4bf4ad]]
> [!example]- Example
> #### Petya ransomware
> - Strange [[Windows Power shell]] commands in log
> 	- command made to reschedule a restart
> - [[Port]] scanning on TCP139, TCP445