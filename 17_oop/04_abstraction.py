from abc import ABC, abstractmethod

# Clase base abstracta para formas geométricas
class Forma(ABC):
    @abstractmethod
    def area(self):
        """Calcula el área de la forma."""
        pass

    @abstractmethod
    def perimetro(self):
        """Calcula el perímetro de la forma."""
        pass

    def describir(self):
        """Método concreto que todas las formas pueden usar."""
        print(f"Esta es una forma geométrica: {type(self).__name__}")

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.14159 * self.radio

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

print("--- Usando clases abstractas para la abstracción ---")

# Intentar instanciar una clase abstracta directamente (fallará)
try:
    mi_forma = Forma()
except TypeError as e:
    print(f"Error: No se puede instanciar una clase abstracta directamente: {e}")

circulo1 = Circulo(5)
rectangulo1 = Rectangulo(4, 6)

print(f"\nCírculo - Área: {circulo1.area():.2f}, Perímetro: {circulo1.perimetro():.2f}")
circulo1.describir()

print(f"\nRectángulo - Área: {rectangulo1.area()}, Perímetro: {rectangulo1.perimetro()}")
rectangulo1.describir()

# Una lista de formas abstractas, pero cada una se comporta de forma concreta
formas = [Circulo(7), Rectangulo(8, 3)]
print("\n--- Procesando una lista de formas ---")
for f in formas:
    print(f"\nTipo: {type(f).__name__}")
    print(f"  Área: {f.area():.2f}")
    print(f"  Perímetro: {f.perimetro():.2f}")