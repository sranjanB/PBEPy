print("The following program can handle :\n1. ZeroDivision Error\n2. ValueError\n")
dividend = input("Enter dividend: ")
divisor = input("Enter divisor: ")

try:
    quotient = int(dividend) / int(divisor)
    #print(f"quotient = {quotient}")
except ZeroDivisionError as e:
    print("Invalid Input, Your divisor is zero.")
    print(f"Error details: {e}")
except ValueError as e:
    print("Invalid Input.")
    print(f"Error details: {e}")
except Exception as e:
    print(f"Error details: {e}")
else:
    print(f"quotient = {quotient}")

print("This program completed Successfully.")