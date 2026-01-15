Used for finding the shortest path connecting all nodes to a specific node in a in a weighted  graph.

##### Instructions:
1. Initiate the candidate list, previous list, selected list and distance list
2. from the candidate list. Select a node with the smallest distance. Append the node into the selected list
3. update the distance and previous list if the total distance of the current node is lower. 
		distance is the total distance travelled from the first node to the selected node
		previous node is the node before it.
4. if not, continue 
5. repeat 2 to 3 until all nodes from candidate list has been exhausted.



>[!example]-
>Reference graph:
>![[Pasted image 20250228185519.png]]
>
>form a [[Adjacency matrix]].
>![[Pasted image 20250228185435.png]]
>V = the current vertices 
>C = candidate list
>S = selected list
>P = Previous list
>D = distance list
>
>![[dijkstra's algorithm example|5000]]
