class Student:
    """This a Student class with a construcor."""
    def __init__(self, name, roll_no):
        """
        The name and roll to 
        identify student properly.
        """
        print(f"The student name is: {name}")
        print(f"The student roll number is: {roll_no}")

# Creating an object from student class
student_robin = Student("Robin", 22)
