def procesar_valor(valor):
    try:
        numero = int(valor) # Podría lanzar ValueError
        resultado = 100 / numero # Podría lanzar ZeroDivisionError
        print(f"Resultado: {resultado}")
    except ValueError:
        print(f"Error: '{valor}' no es un número válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except TypeError as e: # Por si el input no es un tipo comparable (ej. None)
        print(f"Error de tipo: {e}")
    except Exception as e: # Captura cualquier otra excepción no esperada
        print(f"Ocurrió un error inesperado: {e}")

print("--- Procesando diferentes valores ---")
procesar_valor("10")
procesar_valor("abc")
procesar_valor("0")
procesar_valor(None) # Esto generará un TypeError