![[Nmap]]
### Windows 
- TCP port discovery
	- Test-NetConnection -Port (port) (ip)

### Site ports
- Port 80 : http
- Port 443: https
### SMB enumeration
- Server Message Block
- -v/-vv/-vvv : verbose 
- net view 
	- Shows the current network share 
		- Network share: shared file directory in the network
	- Admin (public) Admin$ (private)
- enum4linux
	- used to enum through window machines to list details about the machine
	- Commands
		- -U userlist
		- -M machine list
			- accounts / machines joined to current target through [[Active directory]] or window work group 
		- -S Share list (similar to net view)
		- -A/a show all (simple) enum
			- usgproni