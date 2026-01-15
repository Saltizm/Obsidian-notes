Instructions:
1. **Stepping** through the unsorted list
2. comparing 2 items at a time and swapping if the wrong order
3. Repeat 1 to 2 as many time (<length of array + 1) until sorted

Best case Omega(n)
Worst case O(n^2)
Average case Theta(n^2)

```py
def bubblesort(arr):
	sorted = false
	while i<n and not sorted:
		i = i + 1
		sorted = true
		for j = 1 to n - i:
			if arr[j] > t[arr j+1]:
				t = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = t
				sorted = false
```
