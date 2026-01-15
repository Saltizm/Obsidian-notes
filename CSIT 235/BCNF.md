- Satisfy [[2NF]]
- Automatically will satisfy [[3NF]] upon normalizing to **BCNF**
- Cannot have non-trivial dependency relations 
	- $A \subseteq B$  ,FD $A \rightarrow B$ (non trivial)

### Method
#### Table decomposition 
Take that R(A,B,C)
assume FD:
$AB\rightarrow C,D$
$B \subseteq C$
$\therefore C\rightarrow B$ (Non trivial)

The table should split into 
R(A,C,D) and R(C,B)
*turn the non trivial FD into a separate relation*

>[!note]
>BCNF violations can only occur if there are two **composite** [[Candidate key]] 
>that **overlap** 

### Issue
No UDI issues.

#### loss of FD
- composite primary key's FD will be lost when decomposed into sub-tables. 
- R(A,B,C) with FD $AB \rightarrow C$ will decompose into R(A,C), R(C,B)

#### Unnatural 
- Tables are decomposed more than in [[3NF]]. Difficult to Read.
- Assuming A is name, B is course, and C is professor. The tables will be
	- R(Name, professor) 
	- R(professor, course)
- It would be difficult to determine the student's course at a glance