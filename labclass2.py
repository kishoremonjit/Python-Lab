#15. Write a Python function to multiply all 
def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result
numbers = [1, 2, 3, 4, 5]
print(multiply_list(numbers))  

#16. Check if a number is perfect
def is_perfect_number(number):
    if number < 1:
        return False
    divisors_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)
    return divisors_sum == number
number = 28
print(is_perfect_number(number))  

#17. Create a function that checks if a passed string is a palindrome or not.
def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]
string = "A man, a plan, a canal: Panama"
print(is_palindrome(string))

#18. Write a Python program to check if a passed string is a pangram or not.
import string

def is_pangram(sentence):
    alphabet_set = set(string.ascii_lowercase)
    sentence_set = set(char.lower() for char in sentence if char.isalpha())
    return alphabet_set <= sentence_set
sentence = "The quick brown fox jumps over the lazy dog"
print(is_pangram(sentence))  

#19. Calculate the sum of the digits of a number.
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
number = 12345
print(sum_of_digits(number))  

#20. Generate a list of four random numbers.
import random

def generate_random_numbers(count=4):
    return [random.randint(0, 100) for _ in range(count)]
print(generate_random_numbers())  
