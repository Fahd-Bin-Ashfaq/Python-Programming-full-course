## Tuple

Tuples are used to store multiple items in a single variable.

Tuple is one of the four built-in data types in Python used to store collections of data. The other three are List, Set, and Dictionary, each with different qualities and usage.

### Ordered

When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

### Unchangeable

Tuples are unchangeable, meaning that we cannot change, add, or remove items after the tuple has been created.

### Allow Duplicates

A tuple is a collection that is ordered and unchangeable. Tuples can contain duplicate items.

Tuples are written with round brackets `()`.

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(type(thistyple))
```
## Modifying Tuples

Tuples in Python are immutable, which means you **cannot** directly add or remove items from them once they are created. However, there are some workarounds to modify tuples:

### Adding Items to a Tuple

To add an item to a tuple, you can convert the tuple to a list, add the item, and then convert it back to a tuple.

```python
thistuple = ("apple", "banana", "cherry")
temp_list = list(thistuple)  # Convert tuple to list
temp_list.append("orange")   # Add item to the list
thistuple = tuple(temp_list) # Convert list back to tuple
print(thistuple)  # Output: ('apple', 'banana', 'cherry', 'orange')
```

### Tuple Practice Questions

## Creating Tuples:
Create a tuple named fruits that contains the items "apple", "banana", and "cherry".

## Accessing Elements:
Given a tuple fruits = ("apple", "banana", "cherry"), access and print the second item in the tuple.

## Negative Indexing:
Using the tuple fruits = ("apple", "banana", "cherry"), print the last item using negative indexing.

## Tuple Length:
Create a tuple named colors with the values "red", "green", "blue", and "yellow". Write a program to find and print the length of the tuple.

## Tuple Slicing:
Given the tuple numbers = (10, 20, 30, 40, 50, 60), slice the tuple to get a new tuple with the elements 20, 30, and 40.

## Concatenating Tuples:
Create two tuples, tuple1 with values (1, 2, 3) and tuple2 with values (4, 5, 6). Concatenate these two tuples into a new tuple.

## Finding Elements:
Write a program to check if the element "python" exists in the tuple languages = ("java", "python", "c++", "ruby").

## Tuple Unpacking:
Given a tuple person = ("John", 25, "Engineer"), unpack the values into separate variables and print them.

## Immutable Nature:
Write a program to try to change the first item of the tuple animals = ("cat", "dog", "rabbit") to "bird". What happens?

## Nested Tuples:
Create a tuple named nested_tuple with values (1, (2, 3), 4). Access and print the value 3 from the nested tuple.

## Converting List to Tuple:
Convert the list weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] to a tuple and print it.

## Iterating Over a Tuple:
Write a program to iterate through the tuple prime_numbers = (2, 3, 5, 7, 11) and print each element.

## Tuple Methods:
Use the tuple method count() to find out how many times the value 4 appears in the tuple numbers = (1, 2, 3, 4, 4, 4, 5).

## Tuple Index:
Write a program to find the index of the value 100 in the tuple data = (10, 20, 30, 100, 50, 100).

## Deleting a Tuple:
Create a tuple months = ("January", "February", "March"). Delete this tuple and try printing it afterward. What happens?