# To copy an image file
import os

try:
    with open("TestImage.png", "rb") as input_file:
        with open("TestImage1.png", "wb+") as output_file:
            for content in input_file:
                output_file.write(content)

except FileNotFoundError as e:
    print(f"Error: {e}")
