import os

input_file = open("sample_640×426.png", "rb")
output_file = open("sample1.png", "wb+")

content = input_file.read(15)
while len(content):
    output_file.write(content)
    content = input_file.read(15)
input_file.close()
output_file.close()
