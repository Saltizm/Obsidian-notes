Heap is a hierarchical [[Binary Search Tree|tree]] data structure for an efficient priority queue ( order of operations ).
Max heap - Highest value is the root
Min heap - Lowest value is the root

Heap is built in an array (inplace).

#### Utility
[[Djikstra's Algorithm]] (in finding the shortest path)
[[Heapsort]] 
```python
def buildHeap(lista, n):
    for i in range(n//2 - 1, -1, -1):
        heapify(lista, n, i)

def heapify(lista, n, i):
    largest = i  
    left = (2 * i) + 1    
    right = (2 * i) + 2 

    if left < n and lista[largest] < lista[left]:
        largest = left

    if right < n and lista[largest] < lista[right]:
        largest = right

    if largest != i:
        lista[i], lista[largest] = lista[largest], lista[i] 
        heapify(lista, n, largest) 

def heapSort(lista):
    n = len(lista)
    buildHeap(lista, n)
    
    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

```
##### Pseudocode
![[Pasted image 20250220015830.png]]