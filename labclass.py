#/print hello world?
print("hello world!")

#calculate the sum of two numbers?
def sum_of_two_numbers(a, b):
    return a + b
print(sum_of_two_numbers(5, 3))
 
#find the square of a number
def square_of_number(n):
    return n ** 2
print(square_of_number(4))()

accept the user name and greet them with it
name = input("enter your name:")
print(f"hello, {name}!")

#check whether a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(check_even_odd(7))

#6
def unique_elements(lst):
    return list(set(lst))

print(unique_elements([1, 2, 3, 3, 4, 5, 5]))

#7
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(25))

#8
import math

def area_of_circle(radius):
   return math.pi * (radius ** 2)

print(area_of_circle(5))
#9
def reverse_string(s):
  return s[::-1]

print(reverse_string("hello"))
#10

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
#11
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
#12
def largest_item(lst):
   return max(lst)

print(largest_item([1, 3, 2, 8, 5]))
#13
def is_in_range(num, start, end):
    return start <= num <= end

print(is_in_range(5, 1, 10))
#14
def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower

print(count_case("Hello World"))


