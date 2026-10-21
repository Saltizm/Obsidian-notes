---
index: true
course: "CSCI203"
chapter: "Data structures"
concept: "B tree"
---

# B tree

- [[Self balancing tree]], [[M way tree]]
- Common implementation is the 2-4 tree

### Operations
#### Create(insert)
- Attempt to insert into node
- IF overflow:
	- Split and insert middle node (rounded down) into parent
	- LOOP until no overflow
- Else:  
	- Insert

#### Read
- Check if current value bigger than key in node
	- IF bigger:
		- LOOP until not bigger
	- IF not bigger:
		- move down to Keys Left child
	- IF last Key:
		- move down to Keys Right child
- LOOP until No Right child OR found
	 

#### Update
- This is just Read and Replace
#### Delete
- Read and Check node:
	- IF node not 1/2 Full
		- Append Parent key
		- Move to Parent key
		- LOOP until node 1/2 Full Or at Root node
		- Read and Delete
	- IF node 1/2 Full:
		- Delete