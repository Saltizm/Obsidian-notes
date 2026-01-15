Based on the sources, particularly the subject plan summaries and details regarding the final examination, you should focus your memorization efforts on the **core conceptual underpinnings, key definitions, algorithms, and fundamental mathematical principles** across all seven tutorial/lecture topics.

The final examination will test your **conceptual understanding** rather than purely rote memorization, and **no table with mathematical equations will be provided**. Therefore, you need to understand and internalize the logic and definitions behind the key formulas and algorithms.

Here is a comprehensive breakdown of what you need to memorize or review deeply for the subject:

--------------------------------------------------------------------------------

I. General Subject Structure and Assessment

1. **AI Paradigms:** Know the definitions and differences of the four main modeling paradigms covered in the subject: **Reflex-based, State-based, Variable-based, and Logic-based**.

2. **AI Framework:** Understand the **Modeling-Inference-Learning paradigm** used to navigate the solution space for AI tasks.

3. **Final Exam Requirements:** The exam is worth 50% of the total marks, and you must achieve at least 40% (20/50 marks) to be eligible for a Pass (otherwise a Technical Fail may be given). The exam includes 10 multiple-choice questions and 8 text questions.

II. Reflex-Based Models (Machine Learning & Deep Learning)

A. Linear Models (Regression and Classification)

1. **Three Design Decisions:** Memorize the three crucial steps in developing reflex-based models (linear regression/classification):

    ◦ Defining the **hypothesis class** (which predictors are possible).

    ◦ Defining the **loss function** (how good is a predictor/classifier).

    ◦ Defining the **optimization algorithm** (how to compute the best predictor).

2. **Loss Functions:** Know the specific loss functions and their limitations/motivations:

    ◦ Squared loss and Absolute deviation (for regression).

    ◦ The **limitation of Zero-one loss** and the motivation for using the **Hinge loss** (for classification).

3. **Optimization:** Understand the principle of **Stochastic Gradient Descent (SGD)** and its difference from traditional Gradient Descent (GD) (using only one example vs. all examples for updates).

B. Deep Learning (DNN & CNN) (Lab 1 Focus)

1. **DNN Fundamentals:** Understand the role of **feedforward neural networks (DNN)** (layered system where information flows forward) and the necessity of **computation graphs** and **backpropagation** for training/computing gradients.

2. **Input Handling:** Memorize the key difference in how input images are handled by the two models and why:

    ◦ **DNN** requires the input image to be **flattened to 1D** (loses spatial information, e.g., 28x28 becomes 784x1).

    ◦ **CNN** processes the **2D input directly**, preserving spatial information.

3. **CNN Components:**

    ◦ The mechanism of **Convolution** (filters/kernels scanning for patterns).

    ◦ The role of **Max-Pooling** (returns the maximum value, reduces computation, achieves translation invariance, and performs better than Average Pooling).

4. **Output Layer:** Know the purpose of the output layer (generates **logits**) and the appropriate conversion functions: **Sigmoid** (for binary classification) or **SoftMax** (for multiclass classification).

III. State-Based Models

A. Search Algorithms (Lecture 3)

1. **Algorithms Comparison:** Know the logic, principles, limitations, and suitable scenarios for the core search algorithms:

    ◦ **Tree Search:** Backtracking, DFS, BFS, DFS with Iterative Deepening (DFS-ID).

    ◦ **Dynamic Programming (DP):** Solves recursively, but only works for **acyclic graphs**.

2. _:_*

    ◦ **UCS** (known as Best Cost First search): Enumerates states in order of increasing **PastCost(s)**.

    ◦ **A* Search:** Explores in order of **PastCost(s) + h(s)**.

    ◦ The definitions of **Admissible** (h(s)≤FutureCost(s); optimistic) and **Consistent** heuristics.

    ◦ **Relaxation** is the technique used to derive good heuristics.

B. Markov Decision Process (MDP) and Reinforcement Learning (RL) (Lecture 4, Lab 3)

1. **MDP Fundamentals:** Understand how MDPs differ from search problems (MDPs handle **uncertainty** via probabilistic transitions T(s′∣s,a)). The solution to an MDP is a **policy** π.

2. **Key Definitions:** Understand and know how to apply these terms:

    ◦ **Value Function** Vπ​(s): Expected utility (cumulative discounted reward) received by following policy π from state s.

    ◦ **Q-Value** Qπ​(s,a): Expected utility starting at state s, taking action a, and then following policy π.

    ◦ **Policy Evaluation**: Computes Vπ​(s) for a fixed policy.

    ◦ **Value Iteration**: Computes the optimal value V∗(s) and derives the **optimal policy** π∗.

3. **Reinforcement Learning (RL) Algorithms:** RL is the online setting where **rewards and transition probabilities are unknown**.

    ◦ **Model-Based VI** (estimates T and R).

    ◦ **Model-Free Monte Carlo** (estimates Qπ​ based on total discounted reward, G, after each episode).

    ◦ **SARSA** (On-Policy; update uses Q(s′,a′) where a′ is chosen by the current policy).

    ◦ **Q-Learning** (Off-Policy; update uses maxa′​Q(s′,a′) (the maximal possible future value)).

4. **Exploration/Exploitation:** Know the **Epsilon-greedy** policy for balancing exploration (random actions) and exploitation (choosing the best-known action).

C. Game Theory (Lecture 5)

1. **Game Types and Algorithms (Tree Structure):** Know which algorithm applies to which game type:

    ◦ **Minimax:** Deterministic adversarial games (Max → Min → Max).

    ◦ **Expectimax:** Single agent with randomness (Max → Chance → Max).

    ◦ **Expectiminimax:** Adversarial games with randomness (Max → Chance → Min).

2. **Speed Up Strategies:**

    ◦ **Evaluation Functions:** Provide a domain-specific, approximate estimate of the game value Vminimax​(s) at a given depth.

    ◦ **Alpha-Beta Pruning:** Provides the exact minimax value faster by maintaining two bounds:

        ▪ **Alpha (**α**):** The maximum score that the maximizing player (MAX) can currently guarantee.

        ▪ **Beta (**β**):** The minimum score that the minimizing player (MIN) can currently guarantee.

        ▪ Pruning occurs when α≥β.

IV. Variable-Based Models (CSP & Bayesian Networks)

A. Constraint Satisfaction Problems (CSP) (Lecture 6, Lab 5)

1. **Factor Graph/CSP:** Know the definitions of **Factor Graph** (general model with factors/weights) and **CSP** (a factor graph where all factors are hard constraints). The objective is to find the **maximum weight assignment**.

2. **Backtracking Search Heuristics:** Know the role of each heuristic in search optimization:

    ◦ **Most Constrained Variable (MCV):** Choose the variable with the fewest remaining values in its domain (strategy: **fail early**).

    ◦ **Least Constraining Value (LCV):** Choose the value that rules out the fewest options for neighboring variables (strategy: **succeed more often**).

3. **Lookahead/Inference:**

    ◦ **Arc Consistency (AC-3):** Eliminates redundant values from domains by enforcing local consistency to reduce the search space.

4. **Graph Leverage Techniques:** Understand the purpose of **Conditioning** (fixing a variable's value to simplify the graph) and **Elimination** (solving a sub-problem conditioned on its Markov blanket).

B. Bayesian Networks (BN) (Lecture 7, Lab 6)

1. **BN Structure and Definition:** Know that a BN uses a **Directed Acyclic Graph (DAG)** and defines the **Joint Probability** as the product of **local conditional distributions** (Rule #1).

2. **Probabilistic Inference:** Be able to calculate conditional probabilities (e.g., P(Query∣Evidence)) using the joint distribution and the conditional probability rule (Rule #3: P(A∣B)=P(A,B)/P(B)).

3. **Explaining Away:** Know this key reasoning pattern: conditioning on an effect (like an alarm) can make independent causes (like a burglary and an earthquake) dependent, where confirming one cause reduces the probability of the other.

C. AI Logic (Propositional Logic) (Lecture 7)

1. **Logic Components:** Know the core ingredients: **Syntax** (valid formulas) and **Semantics** (models/truth values).

2. **Knowledge Base (KB):** The KB is a set of formulas that imposes constraints on the world.

3. **KB Relationships:** Know the definitions of three possible responses when adding a new statement (α) to KB:

    ◦ **Entailment** (KB⊨α): Already knew this information (no new constraint added).

    ◦ **Contradiction** (KB⊨¬α): Violates what is known.

    ◦ **Contingency**: Learned something non-trivial (updates the KB).

4. **Inference Rules:** Rules must be **Sound** (derived formulas must be true) and ideally **Complete** (all true formulas can be derived).

--------------------------------------------------------------------------------

In essence, memorize the **conceptual logic behind each algorithm** and the **key definitions** that differentiate one modeling approach (Reflex, State, Variable, Logic) from the others, especially since the exam emphasizes conceptual understanding and does not provide formulas.