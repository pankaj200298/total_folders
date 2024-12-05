class employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print(f" the role of employee is {self.role}")
        print(f" the department of employee is {self.department}")
        print(f" the salary if employee is {self.salary} lpa")


class Engineer(employee):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer","automation testing " , 15  )


# employee1 = employee("engineer" , "automation testing ", 12)
# employee1.show_details()


E1 = Engineer("pankaj", 26)
E1.show_details()