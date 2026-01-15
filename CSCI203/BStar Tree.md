- [[Self balancing tree]] , [[M way tree]]
- Star refers to an improved version from [[B tree]]
- All values are stored at the Roots.

### Improvements 

|                     | B tree              | B* tree                                                       |
| ------------------- | ------------------- | ------------------------------------------------------------- |
| Node fill           | 1/2 Full at least   | 2/3 Full at least                                             |
| Node splitting      | Split upon overflow | Split when adjacent nodes are full (attempts to redistrubute) |
| Implementation      | Simple              | Complex                                                       |
| Storage utilisation | Good                | Great                                                         |
### Operations
#### Create(insert)
- Attempt to insert into node
- IF overflow:
	- Attempt to redistribute to immediate sibling 
- Else: 
	- Insert
![[bstar insert drawing|2000]]
#### Read
- Check if current value bigger than key in node
	- IF bigger:
		- LOOP until not bigger
	- IF not bigger:
		- move down to Keys Left child
	- IF last Key:
		- move down to Keys Right child
- LOOP until No Right child OR found
	 
![[Bstar tree read Drawing|500]]
#### Update
- This is just Read and Replace
#### Delete
- Read and Check:
	- IF node not 2/3 Full
		- Attempt to Redistribute from sibling nodes
	- IF node 2/3 Full:
		- Delete
![[b star tree delete Drawing]]
>[!NOTE]
>I fucked up the [0 - -] node just assume it is [0 -2   ]