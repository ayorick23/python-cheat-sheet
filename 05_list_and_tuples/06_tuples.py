# Creación de tuplas
tupla_vacia = ()
print(f"Tupla vacía: {tupla_vacia}")

tupla_simple = (1, 2, 3, "cuatro", 5.0)
print(f"Tupla simple: {tupla_simple}")

tupla_un_elemento = (10,) # La coma es esencial para que sea una tupla
print(f"Tupla de un elemento: {tupla_un_elemento}, Tipo: {type(tupla_un_elemento)}")

no_es_tupla = (10) # Esto es solo un entero entre paréntesis
print(f"Esto no es una tupla: {no_es_tupla}, Tipo: {type(no_es_tupla)}")

# Acceso a elementos y slicing (igual que en las listas)
print(f"Primer elemento: {tupla_simple[0]}")  # Salida: 1
print(f"Último elemento: {tupla_simple[-1]}") # Salida: 5.0
print(f"Slicing: {tupla_simple[1:4]}")    # Salida: (2, 3, 'cuatro')

# Intentar modificar una tupla (causará un TypeError)
try:
    tupla_simple[0] = 99
except TypeError as e:
    print(f"\nError al intentar modificar una tupla: {e}")
# Salida: TypeError: 'tuple' object does not support item assignment

# Concatenación de tuplas (crea una nueva tupla)
tupla_a = (1, 2)
tupla_b = (3, 4)
tupla_concatenada = tupla_a + tupla_b
print(f"Tupla concatenada: {tupla_concatenada}") # Salida: (1, 2, 3, 4)

# Replicación de tuplas (crea una nueva tupla)
tupla_replicada = ("hola",) * 3
print(f"Tupla replicada: {tupla_replicada}") # Salida: ('hola', 'hola', 'hola')

# Desempaquetado de tuplas
# Permite asignar los elementos de una tupla a variables individuales.
persona = ("Juan Pérez", 30, "Ingeniero")
nombre, edad, profesion = persona
print(f"\nNombre: {nombre}, Edad: {edad}, Profesión: {profesion}")

# Uso común de tuplas: múltiples valores de retorno de funciones
def obtener_valores():
    return "valor1", 200, True

v1, v2, v3 = obtener_valores()
print(f"Valores de retorno: {v1}, {v2}, {v3}")