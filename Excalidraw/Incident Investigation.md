### Scoping the incident
- Process to determine a given incident is security related 
##### Why scope
- to determine if it is our problem to solve. (not all incidents are security incidents)
### key factors of scoping
- Is the issues repeatable
- Is the issue widespread and frequent 
- [[Threat intelligence|Collect data for further analysis]]
>[!note]-
>More data doesn't mean better investigation
>More data can obscure key information from being seen

###### Examples:
---
- A website is running "slow" - could be a [[DDOS]] attack but also might be the user's machine being slow.
	- Perform a basic performance troubleshoot
	- Check if other machines are experiencing the same issue ( frequency )
	- Document all steps taken as instruction for other end users
---

### Lesson learned
- After an initial attack, A document detailing what could have been done better should be created

###### Examples:
---
- To prevent future false positives. A system should be put in place to detect DDOS attacks instead.
- Benefits:
	- Save company hour
	- Reduce disruption to operations
---
