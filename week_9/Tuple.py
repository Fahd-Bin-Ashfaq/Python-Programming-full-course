tuple1 = ("apple", "banana", "cherry")
print(tuple1)
print(type(tuple1))
print(len(tuple1))


tuple1 = ("apple", "banana", "cherry")
temp_list = list(tuple1)  # Convert tuple to list
temp_list.append("orange")   # Add item to the list
thistuple = tuple(temp_list) # Convert list back to tuple
print(thistuple)  # Output: ('apple', 'banana', 'cherry', 'orange')