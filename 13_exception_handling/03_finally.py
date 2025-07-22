import os

nombre_archivo = "mi_recurso.txt"

def manejar_recurso(operacion):
    f = None # Inicializamos f para que sea accesible en finally
    try:
        f = open(nombre_archivo, "w") # Intentar abrir para escritura
        if operacion == "escribir":
            f.write("Datos importantes.")
            print("Datos escritos con éxito.")
        elif operacion == "dividir":
            resultado = 10 / 0 # Causa un ZeroDivisionError
            print(f"Resultado de división: {resultado}")
        else:
            print("Operación desconocida.")
    except ZeroDivisionError:
        print("Manejo: Error de división por cero.")
    except Exception as e:
        print(f"Manejo: Ocurrió un error inesperado: {e}")
    finally:
        # Este bloque siempre se ejecuta
        if f: # Asegurarse de que el archivo fue abierto antes de intentar cerrarlo
            f.close()
            print("Archivo cerrado en finally.")
        print("Bloque finally completado.")

print("--- Escenario 1: Operación exitosa ---")
manejar_recurso("escribir")

print("\n--- Escenario 2: Ocurre una excepción ---")
manejar_recurso("dividir")

# Limpieza (si el archivo se creó en el primer escenario)
if os.path.exists(nombre_archivo):
    os.remove(nombre_archivo)