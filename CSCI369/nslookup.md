- [[Kali linux]] tool used to check for DNS servers 
- Used to obtain:
	- DNS records
	- NS record **
### Command format
```
nslookup [options] [name] [server]
```
- Options :
	- -type=(DNS record type)
	- -debug : verbose 
	- -port=(Port) : change port from default (53)
- Name : ip addr/ hostname
- Server : select DNS server to obtain DNS record from
![[DNS#Types]]
### Exploiting nslookup
- using nslookup with "-type=ns" to locate domain server
- Can search for unused subdomains to launch a [[Subdomain takeover]]
