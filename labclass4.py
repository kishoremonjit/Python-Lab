#a) Program that takes 2 numbers as command line arguments and prints their sum:
import sys
if len(sys.argv) != 3:
    print("Please provide two numbers as command line arguments.")
else:
    try:
        # Convert the arguments to numbers
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        # Calculate and print the sum
        print(f"The sum of {num1} and {num2} is: {num1 + num2}")
    except ValueError:
        print("Please provide valid numbers.")

    
#b) Implement a Python script to show the usage of various operators available in Python:
# Arithmetic operators
a = 10
b = 5

print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")

# Comparison operators
print(f"Is a equal to b? (a == b): {a == b}")
print(f"Is a not equal to b? (a != b): {a != b}")
print(f"Is a greater than b? (a > b): {a > b}")
print(f"Is a less than or equal to b? (a <= b): {a <= b}")

# Logical operators
x = True
y = False
print(f"Logical AND (x and y): {x and y}")
print(f"Logical OR (x or y): {x or y}")
print(f"Logical NOT (not x): {not x}")

# Assignment operator
x = 10
x += 5  # Same as x = x + 5
print(f"After assignment operator, x = {x}")

# Bitwise operators
print(f"Bitwise AND (a & b): {a & b}")
print(f"Bitwise OR (a | b): {a | b}")
print(f"Bitwise XOR (a ^ b): {a ^ b}")

# Membership operators
list1 = [1, 2, 3, 4]
print(f"Is 3 in list1? (3 in list1): {3 in list1}")
print(f"Is 5 not in list1? (5 not in list1): {5 not in list1}")

# Identity operators
print(f"Is a and b the same object? (a is b): {a is b}")

#c) Implement a Python script to read a person's age from the keyboard and display whether they are eligible for voting or not:
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#d) Implement a Python script to check if the given year is a leap year or not:
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
    