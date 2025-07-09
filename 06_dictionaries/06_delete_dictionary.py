# Diccionario de ejemplo
diccionario_datos = {
    "nombre": "Luis",
    "edad": 30,
    "ciudad": "México",
    "profesion": "Arquitecto"
}
print(f"Diccionario inicial: {diccionario_datos}")

# pop()
edad_eliminada = diccionario_datos.pop("edad")
print(f"Después de pop('edad'): {diccionario_datos}") # Salida: {'nombre': 'Luis', 'ciudad': 'México', 'profesion': 'Arquitecto'}
print(f"Edad eliminada: {edad_eliminada}") # Salida: 30

# pop() con valor por defecto
profesion_eliminada = diccionario_datos.pop("profesion", "Desconocida")
print(f"Después de pop('profesion'): {diccionario_datos}") # Salida: {'nombre': 'Luis', 'ciudad': 'México'}
print(f"Profesión eliminada: {profesion_eliminada}") # Salida: Arquitecto

inexistente = diccionario_datos.pop("pais", "Clave no encontrada")
print(f"Intento de pop de clave inexistente: {inexistente}") # Salida: Clave no encontrada

# popitem()
ultimo_par = diccionario_datos.popitem() # Elimina un par (ej. 'ciudad': 'México')
print(f"Después de popitem(): {diccionario_datos}") # Salida: {'nombre': 'Luis'}
print(f"Último par eliminado: {ultimo_par}") # Salida: ('ciudad', 'México')

# del sentencia
del diccionario_datos["nombre"]
print(f"Después de del diccionario_datos['nombre']: {diccionario_datos}") # Salida: {}

# Intentar eliminar una clave que no existe con del (causa KeyError)
try:
    del diccionario_datos["apellido"]
except KeyError as e:
    print(f"\nError: {e} - No se puede eliminar una clave que no existe.")

# clear()
otro_diccionario = {"a": 1, "b": 2, "c": 3}
print(f"\nOtro diccionario antes de clear(): {otro_diccionario}")
otro_diccionario.clear()
print(f"Otro diccionario después de clear(): {otro_diccionario}") # Salida: {}