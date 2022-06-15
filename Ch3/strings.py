text = "Hello, World !"
# Print in uppercase and lowercase
print(text.upper())
print(text.lower())
# Calculate length of a string
print(len(text))
# Print first occurrence of a character
print("The first occurrence of \"o\" is at index: ", text.index("o"))
# Replace world with Universe
print("Old Dev: ", text, "\nPro Dev: ", text.replace("World", "Universe"))
# Difference Between number and strings
my_string1 = "10"
my_string2 = "20"
my_int1 = 10
my_int2 = 20
print(my_string1 + my_string2)  # 1022
print(my_int1 + my_int2)  # 30
# Mixing will give you error
# print("string1 Value is same as " + my_int1) # Error as int can't be added with string
print("string1 Value is same as " + str(my_int1))
# Converting string to Number
print(int(my_string1, 10))  # Here 10 is base, Got converted easily as it is a number
# print(int("abc", 10)) # Here abc can't be converted with base 10
# Using isdigit to verify before conversion
print(my_string1.isdigit())  # True means can be converted to int
# Rounding a Number
print(round(2.7))  # 3
# Print max and min from a set
print(max(1, 2, 3, 4, 5))  # 5
print(min(1, 2, 3, 4, 5))  # 1
from math import *

# Getting a square root of a number
print(f"Square root of 25 is {sqrt(25)}")  # 5.0
# Ceiling and Floor value of a number
print(f"ceiling value of 39.3 is {ceil(39.3)}")  # 40
print(f"floor value of 39.3 is {floor(39.3)}")  # 39
# Find gcd( greatest common divisor) of two number.
print(f"The gcd of 4 and 14 is : {gcd(4, 14)}")  # 2
# Find factorial of a number
print(f"Factorial of 5 is :{factorial(5)}")

# Demo of input string
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print("Welcome", user_name, "! You are now", user_age)
print(f"Welcome {user_name} ! You are now {user_age}")
print("Welcome " + user_name + " ! You are now " + user_age)