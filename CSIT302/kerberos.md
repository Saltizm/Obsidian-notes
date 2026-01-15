- ticket based authentication protocol
- used for secure over the internet client to server connection

### Tickets
#### Golden ticket
- ticket for a master account "KRBTGT" 
- the account encrypts ***All*** other tickets
- non expiring 
- Provide access to ***all*** services

#### Silver ticket
- a TGT(ticket granting ticket) created by a service account
- Provides access to specific services
- expiring (default to 10hours) 

### Exploits 
#### Pass the ticket
![[pass the ticket]]