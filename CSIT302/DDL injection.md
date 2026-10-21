---
index: true
course: "CSIT302"
chapter: "Application security"
concept: "DDL injection"
---

# DDL injection

[[DDL]] injection refers to a technique used to force a **Running process** to run a [[DDL]] (dynamic link library)

### Techniques
##### CreateRemoteThread
- Injects DLL via 'LoadLibrary' in a remote process.
*used by*
Malware, Cheat engines

##### APC injection
- Use APC( asynchronous procedure calls) to queue DDL to load
*used by*
Malware(advanced)

### Reflective DLL injection
- Loads DDL directly from memory
*used by*
[[CSIT302/Metasploit|Metasploit]], Cobalt Strike

#### SetWindowsHookEx
- Injects via windows message hooks
*used by*
key loggers, spyware 

#### Process Hollowing
- Replace legitimate process codes(DDL) with malicious DDL
used by 
fileless malware 

### Detection and mitigation

##### Prevention
✔ **Use ASLR (Address Space Layout Randomization)** – Makes injection harder.  
✔ **Enable DEP (Data Execution Prevention)** – Blocks malicious code execution.  
✔ **Restrict process permissions** (e.g., **Microsoft EMET**).  
✔ **Monitor for unusual DLL loads** (Sysinternals `Autoruns`).

##### Detection
Process Explorer
Window event logs