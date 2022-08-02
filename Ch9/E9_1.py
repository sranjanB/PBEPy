# To print content of a file
import os

file_info = "TestData.txt"
with open(file_info, "r") as file_object:
    for content in file_object:
        print(content, end="")
