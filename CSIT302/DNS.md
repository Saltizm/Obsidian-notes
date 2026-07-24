- Domain name service 
- Hierarchical naming system for domains
### THM
- TLD - top level domain
	- gTLD (generic)
		- .edu, .app, .web
	- ccTLD(country code)
		- .sg, .au, zn
- SLD - second level domain
	- Limits:
		- 63 char long
		- lower char
		- 0-9
- subdomain
	- domain dir
	- Limits:
		- 63 char long
		- lower char
		- 0-9
	- can be stacked up to 253 characters
- Recursive DNS
	- asks other server for address (usually in cache)
- Authoritative DNS
	- has a phonebook of dns records
### Example 
Company.com (Root)
- Dubai.Company.com(Child)
- China.Company.com(Parent)
	- Shanghai.China.Company.com(Child)
### DNS records
Can be access either through a [[Whois]], or [[nslookup]]
- consist of tuple:
	- {name, value, type, ttl}
	- name - Domain name
	- value - IP address
	- type - type of value attached to Domain name
	- TTL - how long the packet can stay
#### Types 
- Type = A
	- IPV4 address
- Type = AAAA
	- IPV6 address
- Type = CNAME
	- canonical name
	- unique alias for domain (e.g. www.uow.au -> uoweduau-lb01-production.terminalfour.net)
- Type = MX (CNAME subtype)
	- mail server (mail exchanger)
	- (uow.edu.au -> 100 au-smtp-imbound-1.mimecast.come)
	- XX (CNAME) 
		- XX - preference value 
			- The lower this is the more preferred (packets more likely to end up here)
- Type = NS
	- authoritative DNS server for the Domain name
	- (e.g. dns1.uow.edu.au)
- Type = SOA
	- Does the same thing as NS but ONLY for the primary one (Primary DNS)

### DNS servers
- A server has a permanent database and a cache
- cache:
	- Stores DNS records that are frequently accessed for better response time
- Database:
	- contains all DNS records 
#### DNS records
![[cname drwaingg|500]]
### Regarding cybersecurity
![[nslookup]]
#### DNS poisoning
![[DNS poisoning]]