---
index: true
course: "CSIT302"
chapter: "Identity and access management"
concept: "pass the ticket"
---

# pass the ticket

- to pass a [[kerberos]] ticket to another machine to login into the victim's account

### Types 
#### Kerberoast golden/silver ticket
- requires:
- the KRBTGT/target service account hash (through [[pass the hash]])
- the KRBTGT/target [[NTLM]] hashes or [[AES]] keys
- the KRBTGT/target [[SID|domain SID]] and [[CSIT302/DNS|domain name]]

