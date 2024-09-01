### Constructor 

A constructor is a special method in a class that is automatically called when an object is created. It is used to initialize the object's attributes with specific values when the object is created.

#### Example Program

Here's a simple example of a class with a constructor in Python:

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Initialize the name attribute
        self.age = age    # Initialize the age attribute

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object of the Person class
person1 = Person("Alice", 30)

# Using the object's method
person1.display()  # Output: Name: Alice, Age: 30
```
`__init__` is the constructor method. It takes `self` (which represents the object itself) and two other parameters, `name` and `age`. 

When `person1 = Person("Alice", 30)` is executed, the constructor initializes `person1`'s `name` and `age` attributes with `"Alice"` and `30`, respectively. 

`person1.display()` then prints the values of `name` and `age` for the `person1` object.
