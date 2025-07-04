# Operadores de Asignación

x = 10
print(f"Valor inicial de x = {x}") # Salida: Valor inicial de x = 10

# Asignación simple (=)
y = x
print(f"Después de y = x, y = {y}") # Salida: Después de y = x, y = 10

# Suma y asignación (+=)
x += 5  # Equivalente a x = x + 5
print(f"Después de x += 5, x = {x}") # Salida: Después de x += 5, x = 15

# Resta y asignación (-=)
x -= 3  # Equivalente a x = x - 3
print(f"Después de x -= 3, x = {x}") # Salida: Después de x -= 3, x = 12

# Multiplicación y asignación (*=)
x *= 2  # Equivalente a x = x * 2
print(f"Después de x *= 2, x = {x}") # Salida: Después de x *= 2, x = 24

# División y asignación (/=)
x /= 4  # Equivalente a x = x / 4
print(f"Después de x /= 4, x = {x}") # Salida: Después de x /= 4, x = 6.0

# Módulo y asignación (%=)
x = 10
x %= 3  # Equivalente a x = x % 3
print(f"Después de x %= 3 (con x=10), x = {x}") # Salida: Después de x %= 3 (con x=10), x = 1

# Exponenciación y asignación (**=)
x = 2
x **= 3 # Equivalente a x = x ** 3
print(f"Después de x **= 3 (con x=2), x = {x}") # Salida: Después de x **= 3 (con x=2), x = 8

# División entera y asignación (//=)
x = 10
x //= 3 # Equivalente a x = x // 3
print(f"Después de x //= 3 (con x=10), x = {x}") # Salida: Después de x //= 3 (con x=10), x = 3

x &= 1  # Equivalente a x = x & 1 (AND bit a bit)
print(f"Después de x &= 1 (con x=3), x = {x}") # Salida: Después de x &= 1 (con x=3), x = 1

x |= 2  # Equivalente a x = x | 2 (OR bit a bit)
print(f"Después de x |= 2 (con x=3), x = {x}") # Salida: Después de x |= 2 (con x=3), x = 3

x ^= 1  # Equivalente a x = x ^ 1 (XOR bit a bit)
print(f"Después de x ^= 1 (con x=1), x = {x}") # Salida: Después de x ^= 1 (con x=1), x = 0

# Desplazamiento a la derecha y asignación (>>=)
x = 8
x >>= 2  # Equivalente a x = x >> 2
print(f"Después de x >>= 2 (con x=8), x = {x}") # Salida: Después de x >>= 2 (con x=8), x = 2

# Desplazamiento a la izquierda y asignación (<<=)
x = 1
x <<= 2  # Equivalente a x = x << 2
print(f"Después de x <<= 2 (con x=1), x = {x}") # Salida: Después de x <<= 2 (con x=1), x = 4