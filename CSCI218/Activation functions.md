### Probability based
- Softmax -
	- range : (0,1)
	- interdependent - outputs sum to 1. 
	- usecase:
		- multiclass classification
- Sigmoid -
	- range : (0,1)
	- independent - output doesn't sum to 1
	- usecase:
		- binary classification 
note : causes vanishing gradient in CNN. probabilities are < 1. products of output will approach 0 during GD.
### Linear
- Relu/leaky Relu
	- range : max(0, x)
	- "leaky" : allow some negative values 
		- Reasoning : stop neurons from dying excessively 
		- negative values -> w - (-w')
### Non linear
- Tanh 
	- range : (-1, 1)
	- shaped like sigmoid
	- use case:
		- RNN (recurrent neural network)