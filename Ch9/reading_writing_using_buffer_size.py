import os

input_file = open("TestData.txt", "r")
output_file = open("TestData1.txt", "r+")

content = input_file.read(15)
while len(content):
    output_file.write(content + "\n")
    content = input_file.read(15)
input_file.close()
output_file.close()
