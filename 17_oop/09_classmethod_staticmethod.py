class Vehiculo:
    numero_vehiculos = 0 # Atributo de clase

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        Vehiculo.numero_vehiculos += 1 # Incrementa el contador de vehículos
        print(f"Vehículo '{marca} {modelo}' creado.")

    def info_instancia(self):
        """Método de instancia: Accede a atributos de instancia y de clase."""
        print(f"Soy un {self.marca} {self.modelo}. Hay {Vehiculo.numero_vehiculos} vehículos en total.")

    @classmethod
    def obtener_total_vehiculos(cls):
        """
        Método de clase: Accede al atributo de clase 'numero_vehiculos'.
        'cls' se refiere a la clase misma (Vehiculo en este caso).
        """
        print(f"Desde el método de clase: Actualmente hay {cls.numero_vehiculos} vehículos.")
        return cls.numero_vehiculos

    @classmethod
    def crear_coche_generico(cls, modelo_generico="Genérico"):
        """
        Método de clase: Constructor alternativo.
        Crea una nueva instancia de la clase (o subclase si se hereda).
        """
        print(f"Creando un coche genérico de modelo '{modelo_generico}'.")
        return cls("Genérica", modelo_generico)

    @staticmethod
    def es_vehiculo_motorizado(tipo):
        """
        Método estático: No accede a la instancia ni a la clase.
        Solo es una función de utilidad relacionada lógicamente con la clase.
        """
        tipos_motorizados = ["coche", "moto", "camion"]
        return tipo.lower() in tipos_motorizados

print("--- Demostración de Métodos de Clase y Estáticos ---")

v1 = Vehiculo("BMW", "X5")
v2 = Vehiculo("Mercedes", "Clase C")

v1.info_instancia()
v2.info_instancia()

# Llamada a método de clase a través de la clase
Vehiculo.obtener_total_vehiculos()

# Llamada a método de clase a través de una instancia (aunque no es lo típico)
v1.obtener_total_vehiculos()

# Usando el constructor alternativo (método de clase)
v3 = Vehiculo.crear_coche_generico("Modelo X")
v3.info_instancia()

# Llamada a método estático a través de la clase
print(f"\n¿'Coche' es motorizado? {Vehiculo.es_vehiculo_motorizado('Coche')}")
print(f"¿'Bicicleta' es motorizada? {Vehiculo.es_vehiculo_motorizado('Bicicleta')}")

# Llamada a método estático a través de una instancia (también posible)
print(f"¿'{v1.marca}' es motorizado? {v1.es_vehiculo_motorizado('Coche')}")

# Demostración en herencia: classmethod entiende la jerarquía
class Camion(Vehiculo):
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self.capacidad_carga = capacidad_carga

    def info_instancia(self):
        print(f"Soy un {self.marca} {self.modelo} con {self.capacidad_carga} kg de carga.")

print("\n--- Método de clase con herencia ---")
c1 = Camion("Volvo", "FH16", 25000)
c1.info_instancia()

# El método de clase llamado desde Camion devolverá el total de vehículos de la clase Vehiculo
# y creará una instancia de Camion si se usa el constructor alternativo.
Camion.obtener_total_vehiculos()
c2 = Camion.crear_coche_generico("Camion Ligero") # Esto crea un objeto Camion, no Vehiculo
c2.info_instancia()