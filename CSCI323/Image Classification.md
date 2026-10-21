---
index: true
course: "CSCI323"
chapter: "Artificial intelligence"
concept: "Image Classification"
---

# Image Classification

Implementing logic is important in ai safety

### Machine learning
### Deep learning
DNN ( dense neural network ) == MLP ( multilayer perceptron)

Deep learning - **Building knowledge**, step by step through **Layers**.
L1, Dots, lines 
L2, Parts (ear, mouth)
L3, Semantic information (cat, lion)

More convolution layers -> more additional information
#### Feed forward neural network
- Raw input into **predictions**
- outputs are **probability** for each **class** denoted as $$f(x)->\hat{y}$$
##### Input
- Product rule : **number of column in A == number of row in B**
- 28x28 input would be flattened
- 28x28 -> 784x1
- input layer = 784x1
- Matrix multiplication:
>[!diagram]-
>![[matrix mult.excalidraw|1000]]
![[Pasted image 20251117163827.png]]
- Process (1 epoch) ^b8a564
	- Forward pass
		- $$Z = W.\phi(x) + b$$$$h(x) = \sigma(Z)$$
		- activation function 
			- Used to extract values >0 (non-negative features, x). Remove features that are not accepted
			- Threshold: 1\[z>=0\] - Ignore all negative feature, analog 1, 0
			- logistic: 1/(1+e^-x) - accept near zero negative values
			- ReLU: max(z,0) - ignore all negative feature, linear (best performance)
		- weight (matrix)
	- Loss function -> update w, b
	- Back propagation 
		- Loss equations
			- Cross entropy loss - ylog(y^) (classification)
			- mean squared error - 1/n(sum(y^-y)^2)  (regression)
		- weight update 
			- dl/dW, dl/db (diff irt weight and bias) 
			- learning rate - n (how much does the value change every epoch)
			- W = W - n(dl/dw) 
			- b = b - n(dl/db)

![[Pasted image 20251117160840.png]]
#### Use case
- Image recognition (base of all models)
	- However, not used for image processing anymore
	- flattened input layer can be millions for vectors long
- Text generation (gpt)

### CNN
convolutional neural network 
- convolution - act of combining multiple function into one
- CNN uses a 2d input array, it uses a kernal to form a composite function 
uses a unflattened input - has semantic context 

#### Code
conv2(channels, filter, kernal_size, padding=false)
channel - how many colour channels
filter - how many feature function(filters)
padding - add padding to image on edge. Helps output fit dimensions of input

#### Process
Convolution -> ReLU + pool 
flatten
feed into DNN

stride - how many tiles kernal moves

Pooling 
- Max/Avg pooling - pick the highest/avg value in pool (x,y) 
	- x size of pool
	- y stride
	- max pool is prefered (supresses noise)
- down sampling - 
![[Pasted image 20251118033127.png]]

Dropout - prevent overfitting, temporary turn off neurons for learning
Batchnorm - normalisation to std = 0 mean = 1 
softmax (MLP) - activation for getting probability 
reLU(conv) - activation for range(0,1)