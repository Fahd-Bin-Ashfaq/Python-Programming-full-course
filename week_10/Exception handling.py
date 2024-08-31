a = 10
b = 0

try:
    c = a / b  # This will cause a ZeroDivisionError
    print(c)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    
print("Future Coding")
