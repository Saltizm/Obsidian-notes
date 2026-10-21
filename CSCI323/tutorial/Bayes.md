---
index: true
course: "CSCI323"
chapter: "Tutorials"
concept: "Bayes"
---

# Bayes

- Comparison to CSP
	- CSP
		- constraint based 
		- uses factor graphs
	- Bayesian network (BN)
		- computes likelihood and predictions
		- use DAG (directed graphs)
#### Definition
##### Rule 1
- Identify a DAG or paragraph descripting a DAG ( bayesian problem )
- $$let\ X = (X_1, ..., X_n)\ be \ random\ variables$$
- bayesian network is a **joint distrubution** over X as a product of **local conditional distrubutions**
- Immediately write down the joint dist of the DAG (dag representation)
- LIST the parents and child!!!! to avoid mistakes
> [!example]- Example
> ![[Pasted image 20251121024242.png]]
> bayesian network = joint probability of all events
>
> C, A - no parents, P(C/A)
> H - parents are C and A. P(C|A, C)
> I - parent is A. P(I|A)
>
> P(C|A,C) = P(C|P(A)xP(C)) = \[P(AnC) x P(A)\]/P(AnC)
##### Step 2
- Write down the conditional probability table (CPT)
- ![[Pasted image 20251121024852.png]]
- P(negH) + p(H) = 1
##### Step 3
- use the conditional probability formula to solve?

##### Example of full question
![[Pasted image 20251121030228.png]]
draw CPT and evaluate 
Expert system, rule based Ai system > logic language (prolog)

goals 
- Represent knowledge 
- Reason with AI model
anatomy
- Syntax - valid set of operation (formulas)
- Semantics - for each formula specify a set of model
- inference rule - given formula f, what new formula g can be made
Interpretation function 
- ![[Pasted image 20251121034501.png]]
