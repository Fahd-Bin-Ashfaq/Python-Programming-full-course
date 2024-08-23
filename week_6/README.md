## Nested If/Else Conditions in Python

A nested `if/else` condition refers to an `if` or `else` statement inside another `if` or `else` block. This allows for more complex decision-making processes by adding additional conditions within existing ones.

### Example of Nested If/Else Conditions

Consider the following example to categorize a number:

```python
number = int(input("Enter a number: "))

if number >= 0:
    if number == 0:
        print("The number is zero.")
    elif number > 0 and number <= 10:
        print("The number is between 1 and 10.")
    elif number > 10 and number <= 100:
        print("The number is between 11 and 100.")
    else:
        print("The number is greater than 100.")
else:
    print("The number is negative.")
```
## Practice Questions for Nested If/Else

### 1. Grade Classification

Write a Python program that classifies a student's grade based on the score:

- If the score is 90 or above, print `"Excellent"`.
- If the score is between 80 and 89, print `"Good"`.
- If the score is between 70 and 79, print `"Fair"`.
- If the score is below 70, print `"Needs Improvement"`.

### 2. Age Group

Write a Python program to determine the age group based on the given age:

- If the age is less than 13, print `"Child"`.
- If the age is between 13 and 19, print `"Teenager"`.
- If the age is between 20 and 59, print `"Adult"`.
- If the age is 60 or above, print `"Senior"`.

### 3. Month Days

Write a Python program that determines the number of days in a month:

- Input the month as an integer (1 for January, 2 for February, etc.).
- Use nested `if/else` to check whether the month is January, February, or has 30 or 31 days.
- Output the number of days in the month.



## Nested Loops in Python

A nested loop is a loop that exists inside another loop. This technique is particularly useful for iterating over multi-dimensional structures such as matrices or grids. Each loop in the nested structure is referred to as an "inner loop" and an "outer loop."

### Concept

- **Outer Loop:** This loop contains one or more inner loops and controls the overall iteration, determining how many times the inner loops will be executed.
- **Inner Loop:** This loop is nested inside the outer loop and is executed for each iteration of the outer loop. It performs operations on each structure element as defined by the outer loop.

### Example of Nested Loops

Consider the following example to print values in a 2D grid:

```python
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i = {i}, j = {j}")
```

## Practice Questions for Nested Loops

### 1. Multiplication Table

Write a Python program to generate a multiplication table from 1 to 10. Use nested loops to print the table:

- The outer loop should iterate through numbers 1 to 10.
- The inner loop should iterate through numbers 1 to 10, and for each pair, print the product.

### 2. Number Pyramid

Write a Python program to create a number pyramid. For a given number `n`, print a pyramid with `n` levels:

- For `n = 4`, the output should be:


### 3. Pattern of Stars

Write a Python program to print a pattern of stars in the following format:

- For `n = 5`, the output should be:


### 4. Chessboard Pattern

Write a Python program to print a chessboard pattern of size `n x n`:

- For `n = 8`, the output should be:


### 5. Sum of Multiples

Write a Python program to calculate the sum of multiples of 3 and 5 up to a given number `n`:

- Use nested loops where the outer loop iterates through numbers up to `n` and the inner loop checks if a number is a multiple of 3 or 5. Sum these multiples.
