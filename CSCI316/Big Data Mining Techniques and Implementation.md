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
- If D^[t] is entirely contain one class value. create a Y^[t]
- if D^[t] empty. D^[t] -> Y^[t] 
- if theres is no more t. Take majority vote -> D^[t] -> Y^[t]
- otherwise:
	- split by y 
	- recursive call < Y^[t] + D^[t+1] 
	- 
Hunt's algorithm will only split according to another attribute when the original doesn't split it distinctively.