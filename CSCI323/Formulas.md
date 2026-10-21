---
index: true
course: "CSCI323"
chapter: "Artificial intelligence"
concept: "Formulas"
---

# Formulas

### Policy evaluation
![[Pasted image 20251025125053.png|500]]
summarise:
v = 
- summation of all actions doable at state **s** (not required)
- summation of all states for an action a.
- reward (outcome) for previous action
	- walking incurr negative reward. (requires resources )
- gamma (Discount factor) : (0,1) range. With 1 being future forward.
	- IF it is deterministic (There is finite iterations) gamme = 1
### Value evaluation
![[Pasted image 20251025125721.png|500]]
- same as Policy evaluation, but multiply for all actions
T is probability of action succ  
R is reward
y is Discount factor
V is Q for staying