---
index: true
course: "CSIT302"
chapter: "Security assessment"
concept: "Metasploit"
---

# Metasploit

### .
- A pen testing tool with a collection of [[CVE(Malware and exploits)|known exploits and payloads]].
- **Specialised for Exploit development and execution**
- is a Exploitation framework
- Used with [[Nessus scanner]] or other scanning tools to find exploits (Security auditing)

### Exploitation steps
1. Vulnerability - Check whether the intended target system is susceptible to know vulnerabilities.
2. (Prepare) Exploit - Select and configure an exploit, taking advantage of said vulnerabilities.
3. (Prepare) Payload - Select and configure a payload
4. Execute - The exploit.
VEPE 
#### Mock scenario
- Use [[social engineering]] principle to leverage a **Trojan** to be received by the victim. Leveraging (CARLSV) the 6 levers. 
- Trojan establish connection to C2 server (command and control server) and creates a [[reverse shell]] 
- Go through VEPE, create and execute the exploit using **Meterpreter** payload provided by Metasploit 
>[!Meterpreter]-
>A metasploit attack payload 
### Commands
- msfconsole : open metasploit console
- help : help instructions
- search \[Keyword\] : Search engine for exploits
- use : use exploit, payload or auxiliary 
- show options : Display options for current module
- run : execute *auxiliary*
- exploit : execute *exploit*