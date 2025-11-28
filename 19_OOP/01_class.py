# In Python, `self` is used instead of `this`
class Employee:
    company = "HP"

    # self needs to be the first parameter
    def getSalary(self):
        return f"At {self.company} you make 34000"



e = Employee()

print(e.getSalary())
print(e.company)