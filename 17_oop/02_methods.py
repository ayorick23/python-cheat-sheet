class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        self.felicidad = 5 # Nivel de felicidad inicial (1-10)

    # Método de instancia
    def ladrar(self):
        """Hace que el perro ladre."""
        print(f"{self.nombre} dice: ¡Guau guau!")

    # Método de instancia con parámetros
    def comer(self, comida):
        """Simula que el perro come algo."""
        print(f"{self.nombre} está comiendo {comida}.")
        self.felicidad += 1 # Aumenta la felicidad al comer
        if self.felicidad > 10:
            self.felicidad = 10

    # Método para mostrar el estado del perro
    def mostrar_estado(self):
        print(f"{self.nombre} ({self.raza}). Nivel de felicidad: {self.felicidad}/10")

# Creando objetos Perro
fido = Perro("Fido", "Golden Retriever")
buddy = Perro("Buddy", "Poodle")

# Llamando a los métodos de los objetos
print("--- Interacción con Fido ---")
fido.mostrar_estado()
fido.ladrar()
fido.comer("croquetas")
fido.mostrar_estado()

print("\n--- Interacción con Buddy ---")
buddy.mostrar_estado()
buddy.ladrar()
buddy.comer("un hueso")
buddy.comer("un filete")
buddy.mostrar_estado()