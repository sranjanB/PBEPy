# Basic Calculator
print(50*"=")
print("This is a simple Calculator.\nIt supports the following operations:\n"
      "i.\tAddition\nii.\tSubstraction\niii.\tMultiplication\nvi.\tDivision.")
print(50*"=")

a = float(input("Enter the first number: "))
b = float(input("Enter the next number: "))

operatorDict = {'+':a+b, "-": a-b, "*": a*b, "/":a/b}

def formatNumber(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num

print("Enter an operator(+,-,*,/):")
try:
    operatorSelect = input()
    answer = operatorDict[operatorSelect]
    print(f"The final result is {formatNumber(answer)}.")
except:
    print("Invalid Operator.Can't compute the result.")
