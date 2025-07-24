def decorar_saludo(funcion):
    """
    Este decorador añade un mensaje de saludo antes y después de la ejecución de una función.
    """
    def wrapper():
        print("¡Hola! Soy el decorador y estoy a punto de llamar a tu función.")
        funcion() # Llama a la función original
        print("¡Adiós! Soy el decorador y tu función ha terminado.")
    return wrapper

@decorar_saludo
def decir_nombre():
    """Una función simple que dice un nombre."""
    print("Mi nombre es Python.")

@decorar_saludo
def despedirse():
    """Una función simple que se despide."""
    print("¡Hasta la próxima!")

print("--- Ejecutando función decorada decir_nombre() ---")
decir_nombre()

print("\n--- Ejecutando función decorada despedirse() ---")
despedirse()