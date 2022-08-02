# Using 'with' keyword in this example
# Python closes the when it is no longer needed
import os

with open("TestData.txt", "r") as file_object:
    print("A-1")
    print("Reading each line 1 by one")
    first_line = file_object.readline()
    second_line = file_object.readline()
    third_line = file_object.readline()
    print(f"first_line: {first_line}", end='')
    print(f"second_line: {second_line}", end='')
    print(f"third_line: {third_line}", end='')

with open("TestData.txt", 'r') as file_object:
    print('A-2')
    print("reading as loop")
    for current_line in file_object:
        print(current_line, end="")

with open("TestData.txt", "r") as file_object:
    print("A-3")
    print("reading using.read()")
    file_content = file_object.read()
    print(file_content)
