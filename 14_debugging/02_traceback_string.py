import traceback
import sys

def funcion_tres():
    return 10 / 0 # Causa un ZeroDivisionError

def funcion_dos():
    return funcion_tres()

def funcion_uno():
    return funcion_dos()

print("--- Obtener traceback como string ---")

try:
    funcion_uno()
except Exception as e:
    print("Ocurrió una excepción. Obteniendo el traceback como string:")
    # traceback.format_exc() sin argumentos recupera el último error manejado
    traceback_str = traceback.format_exc()
    print(traceback_str)

    # Puedes obtener el traceback directamente de sys.exc_info()
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("\nTipo de excepción:", exc_type)
    print("Valor de excepción:", exc_value)
    print("Objeto traceback:", exc_traceback) # Esto es el objeto traceback