### Arguments

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (`fname`). When the function is called, we pass along a first name, which is used inside the function to print the full name:

```python
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")   # Output: Emil Refsnes
my_function("Tobias") # Output: Tobias Refsnes
my_function("Linus")  # Output: Linus Refsnes
```
Arguments are often shortened to args in Python documentation.

### Parameters or Arguments?

The terms parameter and argument can be used for the same thing: information that is passed into a function.
