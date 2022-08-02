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
