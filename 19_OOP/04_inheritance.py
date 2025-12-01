class Animal:
    location = "Australia"
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")



class Dog(Animal):
    def speak(self):
        super().speak() # Super will get the instance of the parent class and cll that method
        print("Woof")






a = Animal("Animal")
a.speak()

zozo = Dog("Zozo")
zozo.speak()
print(Dog.location)
print(zozo.location)