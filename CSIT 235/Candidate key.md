- A candidate key is a [[Minimal key]] that is further decomposed to fit the [[Relational schema]]
- [[Minimal key]] + (context) = Candidate key
- A [[Minimal key]] can fail to be [[Super key|Unique]] and [[Minimal key|Minimal]] after context has been applied.
- A selected Candidate key is called the [[Primary key]]
- A rejected Candidate key is called the [[Alternate key]]


### Example
Take the *Warehouse* table as example
it has attribute:
- Address
- ID
- Name
- Supervisor_
- Date of construction

A minimal key can be assumed.
$Address^+$ or $\{ID, Addres\}^+$

However, with the context that *There are many warehouses in the same address*
The first minimal key fails *Uniqueness*

and 

with the context that *the ID is unique to every warehouse* 
The second minimal key fails *Minimality*
