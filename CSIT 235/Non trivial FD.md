---
index: true
course: "CSIT 235"
chapter: "Database design"
concept: "Non trivial FD"
---

# Non trivial FD

if column (B) is not a proper subset of column (A) when A -> B (A functionally determine B)

![[Non trivial venn diagram]]

### Real world implications
Increase search runtime from redundancy.
- Searching StudentID=101 resulting in both "Bob" and "Amy"

Consistency constraints being forgone
- A student id is unique to each student

Data anomalies
- Deleting studentID of student "Amy will lead to "Bob" being deleted as well
