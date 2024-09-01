### Inheritance 

Inheritance allows a class to inherit attributes and methods from another class. This helps in reusing code and creating a hierarchy of classes, making it easier to manage and extend code.

#### Example

Here's a simple example of inheritance in Python:

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some generic animal sound")

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        print("Woof!")

# Creating an object of the Dog class
my_dog = Dog("Buddy")

# Using methods from both the parent and child classes
print(my_dog.name)  # Output: Buddy
my_dog.speak()     # Output: Woof!
```
In this example:

- **`Animal`** is the parent class with an attribute `name` and a method `speak`.
- **`Dog`** is a child class that inherits from `Animal`. It overrides the `speak` method to provide a specific sound for dogs.
- When `my_dog = Dog("Buddy")` is created, it inherits the `name` attribute from `Animal` and uses its own `speak` method to print `"Woof!"`.
