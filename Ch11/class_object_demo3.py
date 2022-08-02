class Student:
    """
    Student class with a constructor.
    """
    def __init__(self, name, roll_no):
        """
        name and roll no
        to identify.
        """
        print("This constructor has two parameters.")
        self.name = name
        self.roll_no = roll_no
        print(f"The student name is: {self.name}")
        print(f"The student roll is: {self.roll_no}")

# Creating object from student class
# Using the constructor that accepts two parameters.
student_jack = Student("Jack",45)
