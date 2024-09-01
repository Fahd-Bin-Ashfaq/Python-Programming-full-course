### Abstraction 

Abstraction is the concept of hiding complex implementation details and showing only the necessary features of an object. It simplifies interactions by focusing on what an object does rather than how it does it.

For example, when you use a smartphone, you don’t need to understand the internal circuits and software. You simply use the phone's interface to make calls, send messages, or browse the internet. The intricate details are hidden, allowing you to focus on the phone’s features.

### Two Ways of Abstraction

1. **Abstract Class**:
   - An abstract class is a class that cannot be instantiated on its own and is meant to be subclassed. It can include abstract methods (methods without implementation) that must be implemented by subclasses.
   - **Python Example**:

     ```python
     from abc import ABC, abstractmethod

     class Vehicle(ABC):
         @abstractmethod
         def start(self):
             pass
         
         @abstractmethod
         def stop(self):
             pass

     class Car(Vehicle):
         def start(self):
             print("Car is starting")

         def stop(self):
             print("Car is stopping")

     my_car = Car()
     my_car.start()  # Output: Car is starting
     my_car.stop()   # Output: Car is stopping
     ```

2. **Abstract Method**:
   - An abstract method is a method defined in an abstract class without an implementation. Subclasses that inherit from the abstract class must provide their own implementation of these methods.
   - **Python Example**:

     ```python
     from abc import ABC, abstractmethod

     class Shape(ABC):
         @abstractmethod
         def area(self):
             pass

     class Rectangle(Shape):
         def __init__(self, width, height):
             self.width = width
             self.height = height

         def area(self):
             return self.width * self.height

     my_rectangle = Rectangle(4, 5)
     print(my_rectangle.area())  # Output: 20
     ```

In these examples:
- The **abstract class** `Vehicle` defines methods `start` and `stop` without implementing them. The subclass `Car` must provide implementations for these methods.
- The **abstract method** `area` in the `Shape` class is implemented by the `Rectangle` subclass, which provides the specific logic for calculating the area of a rectangle.
