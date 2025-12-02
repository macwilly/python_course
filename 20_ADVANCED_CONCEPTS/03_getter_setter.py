class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def first_name(self):
        return self.name.split(" ")[0]

    # def set_frst_name(self, first_name):
    #     self.first_name = first_name

    # With python a decorator called `property` that will allow the function to be called without the ()
    @property
    def last_name(self):
        name_list = self.name.split(" ")

        if len(name_list) > 1:
            return name_list[-1]
        else:
            return "No last name given"

    @last_name.setter
    def last_name(self, name):
        new_name = f"{self.first_name()} {name}"
        self.name = new_name

e = Employee('Tiger Woods', 20000)

e.project = 6
print(e.name)
print(e.salary)
print(e.project)
print(e.first_name())
print(e.last_name)


r = Employee('Romeo', 20000)
print(r.first_name())
print(r.last_name)
r.last_name = 'capulet'
print(r.last_name)
