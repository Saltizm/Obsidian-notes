---
index: true
course: "CSIT302"
chapter: "Malware and post-exploitation"
concept: "Windows Power shell"
---

# Windows Power shell

- Windows built-in OOP scripting tool
- used for automation

| pro                             | cons                                                                 |
| ------------------------------- | -------------------------------------------------------------------- |
| - Legitimate. Thrfore Encrypted | - Requires [[Remote Desktop Protocol (RDP)]] access (due to SYSTEM user privileges) |

^7ee92d

### Exploits
#### Reverse PowerShell
- Bypass firewall by establishing [[RCE]] using outbound connections through [[Compromised OS| remote desktop]] access
#### Scheduled task
![[Scheduled task]]