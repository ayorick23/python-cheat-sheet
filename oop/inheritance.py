#Clase padre
class Animal:
    def __init__(self, name):
        self.name = name
        
    def makeSound(self):
        print("Some generic animal sound")

#Clase hija
class Dog(Animal):        
    def makeSound(self):
        print("Woof woof!")
        
dog = Dog("Buddy")
dog.makeSound()