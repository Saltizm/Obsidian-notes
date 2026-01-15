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
#### Methods --
1. K-nearest neighbors (KNN)
	- Pros : Easy implementation for small projects
	- Cons : Poor scalability
(ADD later)
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
