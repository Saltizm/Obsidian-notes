---
index: true
course: "CSCI203"
chapter: "Sorting algorithms"
concept: "selection sort"
---

# selection sort

instruction:
1. Find the minimum/maximum value in the unsorted array
2. swap with value in first index position 
3. repeat until (<length of array) sorted

```
procedure select(arr[0...n]):
	for i = 0 to n - 1:
		minIndex = i
		minValue = arr[i]
		for j = i+1 to n:
			if minValue > arr[j]:
				minIndex = j
				minValue = arr[j]
		t = arr[i]
		arr[i] = minValue
		arr[minIndex] = t
```

![[Pasted image 20250212013640.png]]