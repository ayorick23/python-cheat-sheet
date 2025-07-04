# Definir la función
def saludar(nombre):
    """Esta función saluda a la persona cuyo nombre se pasa como argumento."""
    mensaje = f"¡Hola, {nombre}! Bienvenido a Python."
    return mensaje

# Llamar a la función
saludo_personalizado = saludar("Dereck")
print(saludo_personalizado) # Salida: ¡Hola, Dereck! Bienvenido a Python.

# Función sin parámetros y sin retorno explícito
def mostrar_mensaje():
    print("Este es un mensaje simple desde una función.")

mostrar_mensaje() # Salida: Este es un mensaje simple desde una función.

# El valor de retorno por defecto es None si no hay un return explícito
resultado = mostrar_mensaje()
print(f"El resultado de la función sin retorno explícito es: {resultado}") # Salida: None