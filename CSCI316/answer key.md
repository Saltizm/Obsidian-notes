### CSCI316 Big Data Mining Techniques and Implementation
Final Examination Paper Session 3 2021 - Answers
Question 1 (7 marks)
#### (1.1) Word Frequency Counter (3.5 marks)
```python
import pandas as pd
def word_frequencies(X):
    frequencies = pd.Series(X).value_counts()
    return frequencies
```
# Alternative using collections.Counter
from collections import Counter
def word_frequencies_alt(X):
    return dict(Counter(X))
(1.2) Missing Value Replacement with Mean (3.5 marks)
```python
import pandas as pd
import numpy as np
def replace_missing_with_mean(Y):
    series = pd.Series(Y)
    mean_value = series.mean()
    series_filled = series.fillna(mean_value)
    
    return series_filled
```

##### Question 2 (9 marks)
(2.1) Why We Cannot Reuse Training Data for Testing (2 marks)
We cannot reuse training data for testing because:

**Overfitting**: The model would simply memorize the training data rather than learning general patterns

**Unrealistic performance**: Testing on training data gives overly optimistic accuracy that doesn't reflect real-world performance

**No generalization assessment**: We cannot evaluate how well the model performs on unseen data

**Information leakage**: The model has already seen the answers during training

##### (2.2) Feature Selection vs Feature Generation (3 marks)
**Feature Selection**: Process of selecting a subset of relevant features from the original set

**Use when**: Dataset has many irrelevant/redundant features; need to reduce dimensionality; want to improve model interpretability; avoid overfitting

**Feature Generation**: Creating new features from existing ones through transformations or combinations

**Use when**: Original features don't capture important relationships; domain knowledge suggests useful feature combinations; need to capture non-linear patterns

##### (2.3) Converting Strings to Numerical Values (4 marks)
**Why convert strings to numerical values?**

Machine learning algorithms require numerical input for mathematical operations

Distance calculations, gradient descent, and optimization require numbers

Most algorithms cannot process categorical data directly

One-hot encoding advantages example:

Consider a "Color" feature with values: Red, Green, Blue

**Direct conversion (assigning 1, 2, 3):**

Creates artificial ordinal relationship: Red < Green < Blue

Model might incorrectly learn: Blue is "greater than" Red

Distance between Red (1) and Blue (3) = 2, implying they're more different than Red and Green (1)

**One-hot encoding:**

Red = [1,0,0], Green = [0,1,0], Blue = [0,0,1]

Equal distance between all categories

No artificial ordering imposed

Model learns independent weights for each category

##### Question 3 (9 marks)
**(3.1) Information Gain Calculation (6 marks)**
Step 1: Calculate entropy of target variable (Buy?)

Buy?	Count
Yes	4
No	4
$Entropy(S) = -\frac{4}{8}\log_2(\frac{4}{8}) - \frac{4}{8}\log_2(\frac{4}{8}) = -0.5 \times (-1) - 0.5 \times (-1) = 0.5 + 0.5 = 1$

Step 2: Calculate entropy for Income attribute

Income = High:

Yes: 3, No: 0

$Entropy(High) = -\frac{3}{3}\log_2(1) - \frac{0}{3}\log_2(0) = 0 - 0 = 0$

Income = Medium:

Yes: 1, No: 2

$Entropy(Medium) = -\frac{1}{3}\log_2(\frac{1}{3}) - \frac{2}{3}\log_2(\frac{2}{3}) = -0.333 \times (-1.585) - 0.667 \times (-0.585) = 0.528 + 0.390 = 0.918$

Income = Low:

Yes: 0, No: 2

$Entropy(Low) = -\frac{0}{2}\log_2(0) - \frac{2}{2}\log_2(1) = 0 - 0 = 0$

Step 3: Calculate weighted entropy for Income

$Entropy(Income) = \frac{3}{8} \times 0 + \frac{3}{8} \times 0.918 + \frac{2}{8} \times 0 = 0 + 0.344 + 0 = 0.344$

Step 4: Information Gain for Income

$Gain(Income) = Entropy(S) - Entropy(Income) = 1 - 0.344 = 0.656$

Step 5: Calculate entropy for Age attribute

Age = Youth:

Yes: 1, No: 1

$Entropy(Youth) = -\frac{1}{2}\log_2(\frac{1}{2}) - \frac{1}{2}\log_2(\frac{1}{2}) = -0.5 \times (-1) - 0.5 \times (-1) = 0.5 + 0.5 = 1$

Age = Middle age:

Yes: 2, No: 1

$Entropy(Middle) = -\frac{2}{3}\log_2(\frac{2}{3}) - \frac{1}{3}\log_2(\frac{1}{3}) = -0.667 \times (-0.585) - 0.333 \times (-1.585) = 0.390 + 0.528 = 0.918$

Age = Senior:

Yes: 1, No: 2

$Entropy(Senior) = -\frac{1}{3}\log_2(\frac{1}{3}) - \frac{2}{3}\log_2(\frac{2}{3}) = 0.528 + 0.390 = 0.918$

Step 6: Calculate weighted entropy for Age

$Entropy(Age) = \frac{2}{8} \times 1 + \frac{3}{8} \times 0.918 + \frac{3}{8} \times 0.918 = 0.25 + 0.344 + 0.344 = 0.938$

Step 7: Information Gain for Age

$Gain(Age) = Entropy(S) - Entropy(Age) = 1 - 0.938 = 0.062$

Conclusion: Income (Gain=0.656) > Age (Gain=0.062), so Income should be the first split attribute.

##### (3.2) Why Ensemble Classifiers Enhance Performance (3 marks)
Ensemble classifiers (like Random Forest) enhance performance by:

**Reducing variance**: Combining multiple models reduces overfitting

**Reducing bias**: Different models capture different patterns

**Bagging (Bootstrap Aggregating)**: Training on different data subsets reduces correlation between errors

**Feature randomness**: Random feature selection at each split creates diverse trees

**Majority voting/Averaging**: Errors from individual classifiers cancel out

Handling non-linear relationships: Different trees capture different aspects of the data

##### Question 4 (9 marks)
(4.1) Numerical Underflow and Zero Count Issues (4 marks)
**Numerical Underflow**:

**Issue**: When multiplying many small probabilities, result becomes too small for computer precision (effectively zero)

**Solution**: Use log probabilities ($\log(P(A|B)) = \log(P(B|A)) + \log(P(A)) - \log(P(B))$) - converts multiplication to addition

**Zero Count Issue**:

**Issue:** If a feature value never appears in training for a class, probability becomes zero, making entire product zero

**Solution**: Laplace smoothing (add-one smoothing): $P(x_i|C_j) = \frac{count(x_i|C_j) + \alpha}{count(C_j) + \alpha \times |V|}$, where $\alpha$ is smoothing parameter (typically 1)

##### (4.2) F-score and Threshold Calculation (5 marks)
(a) F1 Score with threshold 0.59 (2.5 marks)

Threshold 0.59 means: Probability ≥ 0.59 → Positive class

Actual	Predicted	Count
P	P	3 (Tuples 1,2,3)
P	N	2 (Tuples 5,9)
N	P	1 (Tuple 4)
N	N	4 (Tuples 6,7,8,10)
$Precision = \frac{TP}{TP + FP} = \frac{3}{3 + 1} = \frac{3}{4} = 0.75$

$Recall = \frac{TP}{TP + FN} = \frac{3}{3 + 2} = \frac{3}{5} = 0.6$

$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall} = 2 \times \frac{0.75 \times 0.6}{0.75 + 0.6} = 2 \times \frac{0.45}{1.35} = 2 \times 0.333 = 0.667$

(b) Threshold for recall ≥ 80% (2.5 marks)

Recall = TP/(TP+FN). Total positives = 5.

For recall ≥ 80%: TP ≥ 4 (since 4/5 = 80%)

To get TP=4, we need to correctly classify 4 positives:

At threshold 0.55: Positives classified: Tuples 1,2,3,5 (4 positives) ✓

At threshold 0.56: Positives classified: Tuples 1,2,3,5 (4 positives) ✓

At threshold 0.57: Positives classified: Tuples 1,2,3,5 (4 positives) ✓

At threshold 0.58: Positives classified: Tuples 1,2,3,5 (4 positives) ✓

At threshold 0.59: Positives classified: Tuples 1,2,3 (3 positives) ✗

Therefore, highest threshold with recall ≥ 80% is 0.58.

##### Question 5 (9 marks)
(5.2) Apache Spark: Data-parallel vs Model-parallel (4 marks)
Why Spark is more suitable for data-parallel computation:

**RDD/DataFrame design**: Built for distributed data processing across partitions

**In-memory computing**: Optimized for operations on distributed datasets

**Fault tolerance**: Lineage tracking works well for data transformations

**Communication overhead**: Model-parallel requires frequent parameter synchronization

Example:

Data-parallel: Processing 1TB of clickstream data across 100 nodes - each node processes its partition independently, then aggregates results

Model-parallel: Training a neural network across nodes would require constant weight synchronization, creating network bottlenecks

##### (5.3) PySpark Code Implementation (5 marks)
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, desc, row_number
from pyspark.sql.window import Window

# Assume PATENT and CITATION dataframes are already defined

# (a) Find country with highest average number of claims per patent
country_avg_claims = PATENT.groupBy("COUNTRY") \
    .agg(avg("CLAIM_NUMBER").alias("avg_claims"))

max_avg_claims = country_avg_claims.agg({"avg_claims": "max"}).collect()[0][0]

result_a = country_avg_claims.filter(col("avg_claims") == max_avg_claims)

print("Country with highest average claims:")
result_a.show()

# (b) Find patent name(s) with highest citation count
# Calculate citation count for each patent
citation_count = CITATION.groupBy("CITED") \
    .agg(count("*").alias("citation_count"))

# Join with PATENT to get patent names
patent_citations = citation_count.join(
    PATENT, 
    citation_count.CITED == PATENT.PATENT_ID, 
    "inner"
).select("PATENT_NAME", "citation_count")

# Find maximum citation count
max_citations = patent_citations.agg({"citation_count": "max"}).collect()[0][0]

# Get patents with maximum citations
result_b = patent_citations.filter(col("citation_count") == max_citations)

print("Patent name(s) with highest citation count:")
result_b.show()
```
##### Question 6 (7 marks)
(6.1) Why Classical Perceptron is Not Preferable (2 marks)
Classical Perceptron limitations:

**Linear separability only**: Can only solve linearly separable problems (cannot solve XOR)

**Single layer limitation**: No hidden layers means limited representational power

**Binary output**: Only produces 0/1 outputs, no probability estimates

**No backpropagation**: Cannot learn complex patterns or hierarchies

**Sensitive to scaling**: Requires careful feature scaling

##### (6.2) Feedforward Neural Network with Keras (5 marks)
```python
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from scikeras.wrappers import KerasRegressor

# Assume X (features) and y (target) are already loaded
# X has 4 features, y is numerical target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Function to create model with hyperparameter
def create_model(hidden_neurons=10):
    model = keras.Sequential([
        layers.Input(shape=(4,)),  # Input layer (4 features)
        layers.Dense(hidden_neurons, activation='sigmoid', 
                    name='hidden_layer'),  # Hidden layer
        layers.Dense(1, activation='linear', name='output_layer')  # Output layer
    ])
    
    model.compile(
        optimizer='adam',
        loss='mse',  # Mean squared error for regression
        metrics=['mae']  # Mean absolute error as additional metric
    )
    
    return model

# Wrap model for scikit-learn compatibility
model = KerasRegressor(
    model=create_model,
    hidden_neurons=10,
    epochs=100,
    batch_size=32,
    verbose=0
)

# Define hyperparameter grid
param_grid = {
    'hidden_neurons': [5, 10, 20, 50],
    'batch_size': [16, 32, 64],
    'epochs': [50, 100]
}

# Perform grid search
grid = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,  # 5-fold cross-validation
    scoring='neg_mean_squared_error'
)

# Train with hyperparameter tuning
grid_result = grid.fit(X_train_scaled, y_train)

# Print best parameters
print(f"Best parameters: {grid_result.best_params_}")
print(f"Best CV score: {-grid_result.best_score_:.4f} MSE")

# Evaluate on test set
test_score = grid_result.score(X_test_scaled, y_test)
print(f"Test set R² score: {test_score:.4f}")

# Alternative: Direct training without grid search
def train_single_model(X_train, y_train, X_test, y_test, hidden_neurons=20):
    model = keras.Sequential([
        layers.Input(shape=(4,)),
        layers.Dense(hidden_neurons, activation='sigmoid'),
        layers.Dense(1, activation='linear')
    ])
    
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    
    history = model.fit(
        X_train, y_train,
        validation_split=0.2,
        epochs=100,
        batch_size=32,
        verbose=0
    )
    
    test_loss, test_mae = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test MSE: {test_loss:.4f}, Test MAE: {test_mae:.4f}")
    
    return model, history
```