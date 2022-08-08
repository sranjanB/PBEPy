from employee_module import Employee, PersonalDetails

emp_1 = Employee("Jack", 3)
emp_1_details = PersonalDetails(emp_1.name, emp_1.company, 10.2, 39, "19 USO")

emp_1.get_details()
emp_1_details.backgroundDetails()
