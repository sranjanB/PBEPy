class Student:
    """
    This is a student class with a constructor.
    """
    def __init__(self, name, roll_no):
        """
        The name and roll_no is used to identification.
        """
        self.name = name
        self.roll_no = roll_no

    def get_details(self):
        """
        Points to details of a student.
        """
        print("The current student details is ")
        print(f"Name: {self.name}")
        print(f"Roll number: {self.roll_no}")

    def update_details(self, new_name, new_roll):
        """
        to update existing details.
        """
        self.name = new_name
        self.roll_no = new_roll


# Creating an object
student_1 = Student("Mihir", 1)

# Prinitng the details
student_1.get_details()

# Changing the artibute value
student_1.name = "Ranjan"
student_1.roll_no = 19
print("----After the first update.---")
student_1.get_details()

#Using update method
student_1.update_details("Saumya", 20)
print("---After the second Update.---")
student_1.get_details()
