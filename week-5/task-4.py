class Employee:
    def __init__(self, salary):   
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self._salary * 0.15   


def print_employees(employees):
    for emp in employees:
        print(emp.get_role(), emp.get_salary())


employees = [
    Employee(1500),   
    Manager(4000)
]

print_employees(employees)
