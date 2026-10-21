---
index: true
course: "JC Computing"
chapter: "Network security"
concept: "IDS and IPS"
---

# IDS and IPS

A two stage surveillance system that is situated at the *perimeter* of a network to protect against dubious packets. ^352b9f
### Types
- Behavior based: Detection through trends --> Automated by machine learning
- Signature based: Detection through metadata --> Manual rules update 
- Rule based: Detection through [[access control]] $\_\_\uparrow$ 

| Type      | Pros                               | Cons                                                                 |
| --------- | ---------------------------------- | -------------------------------------------------------------------- |
| Behavior  | Flexible                           | High rate of false positives                                         |
|           | Low maintainance                   | Difficult initial setup (Require large benchmark data to learn from) |
|           | Good for detecting unknown threats |                                                                      |


| Type      | Pros               | Cons                                                                   |
| --------- | ------------------ | ---------------------------------------------------------------------- |
| Signature | Fast               | High rate of false positives (based on strictness)                     |
|           | Easy initial setup | Susceptible to evasion techniques (ie Mac masking)                     |
|           |                    | High maintenance (changing rules according to [[Threat intelligence]]) |

| Type         | Pros               | Cons                                                               |
| ------------ | ------------------ | ------------------------------------------------------------------ |
| Rules        | Fast               | High rate of false positives/negatives                             |
|              | Easy initial setup | Very susceptible to evasion techniques                             |
|              |                    | High maintenance (changing rules for changes in network structure) |
|              |                    | ITS SO BUNS                                                        |
### IDS (Intrusion Detection System)
- Made to detect dangerous or dubious traffic.
- Can *ONLY* alert IPS about the activity and cannot act on it.
#### Placement
##### Host IDS (HIDS/HIPS)
- IDS/IPS that run on host machine instead of network
- Place on [[Crown jewels]] (for protection)
##### Network IDS (NIDS/HIPS)
- IDS/IPS that runs on [[Network segmentation|network segments]] 
- Used to collect network info
### IPS (Intrusion Prevention System)
- Made to actively block and prevent intrusion 
- Done so through: ^98fda4
	- Inspection: *Check the signature* or *Detect anomalous statistics* of incoming traffic
	- Investigation: *Analysis* of the packets or activity (checks data)
	- Action: *Dropping* or putting suspicious packets in *Quarantine* 
	- Log and report: *Logging* of the malicious activity is sent to security personals

![[ips n ids illust.png]]

> [!example]- Example
> | Name                                         | IDS/IPS | type           | notes                                                    |
> | -------------------------------------------- | ------- | -------------- | -------------------------------------------------------- |
> | [[UEBA]] (user and entity behavior analysis) | IDS     | Behavior based | Used in ATA(microsoft advanced threat analytics)         |
> | NTA (network traffic analysis)               | IDS     | Behavior based | detects both inbound, outbound and intra-network traffic |
> |                                              | IPS     | Rule based     |                                                          |
>
> ^4bf4ad
>
