#a) Implement Python Script to generate first N natural numbers.
def generate_natural_numbers(n):
    numbers = list(range(1, n + 1))
    return numbers
n = int(input("Enter a number : "))
print("First", n, "natural numbers:", generate_natural_numbers(n))

#b) Implement Python Script to check given number is palindrome or not.
def is_palindrome(num):
    return str(num) == str(num)[::-1]
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

#c) Implement Python script to print factorial of a number.
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

#d) Implement Python Script to print sum of N natural numbers.
def sum_of_natural_numbers(n):
    return n * (n + 1) // 2
n = int(input("Enter a number N: "))
print(f"Sum of first {n} natural numbers is {sum_of_natural_numbers(n)}")

#e) Implement Python Script to check given number is Armstrong or not.
def is_armstrong(num):
    return num == sum(int(digit) ** len(str(num)) for digit in str(num))
num = int(input("Enter a number: "))
print(f"{num} is {'an Armstrong' if is_armstrong(num) else 'not an Armstrong'} number.")

#f) Implement Python Script to generate prime numbers series up to n
def prime_numbers_up_to_n(n):
    return [num for num in range(2, n + 1) if all(num % i for i in range(2, int(num ** 0.5) + 1))]
n = int(input("Enter a number N: "))
print(f"Prime numbers up to {n}:", prime_numbers_up_to_n(n))


