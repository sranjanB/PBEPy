class MyException(Exception):
    """This is a custom Exception"""
    pass

try:
    user_input = int(input("Enter an integer below 100: "))
    if user_input > 100:
        raise MyException("You have not followed the rule , it is 100 <")
    print(f"Well done , {user_input} is a correct input.")
except MyException as e:
    print(f"Cusetom exception is raised. Error details: {e}")
except ValueError as e:
    print(f"value error details: {e}")
