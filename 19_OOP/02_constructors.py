class Animal:

    # Constructors are made with init
    def __init__(self, name, age, breed):
        self.name = name.lower()
        self.age = age
        self.breed = breed.lower()

    def get_information(self):
        print(self.name)
        print(self.age)
        print(self.breed)
        print(self) # will print the object type and the location in memory

    def set_name(self, name):
        self.name = name.lower()

    def get_name(self):
        return self.name.title()


zozo = Animal('zozo', 25, 'chihuahua')
print(zozo.get_name())


zozo.get_information()
print(zozo)