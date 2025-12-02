class Employee:
    company = 'HP' # class attribute
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # This is an instance method. All the default methods are
    def print_info(self):
        return f"Name: {self.name} Salary: {self.salary}"
    # Static methods
    @staticmethod
    def sum(a,b):
        return a + b

    # Class method
    @classmethod
    def print_company(cls):
        return f"Company: {cls.company}"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company




e1 = Employee('Jack', 20000)
e2 = Employee('Jill', 80000)

print(e1.company)
print(e1.print_info())
print(e2.print_info())

#Static methods
print(e1.sum(10, 20))
# Static methods can be used without creating the object
print(Employee.sum(5,85))


# Class Methods This will impact all instances of the class
print(e1.print_company())
e1.change_company("Apple")
print(e1.print_company())
print(Employee.print_company())
print(e2.company)