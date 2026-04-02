```mermaid
---
title: SDLC steps
---
flowchart TD
id1["Identify problem/need and obtain approval ( vision doc )"] -->
id2[Define scope and objective] -->
id3[Plan and monitor the project] -->
id4[Specify requirements for solution] -->
id5[Design the system component that solves the problem] -->
id6["`Build, test and integrate system *Components*`"] -->
id7[Complete system tests and the deploy solution]

style id4 fill:black
```

<h2>Requirements</h2>
Defined by [[FURPs]]

Requirements are separated into two categories:
**Functional**
- F ([[Functionality]])
- Fundamental components that are required for operation
- Examples:
	- Wheels on a car
	- Legs on a table

**Non-functional**
- URPs ([[Usability]], reliability, performance, security)
- Additional features that are ***important*** for other aspects besides function
- Example:
	- Locks on car door
	- Rounded edges on a table

