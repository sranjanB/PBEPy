# accept integers only
print("This program accept intgers only, press q to quit.")

while True:
    try:
        a = input("Enter an integer: ")
        if a == 'q':
            break
        a = int(a)
    except Exception as e:
        print("Invalid integer")
    else:
        print(f"value = {a}")
