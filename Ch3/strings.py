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
