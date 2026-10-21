---
index: true
course: "JC Computing"
chapter: "Computing fundamentals"
concept: "Object Oriented Programming"
---

# Object Oriented Programming

**Anatomy of OOP**
Class: a blueprint that defines the attribute and method of an object
Object: an instance of a class, a real world entity that contains attributes and methods

example:
	- A car is similar to a class, and the many types of cars are the objects (truck, van, motobike). 
<br><br>
**Functions**
Encapsulation: *bundling attribute and methods together* and using methods to access or edit the attributes, a form of [[Abstract data type|abstraction]]

example:
-  Getter and Setter methods 

Advantages: Access to data is controlled by *public methods* created, providing
- data corruption (data that does not fit the parameters)
-Accidental changes

<br>
Inheritence: the act of a *subclass*/*child* inheriting the properties of a *superclass*/*parent*

example:
- A car or bicycle class inheriting the properties of the vehicle superclass

Advantages: *Code reuseability*, save on development time
Disadvantage: requires careful planning to *identify shared propeties *

<br>
Polymorphism/Overloading: reuse a method inherited from a superclass/parent with *different behaviour* under the *same name*

example:
- The attack method for a mage character object casting a spell instead of swinging a sword 

Advantages: *Code generalisation*, no need for redundant methods that perform similar actions