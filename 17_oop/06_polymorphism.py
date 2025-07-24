# Reutilizamos las clases Animal, Perro y Gato del ejemplo de herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        """Método polimórfico."""
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        return "¡Guau guau!"

class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def hacer_sonido(self):
        return "¡Miau!"

class Pato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        return "¡Cuac cuac!"

# Función que demuestra el polimorfismo
def hacer_hablar_a_animal(animal):
    """Toma un objeto Animal y hace que hable, sin importar su tipo específico."""
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")

print("--- Demostración de Polimorfismo ---")

perro_polimorfico = Perro("Max", "Pastor Alemán")
gato_polimorfico = Gato("Luna", "Blanco")
pato_polimorfico = Pato("Donald")

animales = [perro_polimorfico, gato_polimorfico, pato_polimorfico]

for animal in animales:
    hacer_hablar_a_animal(animal) # La misma llamada a método, diferente comportamiento

# Otro ejemplo de polimorfismo con operadores mágicos (dunder methods)
print("\n--- Polimorfismo con operadores ---")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        """Define el comportamiento del operador '+'."""
        return Vector(self.x + otro.x, self.y + otro.y)

    def __str__(self):
        """Define la representación en string para print()."""
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 7)

# El operador '+' se comporta de forma diferente para enteros y para objetos Vector
print(f"Suma de enteros: {2 + 3}")
print(f"Suma de vectores: {v1 + v2}")