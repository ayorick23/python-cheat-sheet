# Operadores de Identidad
# Se utilizan para comparar las ubicaciones de memoria de dos objetos.
# Es decir, si dos variables se refieren al mismo objeto en memoria.

a = [1, 2, 3]
b = [1, 2, 3]
c = a

# is
# ¿a es el mismo objeto que b?
print(f"¿a is b? {a is b}")  # Salida: ¿a is b? False (aunque tengan el mismo contenido, son objetos diferentes en memoria)

# ¿a es el mismo objeto que c?
print(f"¿a is c? {a is c}")  # Salida: ¿a is c? True (c se refiere al mismo objeto que a)

# Comparando enteros pequeños (Python los "interna" para optimización)
x = 5
y = 5
z = 1000
w = 1000

print(f"¿x is y? {x is y}")  # Salida: ¿x is y? True (para enteros pequeños, Python reutiliza objetos)
print(f"¿z is w? {z is w}")  # Salida: ¿z is w? False (para enteros grandes, normalmente son objetos distintos)

# is not
print(f"¿a is not b? {a is not b}") # Salida: ¿a is not b? True
print(f"¿a is not c? {a is not c}") # Salida: ¿a is not c? False