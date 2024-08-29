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
    print("Yes, 'brand' is a key in the dictionary")