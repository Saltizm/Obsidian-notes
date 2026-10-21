---
index: true
course: "CSIT114"
chapter: "Systems analysis"
concept: "User goal technique"
---

# User goal technique

User goal technique create use cases by asking the actors what their goals with the system and using the goals to create a general use case.

#### Application
lets assume the system is a ***supermarket***

I interview the **cashier**.
I ask the cashier what they use the supermarket system for.

They reply:
1. Scan groceries 
2. Create order bill
3. Ask customer for payment type
4. collect payment from customer

These are the goals of the **cashier** which can be converted into use cases.


```mermaid
flowchart LR
id1[collect payment from customer] --> id2[collect payment]

```

***combine*** duplicate or closely related goals.
```mermaid
flowchart LR
id1[Scan groceries, Create order bill] --> id2[Makes invoice]
```
```mermaid

flowchart LR
id1[Ask for payment type] --> id2[Cash]
id1 --> id3[Card]
```
![[Cashier user goals.excalidraw|500]]
