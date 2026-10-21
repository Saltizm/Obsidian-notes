---
index: true
course: "CSIT302"
chapter: "Identity and access management"
concept: "GPO"
---

# GPO

- Group policy object
- A collection of settings that define what a system will look like and how it will behave for a defined group of users.
- Distributed by:
	- Admin
- Can be enforced on:
	- [[Organisation Units]] (OU)
	- [[Domain]]

### Features
#### Set limits on Control panel
- prevent non admin users from modding system configuration 
#### Prevent Windows from storing LAN manager hashes
- Prevent [[pass the hash]] attacks
#### Control access to command prompt
- Can be used to run commands that are [[legitimate]]. Can give high level access and evade other restrictions listed. 
#### Disable forced system restarts
- Prevent [[Persistence(Cybersecurity)|Persistent malware and scripts]]
#### Disallow removable drives (DVD and CDS)
- Prevent [[RDA (remote drive access)]]
- Prevent [[Malware]] that spread through external drives
#### Restrict Software installation
- Prevent [[Malware]]
#### Disable guest
- Prevent [[living off the lands]] exploits 
#### Password policy
- refer to [[Password policy]]  
- Restrict minimum password length
- Restrict password age (How long before expiry -> Reset)
#### Disable anonymous SID
- [[SID]] can be used to perform [[pass the ticket]] attacks in older systems