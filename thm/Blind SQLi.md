---
index: true
course: "thm"
chapter: "TryHackMe practice"
concept: "Blind SQLi"
---

# Blind SQLi

### Always true query
' OR 1=1;--
'--' ignore all proceeding commands
### Enumeration with wildcard
`admin123' UNION SELECT 1,2,3 from users where username like 'a%`
iterate thr variation of % to find name.
### time based (sleep based) query
`admin123' UNION SELECT SLEEP(5);--`
an successful execution will return with a 5ms delayed response