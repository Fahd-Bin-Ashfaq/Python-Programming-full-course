## Nested Loops in Python

A nested loop refers to a loop that exists within another loop. It is commonly used to perform operations on multi-dimensional structures, such as matrices or grids.

### Example of a Nested Loop

Below is a basic example of a nested loop in Python:

```python
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i = {i}, j = {j}")
```
## Nested Loops in Python

A nested loop is a loop that exists inside another loop. This technique is particularly useful for iterating over multi-dimensional structures such as matrices or grids. Each loop in the nested structure is referred to as an "inner loop" and an "outer loop."

### Concept

- **Outer Loop:** This is the loop that contains one or more inner loops. It controls the overall iteration and determines how many times the inner loops will be executed.
- **Inner Loop:** This loop is nested inside the outer loop and is executed for each iteration of the outer loop. It performs operations on each element of the structure as defined by the outer loop.

### Example

Consider the following example of nested loops to print values in a 2D grid:

```python
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i = {i}, j = {j}")
```