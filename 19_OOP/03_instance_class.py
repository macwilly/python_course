class Employee:
    company = 'Asus' # Class attribute

    def __init__(self, bond, name, salary, company = company):
        self.bond = bond
        self.name = name
        self.salary = salary
        self.company = company

    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"The name of the employee is: {self.name}. Salary is: {self.salary}. The bond is: {self.bond} years.")


e1 = Employee(5, 'Tigger', 20000, 'Disney')
print(e1.company) # Will always print instance attribute


e2 = Employee(5, 'Tigger', 20000 )
print(e2.company) # Will always print instance attribute

# How to print Class attributes
print(Employee.company)

# Object introspection look at the methods and properties of an object
print(dir(e1))