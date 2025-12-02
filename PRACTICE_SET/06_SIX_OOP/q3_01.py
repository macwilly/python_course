class Animal:

    def sound(self):
        print("Some sound")

class Dog(Animal):

    def sound(self):
        print("Bark!")


otto = Dog()

otto.sound()
