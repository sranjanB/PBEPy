# A simple Calculator

def info():
    print("=" * 50)
    print("This is a simple calculator."
          "\nIt supports the following operations:"
          "\n(i)   Addition\n(ii)  Subtraction\n(iii) Multiplication"
          "\n(iv)  Division")
    print("=" * 50)


def verify():
    try:
        sample = float(input())
        return sample
    except IndexError:
        print('Could not be acceptable.')


def formatResult(result):
    if result % 1 == 0:
        return int(result)
    else:
        return result


def main():
    info()
    print("Enter the first number: ", end=" ")
    a = verify()
    print("Enter the next number: ", end=" ")
    b = verify()
    input3 = input("Enter an operator(+, -, *, /): ")

    if (input3 == '/' or input3 == '*') & (b >= 0):
        print('float division by zero will be invalid.')
        exit()

    cal = {"+": a + b, "-": a - b, "*": a * b, "/": a / b}

    if input3 not in cal:
        print("Operator is either invalid or not available.")
        exit()

    print(f"Output: {formatResult(cal[input3])}")


main()
