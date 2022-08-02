# Using try-except to handle file not found error

import os

try:
    my_file = "TestData.txt"
    with open(my_file, "r") as file_object:
        print("Using the read method")
        file_content = file_object.read()
except FileNotFoundError as e:
    print("The file you are looking for is not available.")
    print(f"Error: {e}")
else:
    print(f"content: {file_content}")
