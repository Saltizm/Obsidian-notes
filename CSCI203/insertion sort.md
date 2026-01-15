instruction:
1. iterate through the unsorted array beginning from the second element
2. each element is shifted to the left until it is in order. 
3. repeat 1 to 2 until (<length of array) the array is sorted

Best case: omega(n)
Worst case: O(n^2)
Average case: theta(n^2)

```
procedure insertion sort(arr[0...n]):
	for i = 1 to n:
		if arr[i] < arr[i-1]:
			j = i - 1
			while arr[i] < arr[j] and j >= 0:
				j = j - 1
			t = arr[i]
			arr[i] = arr[j]
			arr[j] = t
```