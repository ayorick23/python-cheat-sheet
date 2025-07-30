import array

print("--- Demostración del módulo array ---")

# 'i' es el código de tipo para signed integer (entero con signo)
# Otros códigos: 'f' para float, 'd' para double, 'B' para unsigned char, etc.
# Consulta la documentación de 'array' para una lista completa.
numeros_enteros = array.array('i', [10, 20, 30, 40, 50])

print(f"Array original: {numeros_enteros}")
print(f"Tipo de elementos en el array: {numeros_enteros.typecode}")
print(f"Primer elemento: {numeros_enteros[0]}")
print(f"Longitud del array: {len(numeros_enteros)}")

# Añadir un elemento
numeros_enteros.append(60)
print(f"Array después de append: {numeros_enteros}")

# Intentar añadir un tipo incorrecto (dará TypeError)
try:
    numeros_enteros.append(3.14)
except TypeError as e:
    print(f"Error al intentar añadir float: {e}")

# Crear un array de floats
numeros_flotantes = array.array('f', [1.1, 2.2, 3.3])
print(f"Array de flotantes: {numeros_flotantes}")

# Comparación de memoria (para demostrar eficiencia, aunque es más notable con muchos elementos)
import sys
list_int = [1, 2, 3, 4, 5]
array_int = array.array('i', [1, 2, 3, 4, 5])
print(f"\nTamaño en memoria de una lista de 5 enteros: {sys.getsizeof(list_int)} bytes")
print(f"Tamaño en memoria de un array de 5 enteros: {sys.getsizeof(array_int)} bytes")
# Verás que el array es significativamente más pequeño para la misma cantidad de datos.