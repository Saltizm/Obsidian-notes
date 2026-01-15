- 1NF refer to atomicity.
- Only one data can be in each column 

It will face issues with UDI(Update, Delete, Insertion)
### Issue
Assume table 

| name  | orderid | password | email          | company  | Product type |
| ----- | ------- | -------- | -------------- | -------- | ------------ |
| shawn | 123     | shawnpw  | shawn@mail.com | sol      | Soap         |
| shawn | 124     | shawnpw  | shawn@mail.com | sol      | Soap         |
| anne  | 125     | ann333   | anne@mail.com  | megamart | Soap         |
#### Update
- redundancy from repeating entries 
- if Shawn were to change his username. There will be 2 entries that require updates
#### Delete
- information loss upon deleting order 
- if Anne removed order with orderid=125. There will be no record of Anne's password, email and name in the system
#### Insertion
- constrained by redundant fields during insertion
- to add a company to the DB, the system will **Need** a order entry