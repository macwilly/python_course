class Employee:
    def __init__(self, salary = None):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            print("salary cannot be negative")
        else:
            self._salary = new_salary

emp = Employee()

emp.salary = 100
print(emp.salary)
emp.salary = -200
print(emp.salary)