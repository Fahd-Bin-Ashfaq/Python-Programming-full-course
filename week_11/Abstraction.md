### Abstraction 

Abstraction is the concept of hiding complex implementation details and showing only the necessary system features. We use abstract classes to define what must be done, not how.

For example, you don’t need to understand the internal circuits and software when you use a smartphone. You use the phone's interface to make calls, send messages, or browse the internet. The internal details are hidden, allowing you to focus on the phone’s features.

### Two Ways of Abstraction

1. **Abstract Class**  
   - An abstract class is a class you **cannot use directly** to create objects.  
   - It is made to be used by other classes (called child classes).
   - It can have **abstract methods** — these are like empty functions with no code inside.
   - The child class must **write the real code** for those methods.

   **🧠 Python Example:**

   ```python
   from abc import ABC, abstractmethod

   # Abstract class
   class Vehicle(ABC):
       @abstractmethod
       def start(self):
           pass
       
       @abstractmethod
       def stop(self):
           pass

   # Child class
   class Car(Vehicle):
       def start(self):
           print("Car is starting")

       def stop(self):
           print("Car is stopping")

   my_car = Car()
   my_car.start()  # Output: Car is starting
   my_car.stop()   # Output: Car is stopping
opping
     ```

2. **Abstract Method**:
   - An abstract method is a method that is defined in an abstract class without implementation details. Subclasses that inherit from the abstract class provide the implementation of abstract method.
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

