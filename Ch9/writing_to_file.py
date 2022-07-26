import os

# Opening a file in 'a' mode

my_file = open("TestData1.txt","a")
my_file.write("This is a new line.")
my_file.write("\nThis is another new line.I append this too.")
my_file.close()
