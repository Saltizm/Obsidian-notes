Philosophical - sementic meaning from observation
Math - boolean programming ( traditional programming )
Neuroscience - MLP
Economics -  Game theory, Markov Decision Problem
Control theory - optimisation (forward pass backpropagation)
Psychology - Deep learning
Linguistic - LLM 

Expert systems - Knowledged based system 
Output solution from input through a series of rules 

##### Reason for current boom
- Algorithm - Transformers, self-supervision, RLHF(RL from human feedback<captcha), tool-use
- Compute - TPU GPU
- Data - Internet allows for widespread data collection
- Scaling laws - moores law (improvement double every 2 years)

np - non polynomial 
p - polynomial 

$$Syllogism\ -\ A\subset B ,A\rightarrow B$$
### Rational agent
- Rational - takes the optimal action
	- optimal can vary according to hyperparameters (maxmise performance)
	- Rationality check:
		- Account for all variables
- Agent - something that perceives and act
	- Act - A
	- Perceive - P/P* (ALL perceptions)
- $$f:P^{*}\rightarrow A$$
#### Elements of an agent
##### Rationality
Rationality - maximise expected performance
Omniscience - maximise actual performance

##### Task environments 
- The problem to which rational agents are the solutions.
**PEAS** : 
performance,(metrics)
environment,(factors)
actuators(provide input vector),
sensors(medium)

![[Pasted image 20260225162016.png|500]]

| Pro                     | Con                 |
| ----------------------- | ------------------- |
| Free humanity from work | Weapons             |
| increase Goods          | Surveillance        |
| Accelerate research     | Bias                |
|                         | Employment          |
|                         | Safety and security |
### Task environment properties
| this                                            | that                                                                          |                                                                          |
| ----------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Fully observable - all states are known         | Partially observable                                                          |                                                                          |
| Single-agent                                    | Multiagent - many agents that are interdependant                              |                                                                          |
| Deterministic - action -> definite outcome(p=1) | Non-deterministic - (stochastic)                                              |                                                                          |
| Episodic - events are independant               | Sequential                                                                    |                                                                          |
| Static                                          | Dynamic - Environment changes                                                 | Semi_dynamic - Agent knowledge changes as it takes action in environment |
| Discrete - finite states                        | Continuous                                                                    |                                                                          |
| Known                                           | unknown - cost and other rules are hidden. Action has to be taken to find out |                                                                          |
##### Agent program type (Learning agents)
- Simple reflex
	- do x when y
	- no memory
	- Usecase : Fully observable, Known
	- examples:
		- SVM 
- Model based
	- keep track with an internal state derived from perception
	- Models: Transition, Sensor
	- usecase : partial observable
	- example:
		- A* search
- Goal based
	- All action aims to reach goal (heuristic estimate usually)
- Utility based
	- has a utility function to evaluate performance (expected)
	-  usecase : conflicting goals(metrics), uncertain
	- example:
		- monte carlos 
- Learning based
	 - Learning elements
		 - make improvements to performance element
		 - update hyperparamenters
	- Critic
		- loss evaluator
	- Performance element
		- select external (optimal) actions
		- exploit
	- Problem generator
		- select external (random) actions
		- explore
		- aims to break out of local minima
	![[Pasted image 20260226000804.png|500]]
Validation set (unseen)- Used to test model mid train 
Test set (unseen) - Used to evaluate model performance
Train set - to train model.

bias - y intercept, derived from differentiation of input feature term
input feature - weight * feature vector

### Threshold perceptron
unit that outputs a label from an input.
through matrix dot product. -> outputs signed magnitude 

The reason why W adjustments must be small. -> large adjustment can lead to misclassification.
#### Steps
**This is a 3 perceptron example**

input ( x ):
x1 = 0.5 (how much i like the actors)
x2 = 0.1 (how good are the reviews)
x3 = 0.9 (how expensive are the tickets)

weights (w):
w1 = 2 (GOOD actors are important)
w2 = -0.5 (BAD reviews should be considered)
w3 = -2 (CHEAP tickets are important)

bias (b):
b = 1 (like watching movies)

z (weighted sum) = x . w + b = 0.5(2) + 1(-0.5) + 0.9(-2) + 1 = -0.3

PUT z into an activation function:
reLU - o(-0.3) = 0
sigmoid - o(-0.3) = 0.425
![[Pasted image 20260226204349.png]]
### Seperability
linearly separable - 2 labels can be separated using a single line. 
- convergence : the model will arrive at a weight that creates a decision boundary that perfectly separate both. (perfect separator)
non-linearly separable - cannot be separated by a straight line.
- convergence : the learning rate will decay -> 0. The model settles on best fit boundary. 
### Resampling methods

^1bb398

Cross validation
![[cross validation diagram]]
Yellow - Test
White - Train

purpose : test a model's performance through rigor without needing to train on the entire dataset.

types : 
- LOOCV - kfold where k = n. (n is the number of samples)
- Stratified - select appx the same distribution of samples of each class

bootstrapping
selecting subset of samples (with replacement) from population to estimate population/train.

#### Issue
##### Hill climbing problem
- How do you know you are in the global maxima when you converge?
![[hills diagram]]
##### Solution
Adam - adjust step size (learning rate) to jump out of local maxima
find the gradient between wider and wider ranges every epoch.
- Utilise momentum for lr updates (mentioned later)
![[hills diagram gradient]]
SGD/SGA - introduce noise by calculating batch gradient using a single batch sample. Is also done per layer rather than per epoch
![[stochastic gd diagram]]
Momentum
![[momentum gd diagram]]
##### Overfitting
**Bias Variance tradeoff**

Bias - Underfitting (bias refers to error in mathematical terms)
Variance - Overfitting ( low variance )

**bias**
- High intra-class variance 
- Low inter-class variance

---
### Computer vision
#### Cameras
##### Lenses
aperture (opening) = 1/depth of field
focal plane - sharpest image
reflection types - 
- Diffused 
- Specular
- Shadows
##### Basic image processing
INPUT ---> Sensor
	(raw data)
	Color interpolation - filling in missing values
	(RGB)
	Color correction
    (sRGB)
Gamma correction ---> OUTPUT
##### Key points
Interpolation
- Bayer color samples - colour filter array arranged in RGGB 
- Bilinear - take the weighted average between a 4x4 tile
Auto focus/exposure:
- adjust parameter (focal depth field, exposure time) to meet visibility
#### Image feature
Traditional feature detection
- Texture - GLCM
	- ![[Pasted image 20260302231433.png]]
	- Diagram for 0 degrees
	- b - matrix for adjacent pixels. (how many 1 beside a 0)
- edge - Robert filter, Sobel filter, Prewitt filter
- Optical flow - movement of pixel picture to picture

**Image segmentation**
input -> Boundary contours -> Segmentation into regions (fine/course)
Segmentation type:
- Region segmentation - each segment separated by region
- Semantic segmentation - segment into objects types
- Instance segmentation - segment into many same objects
##### Detecting object
invariant to:
- Perspective
- Scale
- Brightness
- Occlusion (hidden or not)
- Pose
**Faster RCNN**
- First network - set anchor, create candidate image boxes and calculate the 'objectness' of each
- Second network - feature stack(Region of interest) is routed here. The network uses classifiers to identify the parts 
#### Takeaway
Computer vision 
- Image creation
	- Difficult : **Invariant, Discriminative**
- Model creation 
	- 3d vision - Disparity -> stereopsis.
	- Purpose: 
		- give different viewpoints of object
		- CGI
- To describe actions
	- actions are bound to time frame 
	- (long : fixing snack), (short : open fridge)
- To detect objects
	- Faster RCNN (complex)
	- edge detection (simple) -> OCR recognition (writing)
- Pre processing
	- segmentation - (region, semantic, instance)
		- edge detections - (Robert filter, Sobel filter, Prewitt filter)
		- texture detection - (GLCM (Gray-Level Co-Occurrence Matrix))
### Deep learning models
Colour histogram - binning of rgb values.
#### DNN
- Many layers of n perceptions layers all fully connected with one and other
- input -> hidden layers -> output
	- Relu/leaky Relu (hidden layer)
	- Sigmoid (output)
- Depth - number of layers
- Width - size of layers
- ![[Pasted image 20260303184517.png]]
##### Gradient descent
- change in gradient
- consist of 
	- Forward pass - feed input into network 
	- Backpropagation 
		- Loss calculation 
			- cross entropy 
			- Mean squared error
		- reweigh
			- $$W\leftarrow W-\eta \frac{dL}{dW}$$
			- $$B\leftarrow B-\eta \frac{dL}{dB}\ \ \ \  \eta(eta)\ is\ learning\ rate$$
---
### NLP (natural language processing)
- Quantification - every, one
- Pragmatics - actual meaning
- Long distance dependencies - **who** did the agent give the gold **to**?
- Time and tense - time frame changes meaning
- Ambiguity - text lack inflection in speech to give extra context
- Lexical ambiguity - many meanings one word
#### Bag of words
create a bag for each category 
- take a sentence
- remove special characters and non words
- shuffle randomly

**forming sentences**
- randomly select words out of a bag with replacement
- until eol indicator (period)
##### Word classification
- Naive bayes classifier
- corpus - large word collection
- p(x) = bag of words / corpus

##### Issue
- CIA, conditional independence assumption. (given label)
- ambiguity from using the same word for different things
### n-gram model
- each n-gram assumed to be dependent on the n-gram previous.
- n - how many words (gram size) 
- ![[Pasted image 20260303203026.png]]
unigram independent model - bag of words 

Larger n-grams
- cons:
	- zero problem - low probability of 2 similar n-grams. result of posterior probability is close to zero.
	- overfitting - poor generalization 
- procs:
	- better context, can capture more complex ideas
##### Part of speech tagging
- grammatical tagging of words
- provides tags to follow a KB

#### Discriminative vs Generative
- discriminative 
	- study the boundary of classes. learns conditional probability (P(C|W))
	- Types:
		- Logistical regression
		- SVM
		- CNN
- generative 
	- study the structure of each class. learns join probability (P(C, W))
		- naive bayes algorithm 

Natural language tasks
- Speech recognition
- Text to speech 
- Voice changer
- Machine translation
- Information extraction/retrieval
### RNN
##### word embedding
- random params to initialise for training
- contains params for:
	- POS
	- word feature
RNN - designed to process time series data in order.
time series data - data points(sample) indexed in chronological order. 

hidden layers 
- RNN has recurrent perceptron, stores h (hidden value)
- each perceptron process each data point in sequence
- the weights are updated (h and w)
	- stored as h
	- passed on to the next perceptron
![[Pasted image 20260304003949.png]]
this is across one layer
![[Pasted image 20260304004234.png]]
Single output
![[Pasted image 20260304004246.png]]
aggregation or max
##### Bidirectional RNN
- processes output in BOTH directions. (forward in time, backward in time)
- uses two separate RNN 
- Output are aggregated or maxed

##### Issues
- Diminishing gradient - RNN requires more updates to weight. BPTT(back propagation through time) as there is one more axis (time). 
	- This is an issue as each perceptron has the same weight. SO BPTT will update the weight n time where n is the number of perceptron.
- Long training time - data points are inputted and calculated sequentially 
- Exploding gradient problem - same as diminishing gradient but when the weight is too large (large pos value > 1)
### LSTM
- gating units stop gradients from increasing too much (exploding) or decrease to zero (diminishing) by choosing to forget/keep hidden states.
### Attention
- create context based summary -> fixed dimensional representation
- cross attention - focuses on target
- Self attention - extend attention to the all words (not just target). generate a value for each
self attention understands context better between words. (river bank/money bank)

### Pretraining and Transfer Learning
#### GloVe model
- Used to generate word embeddings
- Hyperparameters : 
	- input
		- Word 1 count (i)
		- Word 2 count (j)
	- Window size W
- for size W, create a co-occurrence (how many of x where there is y in W) matrix. 
- $$E \cdot \hat{E} = log(P(X_{ij}/X_{i}))$$
- log - log of co occurrence probability 
- E - word vector - weight for target
- E hat - context vector - weight for context (within window)

**Masked language model**
- Hide a single word from a input (sentence) to use as test for model. 
![[Pasted image 20260304145231.png]]
### Preprocessing
Tokenization - breakdown sentence into words
Stop word removal - remove punctuation 
Stemming - remove affixes
Lemmatization - standardizing words to one default (better -> good)

---

### Search problems
Search space:
- State space graphs 
	- nodes connected by edges 
	- represent space 
- Search trees:
	- leaf and parents 
	- represent paths
	- params:
		- b - branch factor
		- s - depth of LCS
		- m - max depth
### Tree based search
- NON costed :
	- Depth first search : (example used post order search L R root)
		- Stats : 
			- time complexity : O($b^{m}$)
			- space complexity : O(bm) - only stores current path and immediate sibling 
		- Order : FILO
		- non complete - dependent on tree depth (infinite perhaps)
		- global optimal : no (left most solution)
	- Breadth first search : (example used pre order search root L R)
		- Stats :
			- time complexity : $O(b^{s})$
			- space complexity : $O(b^{s})$ - the nodes up until solution's depth
		- Order : FIFO
		- complete - solution is finite
		- global optimal : yes (if un costed)
	- IDF (iterative deepening)
		- DFS with depth limiting (1,2,3..., m)
		- breadth hybrid in practice imo
- COSTED:
	- UCS (not informed)
		- local improvement heuristics
		- expand cheapest path
		- stats : 
			- time complexity : $O(b^{C^{*} /\varepsilon}))$ (epsilon - action cost)
			- space complexity : $O(b^{C^{*} /\varepsilon}))$
			- C* - estimate of s
		- complete - assuming positive action cost and finite solution
		- global optimal : yes
	- A* search (informed)
		- admissible heuristic (estimate always under cost)
		- functions : 
			- g(n) - cost up until nth node in path
			- h*(n) - actual cost to goal
			- h(n) - heuristic estimate to goal
			- f(n) = g(n) + h(n)
		- admissibility - h(n) < h*(n) 
		- global optimal : no
---
### Knowledge base
- KB 
	- Facts - values assigned to attribute
		- brown = dog
		- ear = sharp
	- Rules - conditions derived from facts
		- conclusion
			- if (brown = dog)
			- and (ear = sharp)
			- then golden retriever;
		- new facts
			- if (brown = dog)
			- and (ear = sharp)
			- then new ear = tapered dog ear
	- Inference engine 
		- apply rules to facts to:
			- generate new facts
			- conclusion
![[Pasted image 20260304173250.png]]
syntactic domain - structural information
semantic domain - semantic information

#### Bayes net
- refer to tutorial
- All variables independent of non child
- 
#### Markov model 
- create matrix 
	- ![[Pasted image 20260304182952.png]]
	- matrix outlines all possible subsequent action taken