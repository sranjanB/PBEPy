import os

file_object = open('TestData.txt', 'r')
print('__Approach:1__')
print('Reading each line one by one.')

first_line = file_object.readline()
second_line = file_object.readline()
third_line = file_object.readline()

print(first_line, end='')
print(second_line, end='')
print(third_line, end='')

file_object.close()

file_object = open("TestData.txt", "r")
print("__Approach:2__")
print("Reading each line using for loop")

for current_line in file_object:
    print(current_line, end ="")
file_object.close()

file_object = open("TestData.txt", "r")
print("__Approach:3__")
print("Using the read metod.")
file_content = file_object.read()
print(file_content)
file_object.close()
