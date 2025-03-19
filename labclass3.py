#a) Program to check if the number is even or odd:
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
    
#b) Program to print decimal equivalents of 1/2, 1/3, ..., 1/10
for i in range(2, 11):
    print(f"1/{i} = {1/i}")   
    
#c) Program to reverse a number
num = int(input("Enter a number: "))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(f"Reversed number: {reversed_num}")   

#d) Program to find the largest of 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

largest = max(num1, num2, num3)
print(f"The largest number is: {largest}") 

#e) Program to countdown from a number to zero
num = int(input("Enter a number to start countdown: "))

while num >= 0:
    print(num)
    num -= 1