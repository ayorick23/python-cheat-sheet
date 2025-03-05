class Cat:
    def makeSound(self):
        return "Meow!"
    
class Cow:
    def makeSound(self):
        return "Moo!"
    
#Función que usa polimorfismo
def animalSound(animal):
    print(animal.makeSound())
    
#Prueba de polimorfismo
cat = Cat()
cow = Cow()
animalSound(cat)
animalSound(cow)