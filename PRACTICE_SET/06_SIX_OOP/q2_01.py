class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

person1 = Person("John", 18)

print(person1.name,person1.age)
person1.print_person()