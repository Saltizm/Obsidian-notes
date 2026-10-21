---
index: true
course: "CSCI323"
chapter: "Artificial intelligence"
concept: "Notable examples"
---

# Notable examples

- Dice game
	- 10 dollar for not playing
	-  4 dollar for rolling 2 dice
		- 1, 2: end
		- else : continue 
	- highlights uncertainty when game is played 
- Policy evaluation route
	- You CHOOSE to stay and play
	- ![[Pasted image 20251025130429.png]]
- Value evaluation route
	- uncertain to play or leave
	![[value eval format.avif|500]]
	Steps:
	- propagate from the goals ( 2, 50 )
	- value is added to the tile moved 
	- iterate till whole map is filled 
	- Move according to results from starting point
	![[Pasted image 20251025132935.png]]
### Expetimax 
- Game : roll dice
- Agent : player
- Action: play or skip ( no cascade )
- Play 
	- 1/6 get 10
	- else 0
- Skip
	- get 3
- ![[Pasted image 20251119174356.png]]

Format
Player {x,y}
State s: {positions}
Action(s) a: {legal moves}
isEnd(s): s is checkmate or draw (king has nowhere to move)
Utility(s) : +inf white win, -inf black win

Alpha beta pruning
recursive 
 initialise all MAX nodes as - inf, MIN nodes as + inf
traverse and compare in post order through the  leaf (Lchild, node, Rchild)
move the MIN/MAX value to the parent once a layer is complete

 