# Arithmetic Operators
a = 10
b = 5
print("Arithmetic Operators:")
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a ** b)  # Exponentiation
print("a // b =", a // b)  # Floor Division

# Assignment Operators
x = 10
x += 5  # x = x + 5
print("\nAssignment Operators:")
print("x += 5 -> x =", x)
x -= 3  # x = x - 3
print("x -= 3 -> x =", x)
x *= 2  # x = x * 2
print("x *= 2 -> x =", x)
x /= 4  # x = x / 4
print("x /= 4 -> x =", x)

# Comparison Operators
y = 20
z = 20
print("\nComparison Operators:")
print("y == z ->", y == z)  # Equal to
print("y != z ->", y != z)  # Not equal to
print("y > z ->", y > z)    # Greater than
print("y < z ->", y < z)    # Less than
print("y >= z ->", y >= z)  # Greater than or equal to
print("y <= z ->", y <= z)  # Less than or equal to

# Logical Operators
p = True
q = False
print("\nLogical Operators:")
print("p and q ->", p and q)  # Logical AND
print("p or q ->", p or q)   # Logical OR
print("not p ->", not p)     # Logical NOT

# Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("\nIdentity Operators:")
print("a is b ->", a is b)  # True because both refer to the same object
print("a is not c ->", a is not c)  # True because a and c refer to different objects

# Membership Operators
list1 = [1, 2, 3, 4, 5]
print("\nMembership Operators:")
print("3 in list1 ->", 3 in list1)  # True if 3 is in list1
print("6 not in list1 ->", 6 not in list1)  # True if 6 is not in list1

# Bitwise Operators
m = 10  # Binary: 1010
n = 4   # Binary: 0100
print("\nBitwise Operators:")
print("m & n =", m & n)  # Bitwise AND
print("m | n =", m | n)  # Bitwise OR
print("m ^ n =", m ^ n)  # Bitwise XOR
print("~m =", ~m)        # Bitwise NOT
print("m << 1 =", m << 1)  # Bitwise left shift
print("m >> 1 =", m >> 1)  # Bitwise right shift
