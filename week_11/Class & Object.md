### Class and Object in Simple Words

- **Class  ** & ** Object**: 
A class is just like a blueprint group of attributes and methods,

Attributes represented by variables that represent data
Methods perform an action or task similar like function


#### Example

Imagine a class called `Car`:

```python
class Car:
    name="hello World" #atribute
    age=22             #atribute

    def show(self):     #method
        print(self.name,seld.age)


#creating an object of class
obj=Car()
obj.show()
print(obj.name)
print(car.age)
```
The code defines a class named `Car` with two attributes, `name` set to `"hello World"` and `age` set to `22`, and a method `show` that prints these attributes. To use this class, an object `obj` is created from it using `obj = Car()`. This object now has access to all the attributes and methods defined in the class. When `obj.show()` is called, it prints the `name` and `age` of the `obj`, outputting `"hello World 22"`. Additionally, the attributes of the object can be accessed directly using `print(obj.name)` and `print(obj.age)`, which will print `"hello World"` and `22`, respectively. Note that there’s a typo in the original code snippet where `print(car.age)` should be `print(obj.age)` to correctly reference the created object.


