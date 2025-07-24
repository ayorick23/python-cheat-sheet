# Clase Base (Superclase)
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Animal '{self.nombre}' creado.")

    def hablar(self):
        """Método que será sobrescrito por las subclases."""
        raise NotImplementedError("Las subclases deben implementar este método")

    def info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad} años.")

# Subclase Perro hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad) # Llama al constructor de la clase padre
        self.raza = raza
        print(f"Perro '{self.nombre}' de raza {self.raza} creado.")

    # Sobrescribir el método hablar
    def hablar(self):
        return "¡Guau guau!"

    # Añadir un nuevo método específico de Perro
    def traer_objeto(self, objeto):
        print(f"{self.nombre} ha traído el {objeto}.")

# Subclase Gato hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color_pelo):
        super().__init__(nombre, edad)
        self.color_pelo = color_pelo
        print(f"Gato '{self.nombre}' de color {self.color_pelo} creado.")

    # Sobrescribir el método hablar
    def hablar(self):
        return "¡Miau!"

# Creando objetos de las subclases
print("--- Demostración de Herencia ---")
mi_perro = Perro("Fido", 3, "Labrador")
mi_gato = Gato("Whiskers", 2, "Negro")

print("\n--- Información de los animales ---")
mi_perro.info()      # Método heredado de Animal
print(f"El perro dice: {mi_perro.hablar()}") # Método sobrescrito
mi_perro.traer_objeto("pelota") # Método propio de Perro

mi_gato.info()       # Método heredado de Animal
print(f"El gato dice: {mi_gato.hablar()}")   # Método sobrescrito

# Verificar tipos
print(f"\n¿mi_perro es una instancia de Perro? {isinstance(mi_perro, Perro)}")
print(f"¿mi_perro es una instancia de Animal? {isinstance(mi_perro, Animal)}")
print(f"¿Perro es una subclase de Animal? {issubclass(Perro, Animal)}")