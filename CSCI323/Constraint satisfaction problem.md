CSP revolves around HARD constraints 
- Example (sudoku)
[[MDP]] revolves around SOFT constraints (penalties)
### Declaration for CSP
- Variable
- Domain
- Constraint 
- Weights
![[Pasted image 20251120020510.png]]
### CSP format
![[Pasted image 20251120164407.png]]
- domain - list of possible value for each variable 
	- $$X_1 \rightarrow D_1$$
- Constraint factor
	- $$f_2(Variables) = [constraint condition(X_1=X_2)]$$
- Assignment
	- $$weight=\Pi(f1..fx)$$
#### Hard/soft constraints
$$Hard\ constraint-[X_1 = X_2]$$
$$Soft\ constraint-[X_1 = X_2] + C\ \ \ where\ c \propto \frac{1}
{Importance}$$

#### Pruning
- remove all the 0 values in hard constraints to prevent it from propagating
- Change the domain as you do this
#### Dynamic ordering
- Steps 
	- MCV ( most constraint var )
		- Find the variable X with the most number of constraints
	- LCV( least constraint var )
		- pick the value for X in domain that reduces the other domain the LEAST
#### Local search
- Use backtracking or minimum conflict local search
- Minimum conflict
	- go to a variable that has conflict 
	- change the value until there is no conflict 
	- iterate 