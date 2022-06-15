"""
Guess in 3 attempt.
"""
from random import randint

while True:
    userInterest = input("Would like to play[y/n] = ")
    try:
        if userInterest == "y":
            flag = False
            guessNumber = randint(1, 15)
            print("The computer has picked a random number for you.")
            print("Clue: It is between 1 to 15 (inclusive) .")
            print("Can you guess it within 3 try ?")
            for i in range(1, 4):
                answer = int(input("Enter your answer: "))
                if answer == guessNumber:
                    print(f"Excellent ! You have won in {i} attempt.")
                    flag = True
                    break
                elif answer > guessNumber:
                    print(f"It is high. {3 - i} attempt left.")
                elif answer < guessNumber:
                    print(f"It is Low. {3 - i} attempt left.")

            if not flag:
                print(f"You have Lost ! {guessNumber} is the number.")
        elif userInterest == "n":
            print("Thanks for playing.")
            break
        else:
            print("Invalid Input.")
    except:
        print("Invalid Entry !!")
