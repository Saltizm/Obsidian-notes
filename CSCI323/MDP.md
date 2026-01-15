gen ai for crawling
- restricted web access
- unable to adapt to new data ( uses training data to create solutions )
### Declarations for MDP problems
![[Pasted image 20251119031603.png]]

#### MDP
problem require a finite number of states
- unknown action
- (Model based RL)Value iteration
	- State and action (s, a) 
		- How good is it to do **a** at state **s**
- Policy iteration
	- used when you have a action you want to take
	- State alone (s)
		- Should you proceed? Is state **s** close to goal?
- Reinforced Learning
	- Machine learning
	- A type of Value iteration
	- Q learining (Rl model free learning)
		- Determined through explore-exploit cycle.
		- ![[Exploration diagram]]
	- ![[Q learning formula.avif|500]]
	- epsilon (a explore coeff ) odds of the agent randomly take action.

### Q table 

![[Pasted image 20251025140758.png]]
Discount factor
Q(s, a) the action taken at the old state
maxQ(s', a') the best action at the new state

Q(s,a) + **a(r + y(maxQ(s', a') - Q(s,a)))**

Exploration - disregard Q value and choose a move at random
Exploitation - choose the highest Q value action 

![[Pasted image 20251025142342.png]]
Model based Value learning
- All actions are checked 
- Q* (optimal q) can be estimated from results
Q-Learning
- uses max of all actoin in s' Estimates Q*
![[Pasted image 20251025143214.png]]
![[qlearning.excalidraw|1000]]
optimal Q-value is only received after CONVERGENCE 

A policy in a model that helps make the decision for which action a to take.

utility is cumilative reward