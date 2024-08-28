# Creating a set
unique_numbers = {1, 2, 3, 4, 5}

# Adding an item to the set
unique_numbers.add(6)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}

# Sets do not allow duplicate values
unique_numbers.add(3)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}
