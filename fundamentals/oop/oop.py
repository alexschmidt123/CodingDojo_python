class Employee:

    def __init__(self, first_name, last_name, salary, department, middle_name = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = salary
        self.department = department

    def change_salary(self, new_salary):
        if isinstance(new_salary, int):
            if new_salary > 40000:
                self.salary = new_salary

    def full_name(self):
        if self.middle_name == None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
    
    # def __repr__(self):


new_employee1 = Employee('Adam', 'Jone', 40000, 'Sales')
new_employee2 = Employee('Brad', 'Smith', 68000, 'HR')
new_employee3 = Employee('Charlie', 'Adams', 74000, 'Engineering',middle_name='Jacob')
new_employee4 = Employee(last_name='Alexander', first_name='Dave', salary=74000, department='Engineering')

print(new_employee1.salary)
new_employee1.change_salary(52000)
print(new_employee1.salary)
new_employee1.change_salary(-52000)
print(new_employee1.salary)


employees =[new_employee1,new_employee2,new_employee3,new_employee4]

for employee in employees:
    print(employee.full_name())