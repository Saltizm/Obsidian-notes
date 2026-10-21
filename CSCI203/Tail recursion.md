---
index: true
course: "CSCI203"
chapter: "Recursion and divide-and-conquer"
concept: "Tail recursion"
---

# Tail recursion

A recursion is tail if each recursive case:
- Defines the function outright
- Calls itself "only" with parameters 


```
def funcT(x, memorisation):
	if base case:
		return 1
	else:
		return funcT(x, memorisation)
```
Functionally identical to a for/while loop for modern ides.


