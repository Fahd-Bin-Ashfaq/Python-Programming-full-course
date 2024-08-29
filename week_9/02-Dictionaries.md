## Dictionary

Dictionaries are used to store data values in **key: value** pairs.

A dictionary is a collection that is ordered*, changeable, and does not allow duplicates. Dictionaries are written with curly brackets `{}`, and each key is associated with a specific value.

### Key Characteristics of Dictionaries

- **Ordered**: As of Python 3.7, dictionaries maintain the order of items based on the insertion order.
- **Changeable**: You can add, modify, and remove items in a dictionary after it has been created.
- **No Duplicates**: Dictionaries do not allow duplicate keys. If a duplicate key is entered, the last value associated with the key will overwrite the previous one.

### Basic Example of a Dictionary

```python
# Creating a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Accessing a value
print(thisdict["model"])  # Output: Mustang

# Adding a new key-value pair
thisdict["color"] = "red"
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# Modifying an existing value
thisdict["year"] = 2020
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'red'}

# Removing an item
thisdict.pop("model")
print(thisdict)  # Output: {'brand': 'Ford', 'year': 2020, 'color': 'red'}

# Checking if a key exists
if "brand" in thisdict:
    print("Yes, 'brand' is a key in the dictionary")  # Output: Yes, 'brand' is a key in the dictionary
```

### Dictionary Practice Questions

## Creating a Dictionary:
Create a dictionary named student with the following key-value pairs: "name": "Alice", "age": 22, "major": "Computer Science". Print the dictionary.

## Accessing Dictionary Values:
Given the dictionary car = {"brand": "Toyota", "model": "Corolla", "year": 2021}, write a code snippet to print the value associated with the key "model".

## Modifying Dictionary Values:
Modify the value of the key "year" in the dictionary car to 2022 and print the updated dictionary.

## Adding a New Key-Value Pair:
Add a new key-value pair "color": "blue" to the dictionary car and print the updated dictionary.

## Removing a Key-Value Pair:
Remove the key-value pair with the key "major" from the dictionary student and print the updated dictionary.