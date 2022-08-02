# Creating Student class
class Student:
    """This is  a Simple Student Class."""
    name = "Student class"

    def say_hi(self, student_name):
        """A simple mthod to say hello to a student."""
        print(f"Hello {student_name}")
        print(f"You are using {self.name} now.")

# Creating an object from student class
object1 = Student()
object1.say_hi('Saumya')

object2 = Student()
object2.say_hi("Ranjan")
