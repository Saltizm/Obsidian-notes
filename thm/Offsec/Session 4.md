---
index: true
course: "thm"
chapter: "Offensive security"
concept: "Session 4"
---

# Session 4

No plan survive first contact with the enemy 
- write for in the moment (notetaking)
	- Guideline for notetaking
		- detailed action recording. Don't assume you will recall
		- record **Exact commands and actions** 
			- Example:
				- During a web pentest
				- record:
					- Application name 
					- Url
					- Request type 
					- Issue Details - link to cve/ categorise to adj cve
					- poc (proof of concept) payload
		- 
- complete report after 
	- Purpose:
		- So that pentest can be repeated to demo t show issue is real
		- So that pentest can be repeated to determine if issue is fixed
		- To rule out pentest as the cause for system failure
- ![[Pasted image 20260730101540.png]]
- screenshots
	- Should show one thing at once
	- should fully represent what you are doing (no obfuscation)
	- Should be client specific (show target in screenshot)
ROE (rules of engagement) - set of agreements between ethical hackers and contractor. Acts as a referee for all pentest action taken.

When weighing vulnerability enforce [[Quantitative risk analysis]] and carry out according to the client's needs

Report should fit the clients technical level. Multiple sections must be provided for different levels.

Demographic:
- C level functions - low technical 
	- describe outcome and impact of engagment
- IT department - high technical
	- sufficient technical detail to recreate pentest and enforce fixes

**Structure**
- Executive summary
	- lay down scope 
		- example: refusal due to number of vulnerability.
		- example: limited budget / feasibility issues
	- time frame
	- Rules of engagement
		- lay down testing methods that will be used
	- supporting infrastructure and accounts (needed to carry out pentest)
	- **Tone** - should be detailing the Worst case scenario. Do not undersell or over sell severity. Follow [[Quantitative risk analysis]]
	- **Example**
	- ![[Pasted image 20260730103452.png]]
- Testing env consideration
	- post game review basically
	- positive outcome - "There were no limitaition or extenuating circumstances"
	- neutral outcome - "There were some issues in access control. However, findings were not affected"
	- negative outcome - "pentest was not suffciently carried out due to xyz constraints"
- Technical Summary
	- User and Privilege Management
	- Architecture
	- Authorizationc
	- Patch Management
	- Integrity and Signatures
	- Authentication
	- Access Control
	- Audit, Log Management and Monitoring
	- Traffic and Data Encryption
	- Security Misconfigurations
	- **Example**
		- ![[Pasted image 20260730104351.png]]
- Technical finding and recommendation
	- Format
		- Ref, Risk, Issues Description and implication, Recommendation 