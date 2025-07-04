# Operadores Bit a Bit (Bitwise)
# Se aplican a los bits individuales de los números enteros.
# 10 en binario es 0000 1010
# 4 en binario es  0000 0100

a = 10
b = 4

# AND Bit a Bit (&)
# 0000 1010
# &0000 0100
# =0000 0000 (0 en decimal)
print(f"{a} & {b} = {a & b}")  # Salida: 10 & 4 = 0

# OR Bit a Bit (|)
# 0000 1010
# |0000 0100
# =0000 1110 (14 en decimal)
print(f"{a} | {b} = {a | b}")  # Salida: 10 | 4 = 14

# XOR Bit a Bit (^)
# 0000 1010
# ^0000 0100
# =0000 1110 (14 en decimal)
print(f"{a} ^ {b} = {a ^ b}")  # Salida: 10 ^ 4 = 14

# NOT Bit a Bit (~)
# Invierte todos los bits. Para un número positivo x, el resultado es -(x+1).
# ~10 (binario: ...11111111111111111111111111110101)
print(f"~{a} = {~a}")  # Salida: ~10 = -11 (depende del sistema, pero sigue la regla -(x+1))

# Desplazamiento a la izquierda (<<)
# Mueve los bits hacia la izquierda, añadiendo ceros a la derecha.
# Equivalente a multiplicar por 2 elevado a la potencia del desplazamiento.
# 10 << 1 (1010 -> 10100 = 20)
print(f"{a} << 1 = {a << 1}")  # Salida: 10 << 1 = 20

# Desplazamiento a la derecha (>>)
# Mueve los bits hacia la derecha, añadiendo ceros a la izquierda (para positivos).
# Equivalente a dividir por 2 elevado a la potencia del desplazamiento (descartando decimales).
# 10 >> 1 (1010 -> 101 = 5)
print(f"{a} >> 1 = {a >> 1}")  # Salida: 10 >> 1 = 5