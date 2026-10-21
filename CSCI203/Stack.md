---
index: true
course: "CSCI203"
chapter: "Data structures"
concept: "Stack"
---

# Stack

Holds data of a single type
Variable size
First in Last out order(FILO)

### Behaviour
operators:
- push(val) - add an element to the stack
- pop() - remove and return the most recently added element
- isEmpty() - (boolean). if empty return True 
- isFull() - (boolean). if full return True.
- peek() - return most recent element without removing it.
#### Implementation
when item **pushed** then increment variable **top**
when item is **popped** then decrement **top**

```
class Stack {
private int maxSize;
private double[] stackArray;
private int top;
// Constructor
Stack (int s) {
maxSize = s;
stackArray = new double[maxSize];
top = -1;
} // End constructor
```

### Use case
used for checking syntax for parenthesis, brackets and braces.

stack used in ram to manage addresses and arguments 

1. argument and return addressed are **pushed** into the stack.
2. when a method returns the return address the argument are **popped**


