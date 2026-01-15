[[Event]] [[decomposition]] technique uses a narrative of a actor interacting with a [[system]] and using relevant events to determine the use cases of the [[system]].

<h4>Application</h4>
Take the use case of a supermarket.

The actor we will be following first will be the ***Customer***.

1. Customer walk into the store
2. They check the product
3. They choose the product 
4. Walk to the cashier 
5. Queue up 
6. They pay for the product and leave.

1-5 are what's considered **Irrelevant** events.
Because the event is not directly related to the supermarket [[system]]. 

6 is considered a **relevant** event.
As it is related to the system.

use [[CRUD]] to further [[decomposition|decompose]] the event into different use cases.

From this event we can get the use case:
1. make invoice ( create, update )
2. Process payment ( read, update )

![[customer decompostion.excalidraw]]



