---
index: true
course: "CSCI323"
chapter: "Artificial intelligence"
concept: "T"
---

# T

phi(x) - transform input data into 2d space seperable by a decision line

update w and b during backpropagation

backprop only done in multilayer llms. 
linear and svms do not need it.

w' = w - n(dloss/dw)

ML DL and linear regression are differentiated by how many convolution layers and how  feature vectors are processed


### Linear regression
goal - predict a continuous value
y,x

y = w.x + b


loss(y,x,w) = (fw(x) - y)^2
this is gradient descent

SGD(  stochastic gradient descent ) is whene you apply gd to only a single selected data to calculate gradient

for computational efficiency when the dataset is very large

if learning rate is very big, min value (goal) is very hard to reach

learning rate is how much points on a graph change



![[Pasted image 20251112125216.png]]
1.)
compute forward pass
differentiate to find gd (loss)
compute new w, b 
draw quadratic graph

sparse data set refer to data that have a lot of zero

MDP
markov property - the future of the process depends only on its present state, not on it's past histroy   <the past does not matter ( only future states)>

if markov property is satisfied, use MDP



