# OOP - Object Oriented Programming
- What are classes
- Why do we use classes

**The Four Pillars**
1. Encapsulation
    - Means wrapping up data and class methods into one unit -- a class.
    - Allows it to be safe from outside interference and misuse
    
2. Abstraction
    - Essentially showing only the necessary features of an object while hiding other irrelevant information.
    - Hides information and good for security
    - e.g. to drive a car you don't need to know HOW the car works

3. Inheritance
    - Enables new objects to take on the properties of existing objects
    - There single, multi-level, multiple and hierarchical inheritance to name.

4. Polymorphism
    - Literally "many forms". A subclass can define its own unique behaviour whilst simulataneously share the same functionalities as the parent class.
    - A subclass can have its own behaviour while sharing others with parent class.
    - It's the ability to redefine methods for derivde classes

**Classes**
- A class is the main factor used to implement these pillars
- It is the "blueprint" for the objects we use in python

```python
    class <name>:
        # The __init__ runs whenever the class is called
        __init__(self, <parameters>):
            self.<parameter1> = <parameter1>
```