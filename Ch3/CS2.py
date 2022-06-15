"""
Math problem statement.
"""
from random import randint

while True:
    game = input("Would you like to play a game[y/n]: ")
    try:
        if game == "n":
            break
        elif game == "y":
            v1 = randint(0 ,100)
            v2 = randint(0 ,100)
            v3 = randint(0 ,100)
            v4 = randint(0 ,100)
            print(f"Predict the value of the expression: {v1}+({v2}*{v3})/4")
            answer = v1+(v2*v3)/4
            userAnswer = float(input("Enter your guess: "))
            if userAnswer == answer:
                print("Correct Answer")
            else:
                print("Your answer is wrong.")
                print(f"Correct answer is {answer}")
        else:
            print("Invalid Entry !, Try Again.")
    except:
        print("Invalid Entry !, Try Again.")
