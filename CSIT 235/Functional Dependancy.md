---
index: true
course: "CSIT 235"
chapter: "Functional dependencies"
concept: "Functional Dependancy"
---

# Functional Dependancy

IF every value in a column (A) is [[One to one functions|one to one]] onto column (B). 
A functional dependency can be denoted as the function:

f: domain(A) -> domain(B)

this can also be represented as

A -> B
##### format
functional dependency A->B is valid in a relational table R.
or
A functionally determines B.
or
FD A->B
### Overview
![[functional dependancy mind map|1000]]
### Proof
For R(A1, A2, ... An), 
Let X, Y be the non empty subsets of R
R ∀ X,Y (every pair X,Y in R)
functional dependency X->Y is valid in relational schema R (X functionally determines Y)

##### examples:
![[Pasted image 20250411185214.png|500]]
### Implications 
- To describe semantics of data 
	- reflection of real world consistency constraints:
	- studentID -> studentName
- Check relational schema
