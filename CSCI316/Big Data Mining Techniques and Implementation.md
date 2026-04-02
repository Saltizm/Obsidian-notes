Big Data refers to **Large** and **Complex** datasets. Cannot be stored or processed effectively in a single machine.

Factors for Big data (input):
- Velocity - Speed at which data is added/changed
- Volume - Amount of data stored
- Variety - Non structured data 
- Veracity - False/Inaccurate data
	- Data validity - Noisy and inaccurate data
	- Data volatility - Irrelevant data (Old data)
(output):
- Value - how relevant or useful is the results 
### Data mining
Refer to collections of meaningful outputs from Big data.
### Data collections

| Method            | Difficulty |                                                                                                                          |
| ----------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------ |
| Download          | Easy       |                                                                                                                          |
| API               | Medium     | API(application program interface), are developer provided services that allow formatted data collection through request |
| Scalping/Crawling | Difficult  | Manual collection of data through web-crawlers etc. Unformatted (highly varied) and random (veracious)                   |
### Data 

![[Pasted image 20260103165828.png]]
Attribute - column data
Object - Record, instance, sample (row)
Class - Attribute that is output
Feature - Attribute that is not output
#### Dimensions 
Number of attribute per Record.
Types
- Fixed (structured data)
- Variable (non structured data)
- Continuous (variable)
##### sparcity
Refer to number of unique records.
High sparcity = High variance 

Sparcity -> High dimensionality
Dimension - how large a row is 
### Pre processing
Things done before data processing (prep input)
Mining methods influenced by nature of data.
##### Domain understanding --
What does the data mean (semantics)
Important to define features 
Important to choose mining methods

Why?
- Problem definition to meet the client's needs
- Mining method selection
- Output interpretation 

#### Factors --
#### Imbalance
Refer to how skewed are the class/feature frequency
Measures:
- Discrete attributes : Frequency, mode
- Continuous attributes : Range, SD, Median, Mean
	- If median != mean :
		- median < mean : right skewed
		- median > mean : left skewed
##### Data quality
Outliers : sample far from the other samples
Missing values : uncollected data due to external restraints
Noise : inaccurate or irrelevant data 

#### Solution
Noise:
- Data polishing : Remove faulty *attribute value* and treat as Missing Value.
- Data filtering : Remove problematic samples

Missing values:
- Obtain from another source (Data Integration)
- Expert knowledge 
	- data from studies to fill in missing data
	- eg. prediction model for heart attacks (what is the EKG pattern that denotes risk)
- Estimate value (taking averages) LAST RESORT

##### Data integration
combining data from different sources
NFL analysis:
- new data can introduce more dirty data
##### Data Aggregation
combining samples(records) together into a single sample(record)
In practice:
- Fusing attributes that have partial dependency
NFL analysis:
- information loss. Context thought to be irrelevant might be important to output. 
#### Instance Selection
selecting a few samples over the whole
why?:
- reduce computational load
- reduce data noise 
- sample balancing 
how?:
- grid method
NFL analysis:
- can skew output due to LLM/expert biases
#### Instance generation
create samples to increase sample size
(stub)
#### Feature transformation
applying a function to attain data suitable for processing
Low (semetics) -> 0.1
functions:
- Format transformation
- Simple encoding and one-hot encoding
- Discretization/Binning 
- Normalization 
- Scaling 
- Filtering (remove noise)
#### Format transformation
Changing formats enough said.
sgd to ringit
american date to british date
current time to time elapsed 

#### Binning 
Separate into ranges (bins) and assign values 
#### Normalisation
Convert into common range
- Redistrubutes skewed data 
#### Filtering
Types:
- Instance filter
- Attribute filter
- Value filter
#### Data sampling
select a subset of data to represent population
Purpose - reduce chance of **Overfitting**
types:
- Simple random sampling
	- Downside: Might be biased. (sample not representative)
- Stratified sampling
- types:
	- Separate into partitions. Draw random samples from each partition
	- Classified first by measure before SRS.
#### Imbalanced data
Imbalance in samples. i.e. More of cats than dogs 
results in under/over sampling

---
### Data mining
data mining - obtain valuable output that reveals patterns and insights from big data
#### Algorithms 
-  K-nearest neighbors (KNN)
	- If it quacks like a duck it is a duck. 
	- labels records based on nearest neighbor (sample that is closest to it)
	- Pros : Easy implementation for small projects
	- Cons : Poor scalability
SciKit-Learn - ML library. fully implemented common models
DF/Data frame - 2d data structure
Pandas - Data struct library

#### Plots
> housing = strat_train_set.copy() > housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)

regular plot 
![[Pasted image 20260116150651.png]]
> corr_matrix = housing.corr() > corr_matrix["median_house_value"].sort_values(ascending=False)

heat map (4D plot)
![[Pasted image 20260116150722.png]]

#### Attribute correlation 

![[Pasted image 20260116235826.png]]
diagonal indicates xx and yy relations 
The rest are attribute correlations
#### Defining new attributes
Secondary attribute -> Primary attribute (operation)
i.e. rooms_per_household = rooms/household

Secondary attribute might have better attribute correlation
#### Sklearn encoding
take example 

| colour | saturation |
| ------ | ---------- |
| Blue   | 100        |
| Yellow | 1          |
| Red    | 50         |

##### One hot encoding
turns definite range into a matrix of 1 and 0 (boolean)

| saturation | Blue | Red | Yellow |
| ---------- | ---- | --- | ------ |
| 100        | 1    | 0   | 0      |
| 1          | 0    | 1   | 0      |
| 50         | 0    | 0   | 1      |
##### Ordinary encoding
turns indefinite range into category

| colour | saturation |
| ------ | ---------- |
| Blue   | 2 (high)   |
| Yellow | 0 (low)    |
| Red    | 1 (medium) |
##### Feature scaling
min max scaling - put into a range (0-1)
standardisation - subtract mean from every value to normalise

Why?
- learning models fare better with numbers with a small range as its easier on computation
##### Evaluation (deduction)
RSME, [[Decision tree]].
### Decision tree
![[Pasted image 20260123181436.png|500]]
**Splitting of data set** according to the decision ( value ) of the attribute.
The leaf (outcome) is the majority class's value. (need not be 100%)

>[!practice]-
>Practice starting with taxable income.
>![[Pasted image 20260123182545.png|500]]
>##### Personal observation
>Use ordinary encoding and categories the certain fields (>120k means not loyal).
>However this does not cover every sample.
>There is very little correlation with between the two fields 

Used for deduction: 
use test sample to go down the decision tree to check if the class value derived from the tree is the same as the test sample

#### Building a decision tree
Hunt's algorithm
- Let D^[t] be the data that is received by node _t_
- termination conditions:
	- If D^[t] is entirely contain one class value. create a Y^[t]
	- if D^[t] have no attributes left. create Y^[t].
	- if D^[t] empty. D^[t-1] -> Y^[t] 
- if theres is no more t. Take majority vote -> D^[t] -> Y^[t]
- otherwise:
	- split by y 
	- recursive call  "Y^[t] + D^[t+1] " split by "splitDataSet"
Splitting methods
- Multisplit - high dimensionality
- binary split - linear categorization, might not capture relationship
##### handling continuous value
Continuous attribute discretisation
- Static - binning with set 
- Dynamic - binning within pipeline, according to metrics such as
	- IQR
	- Clustering (k means)
Ranges (binary decisions)
- find the best split (backtrack)
- computationally expensive
#### Tree induction
**Greedy approach**
$$impurity \propto homogeneous^{-1}$$
impurity - how uncertain (evenly split) the labels are in a node
homogenous - majority class is large (x1 : 10, x2 : 0)

Entropy - measure of information uncertainty (range(0,1))
$$Shannon\ entropy\ model\ -\ H(X)=\sum_{x\in X}p(x)\ log_2(p(x)^-1) = E(surprise)$$
$$conditional\ entropy\ -\ {H(X|Y) = H(X,Y) - H(Y)}$$
**Multiway split (nonbinary)**
![[Pasted image 20260227232736.png]]
Hp(D) - the summation entropy of splitting 
InfoGain(P) - difference between initial H(D), Hp(D)

#### Pruning (overfitting countermeasure)
Pre-pruning - stop tree construction up to a certain threshold
- Information gain
- Split dataset size
Post-pruning - prune branches after seeing overfitting
- CART (cost complexity pruning)
	- identify the weakest link to prune 
		- Metrics:
			- Error rate
			- Depth from node
### Random forest (DT ensemble)
Ensemble - Using many models to create a new model

| Advantage                                                                                 | Disadvantage       |
| ----------------------------------------------------------------------------------------- | ------------------ |
| Increased accuracy - Crowd intelligence (one mistake is nullified if majority is correct) | Computational cost |
| handles high data volumes (multiple trees)                                                |                    |
| Parallelization                                                                           |                    |
##### Sampling
**sample sampling**
- Bagging - select and replace samples to create a subset randomly
**feature sampling**
- Forest-RI(random input) - randomly select features 
	- Feature reduction
- Forest-RC - from existing features, create linear combinations (addition and subtraction only) randomly
	- Feature instantiation 
---
### Probabilistic classification
- Traditional classifier - Provide crispy prediction
- Probabilistic classifier - Give a probability of a label 

| advantage                   | disadvantage                                                 |
| --------------------------- | ------------------------------------------------------------ |
| Comparable accuracy with DT | computationally intractable (non polynomial scaling runtime) |
|                             |                                                              |
#### Probability 
Random variables:
- Discrete RV
	- Boolean - Y/N
	- Discrete - Sunny/Rain
- Continuous RV
	- Discretization - binning into ranges
	- **Probability density function - Gaussian distribution** 
		- 
### Naive Bayes Classifer
Bayes theorem 
![[bayes theorem diagram]]
conditional independence assumption
![[Definitions#^ae4177]]
##### Issues
**Numerical underflow**
- With many attribute (many multiplication of <1 values) 
- Solution:
	- Use log transform
**Zero count**
- Some attribute have a value count of 0 when some label is given
- bayes calculation will have a 0 in the product (p(Y|**X**)=0)
- i.e. label (buy_computer=true) has attribute (name=tom smith) in test set
	- **Laplace smoothing**:
		- Add one(or a small value) to the denominator and numerator 
##### Continuous-value Features
$$- Mean\ \mu = \frac{1}{N} \sum_{i=1}^N x_i$$

$$- Variance\ \sigma^2 = \frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2 = \left( \frac{1}{N} \sum_{i=1}^N x_i^2 \right) - \mu^2$$
- ![[Pasted image 20260301181019.png]]
- Bayes theorem for continuous features (given)
- used in ranges as P(X=x|Y) is near 0. use a small range from r\<x\<r+e. where e is a small value

| Advantages                                   | Disadvantages                                                            |
| -------------------------------------------- | ------------------------------------------------------------------------ |
| • Easy to implement                          | • Assumption: class conditional independence, therefore loss of accuracy |
| • Good results obtained in most of the cases | • Practically, dependencies exist among variables                        |
|                                              | • E.g., Symptoms: fever, cough etc., Disease: lung cancer, diabetes etc. |
|                                              | • Dependencies among these cannot be modeled by Naïve Bayes Classifier   |

• **How to deal with these dependencies?**
• Bayesian Belief Network (DAG learnt from previous mod)
• From correlation to causality?

---
### Model evaluation
![[TF label diagram|10000]]
#### accuracy
Classifier accuracy(recognition rate) - TP+TN/(TP + FP + FN + TN) - T/(T+F)
Error rate - FP+FN/(TP + FP + FN + TN) - F/(T+F) - 1-Acc
#### class imbalance
Recognition rate:
- Sensitivity/recall(TP rec) - TP/(TP + FN) 
	- If classifier keep choosing P, sensitivity low
	- Class imbalance (high positive label)
- Specificity(TN rec) - TN/(TN + FP)
	- If classifier keep choosing N, specificity low
	- Class imbalance (high negative label)
- FP rec - 1-specificity 
	- Used in ROC (yaxis - FP rec/ xaxis - recall)
F measure:
- ![[Pasted image 20260301190301.png]]
- Precision - TP / TP + FP
- TPR (recall) - TP/ TP + FN
- Fb ( weight F measure )
	- ![[Pasted image 20260301191410.png]]
	- b = 2/0.5
Holdout method
- Data split into test and training
- hold out test. Use it to test
![[Ai foundations#Resampling methods]]

#### Metric 
- Accuracy : classifier accuracy 
- Speed - training time/test time
- Robustness - noise handling (preprocessing)
- Scalability - rdd?
- Interpretability - derive semantic meaning 

---
### Big data
MapReduce 
fragmentation of data to split work load over several spark workers.
Map - to project one data onto a different form
Reduce - aggregation function. Used to add from different workers

Relation - table
Column header - attributes
Rows - tuples (samples)

R\[A1, ... , An\] 
A - schema (Column)
R - table

#### Selection
Map - Selection: For each tuple t in R, test if it satisfies C. If so, Mapper produce key value pair (t,t). otherwise, produce nothing

Reduce - identity function (do nothing)

#### Natural join
Map - for each tuple (a, b) in R\[A, B\], 
produce the key value pair b: (R,a).

For each tuple (b, c) in R\[B, C\]. 
produce the key value pair b(S, c).

Reduce - Each key value pair, b will be **associated** with values in the form of (R,a) or (S,c). Construct all tuple (a,b,c), if both (R,c) and (S,c) appear in the list that b is **associated** with.

#### Matrix-Matrix multiplication
$$N = n_{jk},\quad M = M_{ji},\quad P = NM = \sum_{j} n_{jk} m_{ji} = p_{ki}$$
##### Stage 1
Map - For each matrix element mij, produce the key value pair j:(M, i, mij). 
Likewise, for each matrix element njk, produce the key value pari j:(N, k, njk).

Reduce - For each key j, examine it's list of associated values.
For each value that comes from M, 
and each value that comes from N,
produce a key value pair with key (i,k) and value equal to the product mijnjk.

##### Stage 2
Map - identity function 

Reduce - For each key (i, k),
produce the sum of the list of values associated with this key.
The result is a key value pair (i,k) : v, where v is the value of the element in row i and column k of the matrix P = MN.

Apache spark stores data in rdd distributed across multiple machines.
