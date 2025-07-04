# Pedir al usuario que ingrese su nombre
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola, {nombre}!")

# Pedir un número y convertirlo a entero
try:
    edad_str = input("¿Cuántos años tienes? ")
    edad_int = int(edad_str)
    print(f"Así que tienes {edad_int} años.")
    print(f"En 5 años tendrás {edad_int + 5} años.")
except ValueError:
    print("Eso no parece un número válido para la edad.")

# Pedir dos números y sumarlos
try:
    num1_str = input("Ingresa el primer número: ")
    num2_str = input("Ingresa el segundo número: ")
    num1 = float(num1_str) # Usamos float para permitir decimales
    num2 = float(num2_str)
    print(f"La suma de {num1} y {num2} es: {num1 + num2}")
except ValueError:
    print("Asegúrate de ingresar números válidos.")