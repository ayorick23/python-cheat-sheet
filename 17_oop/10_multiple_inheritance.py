class Volador:
    def volar(self):
        return "Estoy volando."

    def habilidad(self):
        return "Habilidad de volar."

class Acuatico:
    def nadar(self):
        return "Estoy nadando."

    def habilidad(self): # Mismo nombre de método que en Volador
        return "Habilidad de nadar."

class Pato(Volador, Acuatico): # Pato hereda de Volador y Acuatico
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Cuac cuac."

print("--- Demostración de Herencia Múltiple ---")

mi_pato = Pato("Donald")

print(f"{mi_pato.nombre} dice: {mi_pato.hacer_sonido()}")
print(f"{mi_pato.nombre} sabe: {mi_pato.volar()}")
print(f"{mi_pato.nombre} sabe: {mi_pato.nadar()}")

# ¿Qué habilidad se llama? Depende del MRO.
print(f"{mi_pato.nombre} tiene la habilidad: {mi_pato.habilidad()}")

# Ver el Orden de Resolución de Métodos (MRO)
print("\n--- Orden de Resolución de Métodos (MRO) de Pato ---")
print(Pato.mro())
# Output esperado (orden puede variar ligeramente en Python versions):
# [<class '__main__.Pato'>, <class '__main__.Volador'>, <class '__main__.Acuatico'>, <class 'object'>]
# Como 'Volador' está antes que 'Acuatico' en la definición de Pato, Volador.habilidad() se usa.

# Para llamar específicamente a un método de una clase padre en herencia múltiple
class PatoModificado(Volador, Acuatico):
    def __init__(self, nombre):
        self.nombre = nombre

    def habilidad(self):
        # Puedes llamar a ambas habilidades si es necesario
        habilidad_volar = super().habilidad() # Llama a la siguiente en el MRO (Volador)
        habilidad_nadar = Acuatico.habilidad(self) # Llamada explícita al método de Acuatico
        return f"{habilidad_volar} y {habilidad_nadar}"

pato_m = PatoModificado("Daisy")
print(f"\n{pato_m.nombre} (Modificado) tiene la habilidad: {pato_m.habilidad()}")