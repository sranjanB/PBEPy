from random import randint, shuffle

print("Welcome to the MCQ Test. 5 mark for correct and -1 for mistake.")
print('='*50)
mark = 0
x = randint(0, 10)
y = randint(0, 10)
z = randint(0, 10)
n = randint(1, 10)

print(f"Q1. What is the value of the expression: {x}*{y}-{z}")

answer = x*y-z

quiz = [answer + randint(1, 10), answer, answer + randint(1, 10), 'None']
shuffle(quiz)
label = ['a', 'b', 'c', 'd']

guess = dict()
for item in range(len(label)):
	key = label[item]
	value = quiz[item]
	guess[key] = value

for key, value in guess.items():
	print(f"({key}) {value}")

user_answer = input("Answer: ")

try:
	if answer == guess[user_answer]:
		print("Correct")
		mark += 5
	else:
		print(f"Incorrect\nCorrect answer is {answer}.")
		mark += -1
except:
	print("Invalid")

print(f"Q2. What is the value of the expression: {x}+({y}*{z})/{n}")

answer = x+(y*z)/n

quiz = [answer + randint(1, 10), answer, answer + randint(1, 10), 'None']
shuffle(quiz)
label = ['a', 'b', 'c', 'd']

guess = dict()
for item in range(len(label)):
	key = label[item]
	value = quiz[item]
	guess[key] = value

for key, value in guess.items():
	print(f"({key}) {value}")

user_answer = input("Answer: ")

try:
	if answer == guess[user_answer]:
		print("Correct")
		mark += 5
	else:
		print(f"Incorrect\nCorrect answer is {answer}.")
		mark += -1
except:
	print("Invalid")

print("Q3. The set data type can hold duplicate values. The statement is:")
print("(a)False\n(b)True\n(c)Partially Correct\n(d)None")
user_answer = input("Answer: ")

try:
	if user_answer == 'a':
		print("Correct")
		mark += 5
	else:
		print("Incorrect\nCorrect answer is False.")
		mark += -1
except:
	print("Invalid")


print(f"Your Final Mark is {mark}")
print("Thank You for your Time.")
