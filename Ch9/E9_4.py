from os import remove

try:
    test1 = open("TestData2.txt", "r")
    test2 = open("TestData1.txt", "a")
    remove("TestData2.txt")
    print("File removed succesfully")
except FileNotFoundError as e:
    print(e)
