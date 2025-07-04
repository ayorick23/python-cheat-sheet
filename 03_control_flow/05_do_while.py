# Emulación de do-while para pedir un número positivo
print("--- Emulación de do-while para número positivo ---")
numero_positivo = 0
while True:
    try:
        numero_str = input("Ingresa un número positivo: ")
        numero_positivo = int(numero_str)
        if numero_positivo > 0:
            print(f"Número ingresado: {numero_positivo}")
            break # Salimos del bucle si el número es positivo
        else:
            print("El número debe ser positivo. Intenta de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

# Otra forma de emular do-while
print("\n--- Otra emulación de do-while ---")
opcion = ''
while True:
    print("\nMenú:")
    print("1. Jugar")
    print("2. Opciones")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        print("¡Iniciando el juego!")
    elif opcion == '2':
        print("Abriendo opciones...")
    elif opcion == '3':
        print("Saliendo del programa.")
        break # Salimos si el usuario elige salir
    else:
        print("Opción inválida. Intenta de nuevo.")