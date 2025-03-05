#Definir una clase
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")
        
#Crear un objeto
person1 = Person("Dereck", 25)
person1.greet()