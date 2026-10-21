---
index: true
course: "CSCI316"
chapter: "Data science skills"
concept: "Code"
---

# Code

![[Pasted image 20260115223256.png]]
```py
from numpy import *
def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0] 
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet 
	sqDiffMat = diffMat ** 2 # square 
	sqDistances = sqDiffMat.sum(axis=1) 
	distances = sqDistances ** 0.5 # square root 
	sortedDistIndicies = distances.argsort() 
	classCount = {}
	for i in range(k): 
		voteIlabel = labels[sortedDistIndicies[i]] 
		classCount[voteIlabel] = \
		classCount.get(voteIlabel, 0) + 1 
	sortedClassCount = sorted(classCount.items(), 
		key=lambda x: x[1], 
		reverse=True) 
	return sortedClassCount[0][0]
```
sklearn fit - train according to parameters x, y
model.fit(x,y)

sklearn simpleimputer from sklearn.impute (data cleaning)
impute = SimpleImputer(strategy="median")
//create new table
//i.e. housing_num  = housing.drop("ocean_proximity", axis=1)
impute.fit(housing_num) //training
impute.transform(housing_num) //update data

sklearn pipeline - series of process to get desired output
num_pipeline = Pipeline(\[array\])

sklearn OneHotEncoder() object - data values into attributes. letter{a,b,c} -> a{1}, b{1}, c{1}

sklearn RSME
a = mean_squared_error(x, y)
b = np.sqrt(a)

![[Pasted image 20260123173434.png]]
![[Pasted image 20260228001241.png]]
![[Pasted image 20260228001252.png]]

#### Gini index
- chance random guessing a label according to class distribution a random sample  
$$\text{Gini} = 1 - \sum_{i=1}^{J} p_i^2$$
#### Variance
- distribution of sample
- used in preprocessing to check for sparsity
$$\sigma(D)=p(1-p)$$
prepruned
![[splitdecision diagram|1000]]