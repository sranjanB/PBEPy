"""
Accept two number from user and print the average.
"""
num1 = float(input("Enter digit1: "))
num2 = float(input("Enter digit2: "))

total = (num1 + num2) / 2

print(f"The average of {num1} and {num2} is {total}.")

"""
output in one line.
"""
print("Hello \n Reader!")

"""
print in different quotation.
"""
print("The height of andrew is 6\'9\"")

"""
Guess it.
"""
x, y = 10, 2.5
print(x + y)    # 12.5
print(x / y)    # 5.5
print(x - y)    # 7.5
# print("x*y = :" + x * y)

"""
area of a circle, radius as input.
"""
rad = float(input("Enter the radius: "))
print(f"The area of the circle with radius {rad} is {(22/7)*rad*rad}")