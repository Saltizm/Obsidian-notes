---
index: true
course: "CSCI203"
chapter: "Recursion and divide-and-conquer"
concept: "Divide and conquer"
---

# Divide and conquer

Divide and conquer algorithms is a method used in computer science to solve big problems by breaking them down (*divide*) into smaller parts, and solving and combining (*conquer*) them into the final output.

## Similarity to Recursion algorithms
although structurally similar to [[Recursion|recursive algorithms]], DnC algorithms have a better average [[runtime complexity]]. 
![[Pasted image 20250109164200.png]]
### log n
on average all partitions are split 1/3 or 2/3 ways due to the randomly chosen pivot.
this follows the logarithmic progression.

### n
during the *conquer* part, the algorithm has to run through the entire array *n* once to combine all of the partitions.