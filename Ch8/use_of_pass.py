print("this program print the sum of two integers.")
sum = 0

try:
    a = int(input("Enter first input: "))
    b = int(input("Enter second input: "))

except ValueError as e:
    pass
else:
    sum = a + b
    print(f"sum = {sum}")

print("This program completed Successfully.")