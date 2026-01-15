![[Pasted image 20251119031603.png]]
declaration for [[MDP]]

![[policy evaluation.excalidraw|1000]]
### Practice
- This should be formulated as a regression problem. First of all, classification cannot be the choice as the output is boolean. The problem is requires a continuous value that is the abalone's age. Therefore regression is more suitable.

UCS can complete this as it find the cheapest path from start to goal. This question uses a weighted graph.

BFS and DFS both cannot be used as they find the shortest path possible with the least amount of edges.

DP can be used as the graph is non cyclical as the instruction dictate that the forward movement and backward movement are separate.

MDP is model based and RL is model free. this means that MDP problems have information on the entire problem and there are a finite number of states while RL can run continuously without information of the entire problem. Solving through local context.

it is game theory, it involves two agents taking turns making decisions where there is a single outcome usually a win or loss for each party (there is an end state). The objective of game theory is to get an optimal outcome from state s usually done through a variation of minimax or expectiminimax.

This is a MDP and not a search question because actions are not guaranteed and definite. A search algorithm run on the assumption that s, a always leads to s'. However, MDP is perfect for this as the problem posed is indeterministic it also has a finite number of states and predetermined probabilities which satisfies the requirement of MDP.

