class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # __str__ para representación legible para humanos
    def __str__(self):
        return f'"{self.titulo}" por {self.autor}'

    # __repr__ para representación inequívoca (útil para depuración)
    def __repr__(self):
        return f'Libro("{self.titulo}", "{self.autor}", {self.paginas})'

    # __len__ para que len() funcione con objetos Libro
    def __len__(self):
        return self.paginas

    # __eq__ para comparar igualdad (==)
    def __eq__(self, other):
        if not isinstance(other, Libro):
            return NotImplemented
        return self.titulo == other.titulo and self.autor == other.autor

    # __add__ para sumar libros (ejemplo de operador)
    def __add__(self, other):
        if isinstance(other, Libro):
            # Sumar páginas de dos libros
            return self.paginas + other.paginas
        elif isinstance(other, int):
            # Sumar un número a las páginas
            return self.paginas + other
        return NotImplemented

    # __call__ para hacer que la instancia sea "callable"
    def __call__(self, mensaje):
        print(f"El libro {self.titulo} dice: {mensaje}")

print("--- Demostración de Dunder Methods ---")

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 496)
libro2 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 368)
libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 496) # Mismo que libro1

print(f"Representación para humanos (str): {libro1}")
print(f"Representación para desarrolladores (repr): {repr(libro1)}")

print(f"Número de páginas de '{libro1.titulo}': {len(libro1)} páginas")

print(f"\n¿Libro 1 es igual a Libro 2? {libro1 == libro2}")
print(f"¿Libro 1 es igual a Libro 3? {libro1 == libro3}") # True porque __eq__ compara título y autor

print(f"\nPáginas totales de Libro 1 y Libro 2: {libro1 + libro2}")
print(f"Páginas de Libro 1 + 50: {libro1 + 50}")

# Llamar a una instancia de Libro como si fuera una función
libro1("¡Disfruta la lectura!")

# __getitem__ y __setitem__ para una clase similar a una lista/diccionario
class MiColeccion:
    def __init__(self):
        self._items = []

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return len(self._items)

    def add_item(self, item):
        self._items.append(item)

mi_coleccion = MiColeccion()
mi_coleccion.add_item("Manzana")
mi_coleccion.add_item("Banana")

print(f"\nElementos en la colección: {mi_coleccion[0]}, {mi_coleccion[1]}")
mi_coleccion[0] = "Pera"
print(f"Elemento modificado: {mi_coleccion[0]}")
print(f"Tamaño de la colección: {len(mi_coleccion)}")