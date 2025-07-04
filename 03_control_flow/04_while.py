# Bucle while básico
contador = 0
print("--- Bucle while básico ---")
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1 # Es crucial actualizar la condición para evitar un bucle infinito

# Bucle while con break
print("\n--- Bucle while con break ---")
i = 0
while True: # Bucle infinito intencional
    print(f"Iteración (con break): {i}")
    if i >= 3:
        break # Sale del bucle cuando i es 3
    i += 1
print("Bucle terminado por break.")

# Bucle while con continue
print("\n--- Bucle while con continue ---")
j = 0
while j < 5:
    j += 1
    if j == 3:
        print(f"Saltando el número 3...")
        continue # Salta el resto del código en esta iteración y va a la siguiente
    print(f"Procesando número: {j}")
print("Bucle con continue finalizado.")

# Bucle while para pedir input hasta que sea válido
print("\n--- Bucle while para input válido ---")
while True:
    contrasena = input("Ingresa la contraseña (admin123): ")
    if contrasena == "admin123":
        print("¡Contraseña correcta!")
        break
    else:
        print("Contraseña incorrecta. Intenta de nuevo.")