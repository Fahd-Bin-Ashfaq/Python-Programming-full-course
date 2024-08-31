### Exception handling

Exception handling helps prevent our program from crashing when something goes wrong. Instead of stopping the entire program, we can use exception handling to catch errors, provide meaningful error messages, and decide what the program should do next. This makes our programs more reliable and user-friendly.
## Basic Components of Exception Handling

- **`try` Block**: The code that might cause an exception is placed inside a `try` block. If no exceptions occur, the code runs normally.

- **`except` Block**: If an exception occurs in the `try` block, the control is transferred to the `except` block. Here, you can define how to handle specific exceptions.

- **`else` Block**: The `else` block is optional and runs only if no exceptions were raised in the `try` block. It is often used for code that should execute only if the `try` block was successful.

- **`finally` Block**: The `finally` block is optional and always executes, regardless of whether an exception occurred or not. It is commonly used for cleanup actions, like closing files or releasing resources.

- **`raise` Statement**: You can use the `raise` statement to manually trigger an exception if a certain condition occurs.

## Example of Exception Handling

```python
try:
    # Code that might raise an exception
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    # Handles ValueError exceptions (e.g., if input is not an integer)
    print("Please enter a valid integer.")
except ZeroDivisionError:
    # Handles ZeroDivisionError exceptions (e.g., if the number is zero)
    print("Cannot divide by zero.")
else:
    # Executes if no exceptions were raised
    print(f"The result is {result}")
finally:
    # Always executes, regardless of exceptions
    print("Execution complete.")
```