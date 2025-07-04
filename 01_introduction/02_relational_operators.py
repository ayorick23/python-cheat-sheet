# Operadores Relacionales

a = 10
b = 20
c = 10

# Igual que (==)
print(f"{a} == {b} es {a == b}")  # Salida: 10 == 20 es False
print(f"{a} == {c} es {a == c}")  # Salida: 10 == 10 es True

# Diferente de (!=)
print(f"{a} != {b} es {a != b}")  # Salida: 10 != 20 es True
print(f"{a} != {c} es {a != c}")  # Salida: 10 != 10 es False

# Mayor que (>)
print(f"{a} > {b} es {a > b}")  # Salida: 10 > 20 es False
print(f"{b} > {a} es {b > a}")  # Salida: 20 > 10 es True

# Menor que (<)
print(f"{a} < {b} es {a < b}")  # Salida: 10 < 20 es True
print(f"{b} < {a} es {b < a}")  # Salida: 20 < 10 es False

# Mayor o igual que (>=)
print(f"{a} >= {c} es {a >= c}")  # Salida: 10 >= 10 es True
print(f"{a} >= {b} es {a >= b}")  # Salida: 10 >= 20 es False

# Menor o igual que (<=)
print(f"{a} <= {c} es {a <= c}")  # Salida: 10 <= 10 es True
print(f"{b} <= {a} es {b <= a}")  # Salida: 20 <= 10 es False