---
index: true
course: "CSIT114"
chapter: "Systems analysis"
concept: "Use case diagram"
---

# Use case diagram

Use case diagram describe the high-level functions and scope of a [[system]]. 

Describes the relationship between the [[system]] and its actors.
![[usecase diagram.excalidraw|1000]]

#### Use case
Use case are an activity that the [[system]] perform usually in response to a user.
Use cases are [[Specify requirements|functional requirements]].

***technique***
[[User goal technique]]
[[Event decomposition technique]]

***formatting***
Each use case has to be in *Verb-Noun* or *Verb/Noun* form.
![[Exampleusecasebad.excalidraw]]

Each use case has to perform [[CRUD]].
#### Include
**non-exclusive and mandatory** use cases.
Whereby the base use case (browse app) "includes" additional features (search map, weather check etc.)

Commonly **shown**.

#### Extend
**conditional and optional** use cases.
Whereby the base use case (Login) has different options (username and password, create account etc.)

Commonly **hidden**.


Use case diagram can also be represented in textual in the form of [[use case description]].