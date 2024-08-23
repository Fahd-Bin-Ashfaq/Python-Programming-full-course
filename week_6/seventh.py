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



for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i = {i}, j = {j}")
