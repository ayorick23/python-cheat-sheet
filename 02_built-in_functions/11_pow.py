# Elevar a una potencia simple
print(f"pow(2, 3): {pow(2, 3)}")     # Salida: 8 (2 elevado a la 3)
print(f"pow(5, 2): {pow(5, 2)}")     # Salida: 25 (5 elevado a la 2)

# Con números flotantes
print(f"pow(2.5, 2): {pow(2.5, 2)}") # Salida: 6.25

# Elevar a una potencia negativa
print(f"pow(2, -2): {pow(2, -2)}")   # Salida: 0.25 (1 / 2^2)

# Usando el tercer argumento 'mod' (potencia modular)
# pow(base, exp, mod) es equivalente a (base ** exp) % mod
print(f"pow(2, 10, 5): {pow(2, 10, 5)}") # Salida: 4
# Explicación: (2**10) = 1024. 1024 % 5 = 4