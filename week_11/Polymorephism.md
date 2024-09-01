### Polymorphism 

The word "polymorphism" means "many forms." In programming, polymorphism refers to the ability of methods, functions, or operators with the same name to operate on different types of objects or classes. It allows a single interface to be used for different underlying data types.

### Example of Polymorphism

Here's a simple Python example demonstrating polymorphism:

```python
class Animal:
    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Function that uses polymorphism
def make_animal_speak(animal):
    animal.speak()

# Using polymorphism
dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!
