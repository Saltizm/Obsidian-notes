---
index: true
course: "CSCI218"
chapter: "Artificial intelligence foundations"
concept: "CSCI218 Spring2022 Answers"
---

# CSCI218 Spring2022 Answers

## CSCI218 – Foundations of Artificial Intelligence
## Spring 2022 – Examination Answers

---

## Question 1. Basic Concepts of AI (12 marks)

## 1. The Official Birth of AI (1 mark)

The official birth of AI is regarded as the **Dartmouth Conference of 1956**, organised by John McCarthy, Marvin Minsky, Nathaniel Rochester, and Claude Shannon. At this conference, the term "Artificial Intelligence" was formally coined and the field was established as an independent discipline. It brought together researchers who collectively proposed that every aspect of learning and intelligence could in principle be described precisely enough for a machine to simulate it.

---

## 2. Meaning of "Rational" in Rational Agent (2 marks)

In AI, "rational" does not mean human-like or emotionally intelligent. A rational agent is one that **selects actions that maximise its expected performance** given the information available from its percepts and knowledge base.

Rationality is defined with respect to four factors:
- The **performance measure** that defines success
- The agent's **prior knowledge** of the environment
- The **actions** available to the agent
- The agent's **percept sequence** to date

A rational agent always chooses the action that is expected to maximise its performance measure given everything it currently knows.

---

## 3. Is Rationality Objective? (2 marks)

**No, I disagree with the student.**

Rationality in AI is **not purely objective** — it is defined relative to a performance measure, and that performance measure is specified by AI developers or end users. Different performance measures will lead to different definitions of what constitutes rational behaviour for the same agent in the same environment.

For example, a vacuum cleaner agent could be measured by:
- The amount of dirt cleaned (maximise cleaning)
- The amount of electricity used (minimise energy)

These two measures would lead to different rational behaviours. Therefore rationality **depends directly** on the performance measure defined by humans, making it a subjective design decision rather than a purely objective matter.

---

## 4. PEAS Description (4 marks)

### a. AI-Based Virtual Lecturer of CSCI218 (2 marks)

| Factor | Description |
|---|---|
| **Performance (P)** | Student comprehension scores, quiz results, student satisfaction ratings, question answering accuracy |
| **Environment (E)** | Online learning platform, student queries, course content, discussion forums |
| **Actuators (A)** | Text output, audio/video delivery, presenting slides, responding to student questions |
| **Sensors (S)** | Student text input, quiz responses, interaction logs, microphone/camera input |

### b. Mobile Robot for UOW Campus Tour (2 marks)

| Factor              | Description                                                                             |
| ------------------- | --------------------------------------------------------------------------------------- |
| **Performance (P)** | Tour completion rate, accuracy of navigation, student satisfaction, collision avoidance |
| **Environment (E)** | UOW campus grounds, indoor/outdoor paths, moving people, weather conditions             |
| **Actuators (A)**   | Wheels/motors for movement, speakers for narration, display screen for information      |
| **Sensors (S)**     | Cameras, GPS, laser scanner, sonar, bump sensors, infrared sensors, odometry            |

---

## 5. Four Basic Kinds of Agent Programs (3 marks)

### a. Names of the Four Basic Agent Programs (1 mark)

1. Simple Reflex Agent
2. Model-Based Reflex Agent
3. Goal-Based Agent
4. Utility-Based Agent

### b. Which Agents Work in Partially Observable Environments? (2 marks)

When the environment is only **partially observable**, the agent cannot perceive the full current state of the world from sensors alone. The agents that can handle this are:

**Model-Based Reflex Agent, Goal-Based Agent, and Utility-Based Agent** — all three maintain an **internal state model** that tracks the parts of the world that cannot be directly observed.

The **Simple Reflex Agent** cannot handle partial observability because it acts purely on the current percept with no internal memory — it has no way to reason about what it cannot see.

The internal model allows the agent to maintain a best estimate of the current world state even when sensors provide incomplete information.

---

## Question 2. Machine Learning and Neural Networks (14 marks)

## 1. Degree of Fit vs Complexity (3 marks)

### a. Degree of Fit (1 mark)

The degree of fit refers to **how well the model's predictions match the training data**. A high degree of fit means the model closely reproduces the outputs seen during training. It is measured by the training error — the lower the training error, the higher the degree of fit.

### b. Complexity (1 mark)

Complexity refers to **the expressiveness or capacity of the model** — how many parameters it has and how intricate the function it can represent. A more complex model (e.g. a deep neural network with many layers) can represent more elaborate patterns than a simple model (e.g. linear regression).

### c. Purpose of the Tradeoff (1 mark)

The purpose is to achieve **generalisation** — the ability to perform well on unseen data. A model with too high a degree of fit and too much complexity will overfit (memorise noise in training data). A model with too little complexity will underfit (fail to capture true patterns). Trading off these two factors finds the sweet spot where the model learns true underlying patterns without memorising noise.

---

## 2. Gradient Ascent in Neural Network Training (3 marks)

### a. Purpose of Gradient Ascent (1 mark)

Gradient ascent is used to **maximise an objective function** — specifically the likelihood or reward function — by iteratively updating model parameters in the direction of the steepest increase (the gradient). In neural network training, this is equivalent to moving weights in the direction that most increases the model's performance on training data.

Note: When minimising a loss function (e.g. cross-entropy), the equivalent operation is **gradient descent** — the same principle applied in the opposite direction. The terms are often used interchangeably depending on whether the objective is framed as maximisation or minimisation.

### b. Maintaining Efficiency with Large Training Sets (2 marks)

When the number of training samples increases significantly, computing the gradient over the full dataset becomes computationally expensive. The solution is to switch to **Stochastic Gradient Ascent (SGA)** or **Mini-Batch Gradient Ascent**:

- **Stochastic Gradient Ascent**: Update parameters after every single training sample. Very fast per update but noisy.
- **Mini-Batch Gradient Ascent**: Update parameters after a small random subset (batch) of samples (e.g. 32 or 64 samples). Balances computational efficiency with gradient stability.

This maintains efficiency because each update only requires computing the gradient over a small subset rather than the entire dataset, while still converging toward the optimal parameters.

---

## 3. MLP Layer Sizes (3 marks)

Given:
- N = number of training samples
- D = dimensions of feature vector
- C = total number of classes

| Layer | Size Determinable? | Justification |
|---|---|---|
| **Input layer** | **Yes — size = D** | Each input neuron corresponds to one dimension of the feature vector |
| **Hidden layer(s)** | **No** | The number of hidden layers and neurons per layer is a hyperparameter chosen by the designer — it cannot be determined from N, D, or C alone |
| **Output layer** | **Yes — size = C** | Each output neuron corresponds to one class in the classification task |

N (number of training samples) does not determine any layer size — it only affects training but not the architecture.

---

## 4. Total Neurons and Weights in MLP (3 marks)

Given:
- Input layer: P inputs
- Output layer: Q neurons
- K hidden layers with N₁, N₂, ..., Nₖ neurons respectively

### Total Number of Neurons

$$\text{Neurons} = P + N_1 + N_2 + \cdots + N_K + Q$$

$$= P + \sum_{i=1}^{K} N_i + Q$$

### Total Number of Weights

Weights exist between every pair of neighbouring fully-connected layers. Each weight connects one neuron in layer l to one neuron in layer l+1.

$$\text{Weights} = (P \times N_1) + (N_1 \times N_2) + \cdots + (N_{K-1} \times N_K) + (N_K \times Q)$$

$$= P \cdot N_1 + \sum_{i=1}^{K-1} N_i \cdot N_{i+1} + N_K \cdot Q$$

Note: If biases are included, add one bias weight per neuron in every layer except the input layer, giving an additional N₁ + N₂ + ... + Nₖ + Q bias weights.

---

## 5. Advantages of Deep Learning over Traditional ML (2 marks)

**Automatic Feature Extraction**: Traditional ML requires manual feature engineering — domain experts must design features before training. Deep learning automatically learns hierarchical feature representations directly from raw data (e.g. pixels, text, audio), removing the need for manual feature design.

**Scalability with Data**: Deep learning models continue to improve in performance as the volume of training data increases, whereas traditional ML models tend to plateau. This makes deep learning particularly powerful in data-rich domains such as computer vision, speech recognition, and NLP.

---

## Question 3. Computer Vision and NLP (10 marks)

## 1. Computer Vision (3 marks)

### a. Why Computer Vision is Important for AI (1 mark)

Computer vision enables AI systems to **perceive and interpret visual information from the world** — the most information-rich sensory channel available. Since a vast proportion of real-world data is visual (images, video, physical environments), AI agents cannot operate effectively in the real world without the ability to process visual input. It is fundamental to applications ranging from autonomous vehicles to medical diagnosis.

### b. Two Applications of Computer Vision (2 marks)

**Facial Recognition**: Computer vision systems analyse facial features extracted from images or video to identify or verify individuals. Used in security systems, mobile authentication, and law enforcement.

**Medical Image Analysis**: Computer vision models analyse X-rays, MRI scans, and CT images to detect anomalies such as tumours, fractures, or disease markers. This assists radiologists in diagnosis and enables earlier detection of conditions.

---

## 2. Bag-of-Words Model (2 marks)

**Key Assumption**: The bag-of-words model assumes that **word order does not matter** — a document is represented purely as a collection (bag) of its words, ignoring grammar, sequence, and context. Each document is represented as a vector of word frequencies or presence/absence indicators.

**Advantage**: The model is computationally simple and efficient. Representing documents as fixed-length frequency vectors makes them easy to process with standard classifiers (e.g. Naive Bayes, SVM). It works surprisingly well for many text classification tasks.

**Disadvantage**: By ignoring word order and context, the model loses important semantic and syntactic information. For example, "the cat chased the dog" and "the dog chased the cat" produce identical bag-of-words representations despite having opposite meanings.

---

## 3. Sentiment Classifier Design (5 marks)

### a. Language Model to Use (2 marks)

**Bag-of-Words model**, because the question explicitly states that the relationship between words should be ignored to keep the classifier simple. Bag-of-words is the natural language model for this requirement — it represents each sentence as a vector of word frequencies without any sequential or positional information.

### b. Data Preparation (1 mark)

Each submitted sentence needs to be:
1. **Labelled** as positive or negative (ground truth)
2. **Tokenised** — split into individual words
3. **Vectorised** — converted into a bag-of-words feature vector using a vocabulary built from all training sentences (e.g. using term frequency or TF-IDF weighting)
4. **Preprocessed** — lowercased, stop words removed, punctuation stripped

### c. Classifier to Use (1 mark)

**Naive Bayes Classifier** — it is the natural pairing with bag-of-words for sentiment classification. It models P(positive | words) and P(negative | words) using the conditional independence assumption between words, which aligns with the bag-of-words assumption of ignoring word relationships.

### d. Evaluating Classifier Performance (1 mark)

Split the labelled data into training and test sets and evaluate using:
- **Accuracy**: proportion of correctly classified opinions
- **Precision, Recall, and F1-score**: especially important if the positive/negative class distribution is imbalanced
- **Confusion matrix**: to inspect false positives and false negatives
- Optionally use **k-fold cross-validation** for a more robust performance estimate

---

## Question 4. Search, Knowledge and Logic (12 marks)

## 1. Search Tree and Issues (2 marks)

The state graph has nodes B, x, y, E with edges forming cycles (B→x, B→y, x→y, y→x, x→E, y→E).

**Search Tree:**

```
                B
              /   \
             x     y
           / \   / \
          y   E x   E
         / \   |
        x   E  y
       ...     ...
```

**Issue — Repeated States / Infinite Loops**: Because the state graph contains cycles (x↔y, B→x→y→x...), the search tree can expand infinitely by revisiting the same nodes repeatedly. The search algorithm must maintain a **visited/explored set** to detect and avoid repeated states, preventing infinite loops and redundant exploration.

---

## 2. Uninformed vs Informed Search (3 marks)

**How to distinguish**: An uninformed (blind) search algorithm has **no knowledge about the goal** beyond the problem definition — it does not use any estimate of how close a state is to the goal. An informed search algorithm uses a **heuristic function h(n)** that estimates the cost from the current node to the goal, guiding the search more efficiently.

**Uninformed Search — Breadth-First Search (BFS)**: Explores all nodes at the current depth level before moving to the next depth level. Uses a FIFO queue. Guaranteed to find the shallowest (shortest path) solution but can be memory intensive as it stores all frontier nodes.

**Informed Search — A* Search**: Uses the evaluation function f(n) = g(n) + h(n), where g(n) is the cost from the start to node n and h(n) is an admissible heuristic estimating the cost from n to the goal. A* expands the node with the lowest f(n) value and is both complete and optimal when the heuristic is admissible.

---

## 3. Admissibility of h3 = max(h1, h2) (2 marks)

**Yes, h3 is still admissible.**

A heuristic is admissible if it **never overestimates** the true cost to reach the goal — formally: h(n) ≤ h*(n) for all nodes n, where h*(n) is the true optimal cost.

Since h1 and h2 are both admissible:
$$h_1(n) \leq h^*(n) \quad \text{and} \quad h_2(n) \leq h^*(n)$$

Therefore:
$$h_3(n) = \max(h_1(n), h_2(n)) \leq h^*(n)$$

Since both h1(n) and h2(n) are individually bounded above by h*(n), their maximum also remains bounded by h*(n). So h3 never overestimates the true cost and is admissible. Furthermore h3 is a **better heuristic** than either h1 or h2 alone because it is more informed (closer to h*) while remaining admissible.

---

## 4. Agent Using Knowledge Base to Decide Action (2 marks)

The process is as follows:

1. **Perception**: The agent receives a percept from its sensors describing the current state of the environment.

2. **Knowledge Base Update (TELL)**: The agent uses the TELL operation to add the new percept information to its knowledge base, updating it with current observations.

3. **Inference**: The agent uses its inference engine to reason over the knowledge base — applying logical rules to derive new facts and evaluate possible actions.

4. **Action Selection (ASK)**: The agent uses the ASK operation to query the knowledge base: "What action should I perform now?" The knowledge base returns the best action based on its current knowledge and inferred conclusions.

5. **Execution**: The agent executes the selected action through its actuators, which affects the environment.

---

## 5. Logic (3 marks)

### a. Entailment (1 mark)

Entailment (⊨) means that one sentence **logically follows** from another in all possible models. Formally, α ⊨ β means that in every world where α is true, β is also true. It is a semantic concept — β is a necessary consequence of α regardless of any specific interpretation.

### b. α = A ∧ (¬B) ∧ C ∧ D and β = (¬B) — Entailment? (1 mark)

**Yes, α ⊨ β.**

α = A ∧ (¬B) ∧ C ∧ D requires that A is true, ¬B is true, C is true, and D is true simultaneously. In every model where α is true, ¬B must be true. Therefore β = (¬B) is true in every model where α is true. This means α entails β.

### c. α = A ∨ (¬B) ∧ C ∧ D — Entailment? (1 mark)

**No, α ⊭ β.**

With operator precedence, α = A ∨ ((¬B) ∧ C ∧ D). This sentence is true when A is true **regardless of whether ¬B is true**. For example, consider a model where A = true and B = true (so ¬B = false). In this model α is satisfied (because A is true) but β = (¬B) is false. Therefore α does not entail β.

---

## Question 5. Probabilistic Reasoning and Robotics (8 marks)

## 1. Alarm Bayes Network (5 marks)

### a. Concept of Bayes Network (2 marks)

A Bayesian network is a **directed acyclic graph (DAG)** where each node represents a random variable and each directed edge represents a conditional dependency between variables. Each node has an associated **conditional probability table (CPT)** that quantifies the probability of that variable given its parents in the graph.

In the alarm network example:
- **Burglary** and **Earthquake** are root nodes with prior probabilities P(B) and P(E) — they have no parents
- **Alarm** depends on both Burglary and Earthquake — its CPT specifies P(A | B, E)
- **JohnCalls** depends only on Alarm — P(J | A)
- **MaryCalls** depends only on Alarm — P(M | A)

The network encodes the assumption that JohnCalls and MaryCalls are **conditionally independent** given the Alarm state, and that Alarm is conditionally independent of all other variables given its direct causes.

### b. Joint Probability Distribution (1 mark)

Using the chain rule and the conditional independence structure of the network:

$$P(B, E, A, J, M) = P(B) \cdot P(E) \cdot P(A | B, E) \cdot P(J | A) \cdot P(M | A)$$

### c. P(Burglary = T | JohnCalls = T, MaryCalls = F) (2 marks)

Using Bayes' theorem:

$$P(B=T | J=T, M=F) = \frac{P(J=T, M=F | B=T) \cdot P(B=T)}{P(J=T, M=F)}$$

We need to sum over all values of E and A (hidden variables).

**Step 1 — Compute P(J=T, M=F, B=T)** by summing over E ∈ {T,F} and A ∈ {T,F}:

For each combination:

| E | A | P(E) | P(A\|B=T,E) | P(J=T\|A) | P(M=F\|A) | Product |
|---|---|---|---|---|---|---|
| T | T | 0.002 | 0.95 | 0.9 | 0.3 | 0.002×0.95×0.9×0.3 = 0.000513 |
| T | F | 0.002 | 0.05 | 0.05 | 0.99 | 0.002×0.05×0.05×0.99 = 0.00000495 |
| F | T | 0.998 | 0.94 | 0.9 | 0.3 | 0.998×0.94×0.9×0.3 = 0.253461 |
| F | F | 0.998 | 0.06 | 0.05 | 0.99 | 0.998×0.06×0.05×0.99 = 0.002970 |

$$P(J=T, M=F, B=T) = P(B=T) \times \sum = 0.001 \times (0.000513 + 0.00000495 + 0.253461 + 0.002970)$$

$$= 0.001 \times 0.256949 = 0.000256949$$

**Step 2 — Compute P(J=T, M=F, B=F)** similarly with P(B=F) = 0.999:

| E | A | P(E) | P(A\|B=F,E) | P(J=T\|A) | P(M=F\|A) | Product |
|---|---|---|---|---|---|---|
| T | T | 0.002 | 0.29 | 0.9 | 0.3 | 0.002×0.29×0.9×0.3 = 0.0001566 |
| T | F | 0.002 | 0.71 | 0.05 | 0.99 | 0.002×0.71×0.05×0.99 = 0.0000703 |
| F | T | 0.998 | 0.001 | 0.9 | 0.3 | 0.998×0.001×0.9×0.3 = 0.0002695 |
| F | F | 0.998 | 0.999 | 0.05 | 0.99 | 0.998×0.999×0.05×0.99 = 0.049351 |

$$P(J=T, M=F, B=F) = 0.999 \times (0.0001566 + 0.0000703 + 0.0002695 + 0.049351)$$

$$= 0.999 \times 0.049848 = 0.049798$$

**Step 3 — Normalise:**

$$P(B=T | J=T, M=F) = \frac{0.000256949}{0.000256949 + 0.049798} = \frac{0.000256949}{0.050055} \approx 0.00513$$

$$\boxed{P(\text{Burglary}=T | \text{JohnCalls}=T, \text{MaryCalls}=F) \approx 0.005 \text{ (0.5\%)} }$$

This makes intuitive sense — Mary not calling is strong evidence against an alarm, which greatly reduces the probability of burglary.

---

## 2. Mobile Robot Components (3 marks)

**Sensors / Stereo Vision**: Two cameras positioned to provide depth perception through stereoscopic imaging, enabling the robot to perceive its 3D environment and detect obstacles.

**Communications**: Wireless communication module allowing the robot to send and receive data — for example, transmitting its status to a control system or receiving navigation commands.

**Processing Power**: The onboard computer (CPU/GPU) that runs the robot's AI algorithms — processing sensor data, making navigation decisions, and controlling actuators in real time.

**Sonars**: Ultrasonic sensors that emit sound waves and measure the time for reflections to return, used for detecting obstacles and estimating distances at close range.

**Bump Sensors**: Physical contact sensors that detect when the robot has collided with an obstacle, triggering an emergency stop or avoidance behaviour.

**Infrared Sensors**: Detect nearby objects or measure distances using infrared light, useful for short-range obstacle detection especially in low-light conditions.

**Laser Scanner (LiDAR)**: Emits laser pulses and measures return times to create a precise 2D or 3D map of the surrounding environment, essential for accurate localisation and navigation.

**Odometry**: Uses wheel encoders to measure how far and in what direction the robot has moved, providing an estimate of position relative to a starting point.

**Motors**: Actuators that drive the robot's wheels, translating decisions from the processing unit into physical movement in the environment.

**Interaction**: Interface components (screen, speaker, microphone) enabling the robot to communicate with humans — displaying information, providing audio guidance, and receiving voice commands.

---

## Question 6. Safe and Responsible AI (4 marks)

## 1. AI Ethics (4 marks)

### a. Potential Negative Impacts of AI (2 marks)

**Job Displacement and Unemployment**: AI-driven automation is replacing human workers across industries including manufacturing, transportation, customer service, and data processing. This can lead to large-scale unemployment and economic inequality, particularly affecting lower-skilled workers who lack the resources to reskill.

**Algorithmic Bias and Discrimination**: AI systems trained on biased historical data can perpetuate and amplify discrimination. For example, facial recognition systems have been shown to perform significantly worse on darker-skinned individuals, and hiring algorithms have been found to discriminate against women. These systems can reinforce systemic inequality at scale.

**Privacy Violation and Mass Surveillance**: AI-powered surveillance systems — including facial recognition, behaviour analysis, and data mining — enable unprecedented monitoring of individuals without their knowledge or consent. This threatens civil liberties, freedom of expression, and the right to privacy.

### b. Measures to Ensure Safe and Beneficial AI (2 marks)

**Transparency and Explainability**: Design AI systems to be interpretable — developers should be able to explain how a model reaches its decisions. Using explainable AI (XAI) techniques ensures that users and stakeholders can audit, understand, and trust AI outputs.

**Fairness Testing and Bias Auditing**: Before deploying AI systems, rigorously test for bias across different demographic groups. Use balanced and representative training datasets, and apply fairness metrics to ensure the system does not discriminate against any group.

**Privacy-Preserving Design**: Apply data minimisation principles — only collect data necessary for the task. Use techniques such as differential privacy, federated learning, and data anonymisation to protect user privacy while still enabling effective AI systems.

---

*End of Answers*
