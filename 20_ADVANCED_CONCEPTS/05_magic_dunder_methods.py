# dunder = double underscore __
class Employee:
    company = "HP"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # more for the user
    def __str__(self):
        return f"{self.name} {self.salary}"

    # repr is mostly used for debuffing
    def __repr__(self):
        return f"name = {self.name}\nsalary {self.salary}"

    # The developer will decide how to assign what len will return
    def __len__(self):
        return len(self.name)


e = Employee('Tiger Woods', 20000)

print(e.name, e.salary)
print(str(e))
print(repr(e))
print(len(e))