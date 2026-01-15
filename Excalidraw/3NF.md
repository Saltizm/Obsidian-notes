- Satisfy [[2NF]]
- Have no [[Transitive FD]] (Cannot be dependent on the [[Super key]] through another attribute) 

### Methods
#### Table decomposition
Take that R(A,B,C)
Assume FD:
$A\rightarrow B$ 
$B\rightarrow C$

Decompose the table into
R(**A**,B) and R(**B**,C)

### Issues
Mostly no issues with UDI (update, deletion, insertion)

>[!info] 
>Although this is good enough to eliminate redundancies. Some may arise from alternate keys overlapping with the primary key. This can be solved with [[BCNF]]