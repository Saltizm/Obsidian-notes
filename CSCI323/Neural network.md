---
index: true
course: "CSCI323"
chapter: "Artificial intelligence"
concept: "Neural network"
---

# Neural network

### Types of models
#### Reflex base
- $$x\rightarrow f_{predictor} \rightarrow y$$
- run it through linear algebra 
- [[image classification]] 
- get output y
### Binary classification based
- $$x\rightarrow f_{classifier} \rightarrow y \in \{+1, -1\}$$
- determine if input x is (+1) or isnt(-1) something
- spam detection
### Regression based
- $$x\rightarrow f_{classifier} \rightarrow y \in \mathbb{R} \ response$$
- returns a continuous value 
- predicting house prices 
### Structured prediction
- $$x\rightarrow f_{classifier} \rightarrow y \in \ complex \ object$$
- Machine translation

### Loss functions
- Linear function
	- ![[Pasted image 20251122234025.png]]
	- ![[Pasted image 20251122234958.png]]
- Hinge loss
	- ![[Pasted image 20251122235923.png]]
- activation function
	- ![[Image Classification#^b8a564]]
- SGD (stochastic gradient descent)
	- just take one example (x,y) and update all weight from loss(x,y,w)
	- many small updates 
- GD (gradient descent)
	- iterate through all Sumation(x,y) update each weight from loss(x,y,w)
	- few big updates
- Feature map
	- $$\phi(x)\ feature\ map$$
	- $$\phi(x)=[1,x^2]\ quadratic\ fm$$
	- 