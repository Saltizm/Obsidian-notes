---
index: true
course: "CSIT 235"
chapter: "Database indexing"
concept: "Clustered index"
---

# Clustered index

- index ordered using [[BStar Tree]] directly using the keys ^aeaaf4
- values has to be unique $\therefore$  [[Primary key]], automatically creates an [[Primary index]]
- stored locally (in table)
- Cannot have more than one. 
	- (as it is stored in the table, there is only one way to arrange the table at one time)

| pros                             | cons              |
| -------------------------------- | ----------------- |
| Fast reading(ranges) and sorting | Slow insert speed |
|                                  | Slow update speed |
|                                  | Slow delete speed |
>[!Explanation]-
>The data is stored in the table itself, so all operation require the entire row to be modified
### Structure
- There are redundancy stored in the non-leaf nodes for identification 
- The leaf nodes are the literal data stored in the table
![[Pasted image 20250531231835.png|500]]
#### Use case 
- For range query and sorting