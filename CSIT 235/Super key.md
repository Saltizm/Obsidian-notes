---
index: true
course: "CSIT 235"
chapter: "Keys and relational schemas"
concept: "Super key"
---

# Super key

- A set of attribute/ An attribute such that when closed will determine the entire [[Relational schema]] 
- May not be suitable

### Creation
consider R(A, B, C, D) has FD:
$A \rightarrow B$
$C \rightarrow D$

The relation will close with:
$\{A\}^+ = \{A, B\}$
$\{C\}^+ = \{C, D\}$

Therefore the super key of this [[Relational schema]] will be:
$AB^+ = \{A, B, C, D\}$
