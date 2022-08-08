# This is an Employee class where you can
# find the name, employee_id and company details.

class Employee:
    """
    Basic employee detils.
    """
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        self.company = "Sasken"

    def get_details(self):
        print(f"\nThe current Employee details are:")
        print(f"Name : {self.name}")
        print(f"Id: {self.emp_id}")
        print(f"Company: {self.company}")

class PersonalDetails:
    """
    background details of an employee.
    """
    def __init__(self, name, current_company, work_exp, age, address):
        self.name  = name
        self.current_company = current_company
        self.work_exp = work_exp
        self.age = age
        self.address = address

    def backgroundDetails(self):
        print("-"*10)
        print("Here are the backgound details.")
        print(f"Name : {self.name}\nCurrent Company:{self.current_company}\nWork Experience : {self.work_exp}\nAge :{self.age}\nAddress : {self.address}")
        print("-"*10)
