def log_ejecucion(func):
    """
    Un decorador que registra el inicio y fin de una función,
    incluyendo sus argumentos.
    """
    def wrapper(*args, **kwargs):
        print(f"INFO: Ejecutando función '{func.__name__}' con args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs) # Llama a la función original con sus argumentos
        print(f"INFO: Función '{func.__name__}' terminada. Resultado: {resultado}")
        return resultado
    return wrapper

@log_ejecucion
def sumar(a, b):
    """Suma dos números."""
    return a + b

@log_ejecucion
def saludar(nombre, mensaje="Hola"):
    """Saluda a una persona con un mensaje."""
    return f"{mensaje}, {nombre}!"

print("--- Sumando números ---")
suma_resultado = sumar(5, 3)
print(f"El resultado final de la suma es: {suma_resultado}")

print("\n--- Saludando a alguien ---")
saludo_resultado = saludar("Alice", mensaje="Buenos días")
print(f"El saludo final es: {saludo_resultado}")

print("\n--- Saludando solo con nombre ---")
saludo_simple = saludar("Bob")
print(f"El saludo simple es: {saludo_simple}")