# Inicialización de un conjunto
mi_conjunto = {1, 2, 3, 4, 5}
print(f"Conjunto inicial: {mi_conjunto}") # Salida: {1, 2, 3, 4, 5} (el orden puede variar)

# Conjunto con duplicados (los duplicados son eliminados automáticamente)
conjunto_con_duplicados = {1, 2, 2, 3, 4, 4, 5}
print(f"Conjunto con duplicados: {conjunto_con_duplicados}") # Salida: {1, 2, 3, 4, 5} (solo elementos únicos)

# Creando un conjunto a partir de una lista
lista_original = [10, 20, 30, 20, 40, 10]
conjunto_desde_lista = set(lista_original)
print(f"Conjunto desde lista: {conjunto_desde_lista}") # Salida: {40, 10, 20, 30} (orden desordenado)

# Creando un conjunto vacío (IMPORTANTE)
conjunto_vacio_correcto = set()
print(f"Conjunto vacío correcto: {conjunto_vacio_correcto}, Tipo: {type(conjunto_vacio_correcto)}")

# Esto NO crea un conjunto vacío, crea un diccionario vacío
diccionario_vacio = {}
print(f"Esto es un diccionario vacío: {diccionario_vacio}, Tipo: {type(diccionario_vacio)}")

# Intentar acceder por índice (causará un TypeError)
try:
    print(mi_conjunto[0])
except TypeError as e:
    print(f"\nError al intentar indexar un conjunto: {e}") # Salida: TypeError: 'set' object is not subscriptable

# Verificar pertenencia (muy eficiente)
print(f"¿Está 3 en mi_conjunto? {3 in mi_conjunto}") # Salida: True
print(f"¿Está 6 en mi_conjunto? {6 in mi_conjunto}") # Salida: False