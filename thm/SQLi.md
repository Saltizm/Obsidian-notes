---
index: true
course: "thm"
chapter: "TryHackMe practice"
concept: "SQLi"
---

# SQLi

in-band SQLi
- you extract where you exploit
- the query returns the data directly
[[Blind SQLi]]
- you query and no feedback
Error-based SQLi
- you query and extract from an error message
- most common way to enumerate a database
[[Unions-based SQLi]]
- using unions to extract more data from other tables
- most common way to extract large quantity of data
Out-of-band SQLi
- you query and database sends request to you to extract

### Remediation
As impactful as
sql
Injection vulnerabilities are, developers do have a way to protect their web applications from them by following the advice below:

  

**Prepared Statements (With Parameterized Queries):**

In a prepared query, the first thing a developer writes is the

query, and then any user inputs are added as parameters afterwards. Writing prepared statements ensures the
sql
code structure doesn't change and the database can distinguish between the query and the data. As a benefit, it also makes your code look much cleaner and easier to read.

  

**Input Validation:**

Input validation can go a long way to protecting what gets put into an
sql
query. Employing an allow list can restrict input to only certain strings, or a string replacement method in the programming language can filter the characters you wish to allow or disallow. 

  

**Escaping User Input:**

Allowing user input containing characters such as ' " $ \ can cause
sql
Queries to break or, even worse, as we've learnt, open them up for injection attacks. Escaping user input is the method of prepending a backslash (**\**) to these characters, which then causes them to be parsed just as a regular string and not a special character.