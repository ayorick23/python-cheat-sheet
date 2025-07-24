import functools

def añadir_timestamp(ClaseOriginal):
    """
    Un decorador de clase que añade un atributo `creado_en`
    a cada nueva instancia de la clase, con la hora de creación.
    """
    @functools.wraps(ClaseOriginal) # Para preservar los metadatos de la clase
    class ClaseMejorada(ClaseOriginal):
        def __init__(self, *args, **kwargs):
            import datetime
            super().__init__(*args, **kwargs)
            self.creado_en = datetime.datetime.now()
            print(f"INFO: '{ClaseOriginal.__name__}' instancia creada con timestamp.")
    return ClaseMejorada

@añadir_timestamp
class Documento:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido
        print(f"Documento '{self.titulo}' inicializado.")

    def mostrar(self):
        print(f"\n--- Documento: {self.titulo} ---")
        print(self.contenido)
        print(f"Creado en: {self.creado_en}")

@añadir_timestamp
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        print(f"Usuario '{self.nombre}' inicializado.")

    def info(self):
        print(f"\nUsuario: {self.nombre} ({self.email})")
        print(f"Registro: {self.creado_en}")

print("--- Creando instancias de clases decoradas ---")
doc1 = Documento("Reporte Mensual", "Este es el contenido del reporte.")
doc1.mostrar()

user1 = Usuario("Ana", "ana@example.com")
user1.info()

# Accediendo al atributo añadido por el decorador
print(f"\nTipo de doc1: {type(doc1)}")
print(f"Hora de creación de doc1 (directo): {doc1.creado_en}")