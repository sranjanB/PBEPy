class Student:
    """
    Simple student class
    """
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        print(f"Name : {self.name}")
        print(f"Roll Number: {self.roll}")



print("Creating Object: JACK")
jack = Student("Jack", 19)
jack_2 = Student("Jack", 19)

print("Using Identify Opeator")
print("Jack is Jack2",jack is jack_2)
jack_3 = jack

print("jack is jack_3",jack is jack_3)
print("jack2 is jack3",jack_2 is jack_3)
