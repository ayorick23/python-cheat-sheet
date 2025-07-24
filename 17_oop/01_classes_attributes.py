class Coche:
    # Atributo de Clase: compartido por todas las instancias de Coche
    numero_ruedas = 4

    def __init__(self, marca, modelo, color):
        """
        Método constructor para inicializar un nuevo objeto Coche.
        'self' se refiere a la instancia actual del objeto.
        """
        # Atributos de Instancia: únicos para cada objeto Coche
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0 # Atributo con valor por defecto

# Creando instancias de la clase Coche
coche1 = Coche("Toyota", "Corolla", "Rojo")
coche2 = Coche("Ford", "Focus", "Azul")

# Accediendo a atributos de instancia
print(f"Coche 1: Marca={coche1.marca}, Modelo={coche1.modelo}, Color={coche1.color}, Velocidad={coche1.velocidad}")
print(f"Coche 2: Marca={coche2.marca}, Modelo={coche2.modelo}, Color={coche2.color}, Velocidad={coche2.velocidad}")

# Accediendo a atributos de clase
print(f"Número de ruedas (Coche 1): {coche1.numero_ruedas}")
print(f"Número de ruedas (Coche 2): {coche2.numero_ruedas}")
print(f"Número de ruedas (Clase Coche): {Coche.numero_ruedas}")

# Modificando atributos de instancia
coche1.velocidad = 60
print(f"Nueva velocidad de Coche 1: {coche1.velocidad}")
print(f"Velocidad de Coche 2 (no afectada): {coche2.velocidad}")

# Modificando atributo de clase a través de la clase (afecta a todas las instancias)
Coche.numero_ruedas = 5 # ¡Imagina que es un coche con una rueda de repuesto o un camión pequeño!
print(f"Nuevo número de ruedas (Coche 1): {coche1.numero_ruedas}")
print(f"Nuevo número de ruedas (Coche 2): {coche2.numero_ruedas}")