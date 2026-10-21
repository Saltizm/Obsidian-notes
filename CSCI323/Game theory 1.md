---
index: true
course: "CSCI323"
chapter: "Artificial intelligence"
concept: "Game theory 1"
---

# Game theory 1

Multiple actor 
Decision making 
env adversarial in nature - one actors increase results in one actors decrease

MDP ( single actor )
- require a finite state space

#### Types
- Two player zero sum
- Stochastic games (randomise)
	- probabilistic events (coin flips/ dice rolls)
- multiplayer, non zero sum

#### Formulas 
![[Pasted image 20251118155307.png]]
Game Theory (GT)
Minimax - no Transition probability
Expectiminimax / Expectimax - has transition probability P


No reward for both, only goal is terminal state (win / lose)
V value is best achievable outcome from state s. (NOT cumilative)

MM - Max > min> max > min (chess)
EM - max > chance > max > chance ( dice game )
EMM - Max > chance > min > chance > max > chance (2 player dice game)
![[postorderminimax.excalidraw]]
#### Alpha beta pruning
type of tabulation DP.
When the other branch does not provide any values that could be lower than the parent. Prune it.
set 2 variables for every node, Alpha, Beta
$$\alpha=-\infty\ \ \ \beta=+\infty$$
update the values when parent > alpha/ parent < beta and **when traversing down a tree** (global var). 
repeat until 
$$\alpha>=\beta$$
### Time complexity
$$without\ pruning-O(b^d)$$
$$with\ pruning-O(b^{d/2})$$