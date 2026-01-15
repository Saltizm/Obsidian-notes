- All requirement in [[1NF]] must be met
- Has no [[Partial FD]] (All attributes must be solely dependent on 1 [[Super key]])
- This means:
	- R(A,B,C,D) cannot have $AB^+$ and have FD $C \rightarrow A$ 
	- Only $C \rightarrow AB$ and $D \rightarrow AB$ 

### Methods
#### Table decomposition 
Take R(A,B,C,D)
Assume FD:
$A \rightarrow C$
$B \rightarrow D$

The table should split into
R(**A**,D), R(**B**,C)
with A and B being **primary keys**
#### Primary key decomposition 
Take R(A,B,C,D)
Assume FD:
$A \rightarrow C,D,B$
$B \rightarrow D$

$AB^+$

The primary key should become
$A^+$ instead.

### Issues
| name  | password | email          |
| ----- | -------- | -------------- |
| shawn | shawnpw  | shawn@mail.com |
| anne  | ann333   | anne@mail.com  |

| orderid | company  | Product type |
| ------- | -------- | ------------ |
| 124     | sol      | Soap         |
| 125     | megamart | Soap         |
#### Update
- No issues
##### Deletion
- Information loss on deletion 
- deletion of product type soap will delete the company 
#### Insertion
- Redundant field during insertion
- A company can only be created if there is an order

