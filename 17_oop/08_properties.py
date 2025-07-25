class Rectangulo:
    def __init__(self, ancho, alto):
        self._ancho = None # Atributos internos protegidos
        self._alto = None
        self.ancho = ancho # Usamos los setters para validar
        self.alto = alto

    @property
    def ancho(self):
        """Getter para el atributo ancho."""
        print("INFO: Accediendo al ancho.")
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        """Setter para el atributo ancho, con validación."""
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El ancho debe ser un número positivo.")
        print(f"INFO: Estableciendo ancho a {valor}.")
        self._ancho = valor

    @property
    def alto(self):
        """Getter para el atributo alto."""
        print("INFO: Accediendo al alto.")
        return self._alto

    @alto.setter
    def alto(self, valor):
        """Setter para el atributo alto, con validación."""
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El alto debe ser un número positivo.")
        print(f"INFO: Estableciendo alto a {valor}.")
        self._alto = valor

    @property
    def area(self):
        """Propiedad calculada dinámicamente."""
        print("INFO: Calculando área.")
        return self.ancho * self.alto # Usa los getters de ancho y alto

print("--- Demostración de Propiedades (@property) ---")

rect = Rectangulo(10, 5)

print(f"Ancho inicial: {rect.ancho}") # Llama al getter de ancho
print(f"Alto inicial: {rect.alto}")   # Llama al getter de alto

print(f"Área: {rect.area}") # Llama al getter de area (que a su vez llama a los getters de ancho/alto)

# Intentar asignar un valor inválido al ancho
try:
    rect.ancho = -5
except ValueError as e:
    print(f"Error al establecer ancho: {e}")

# Cambiar el ancho y ver cómo se recalcula el área
rect.ancho = 12
print(f"Nuevo ancho: {rect.ancho}")
print(f"Nueva área: {rect.area}")

# Uso del deleter (opcional, si se necesita)
class Producto:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @nombre.deleter
    def nombre(self):
        print("INFO: Eliminando el nombre del producto.")
        del self._nombre

p = Producto("Monitor")
print(f"\nNombre del producto: {p.nombre}")
del p.nombre
try:
    print(f"Nombre del producto después de eliminar: {p.nombre}")
except AttributeError as e:
    print(f"Error: {e} (el nombre fue eliminado)")