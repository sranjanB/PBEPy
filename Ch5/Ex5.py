
# while True:
# 	data = input("Please Enter valid positive numbers only !\n")
# 	if data == 'quit':
# 		break
# 	else:
# 		if data.isdigit():
# 			num = int(data)
# 			if num < 0:
# 				print("Not a positive Number.")
# 			else:
# 				continue
# 		else:
# 			print("not a number at all.")

list = [1, 2, 5, 0.6, 3.6]

for elements in range(len(list)):
	print(list[elements])

for element in range(2, 5):
	print(list[element])

for i in range(20, 9, -5):
	print(i)