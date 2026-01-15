`recursive algorithms are methods used in computer science to helps in solving complex problems by breaking them into smaller subproblems.

Recursive solutions work as a a basis for [[Dynamic Programming]] and [[Divide and Conquer]] algorithms.

### calculations
```
def f(n):
	if n == 0:
		return 1
	else:
		return n * f(n-1)
```
#### recurrence relations
![[recursion composite function|800]]
T(0):
a = 2
```
if n == 0: (1)
	return 1 (2)
```
T(n):
b = 3 + T(n-1)
```
else:(1)
return n(2) *(3) f(n-1)
```

### Types of recursion

![[Tail recursion]]
<br>![[Non tail recursion]]
### Growth rate
Recursion can either be [[runtime complexity|Linear or Non Linear]] depending on recursive calls per pass. 
This can be calculated using the [[CSCI203/Master theorem]]
