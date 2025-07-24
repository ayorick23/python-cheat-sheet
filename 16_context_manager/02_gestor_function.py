import contextlib
import time

@contextlib.contextmanager
def temporizador(nombre="Bloque"):
    """
    Un gestor de contexto que mide el tiempo de ejecución de un bloque de código.
    """
    inicio = time.time()
    print(f"[{nombre}] Iniciando temporizador...")
    try:
        yield # El control se pasa al bloque 'with'
    finally:
        fin = time.time()
        duracion = fin - inicio
        print(f"[{nombre}] Finalizado. Duración: {duracion:.4f} segundos.")

print("--- Usando gestor de contexto basado en función ---")

with temporizador("Operación Lenta"):
    print("Realizando una operación que toma tiempo...")
    time.sleep(1.5) # Simular trabajo
    print("Operación lenta completada.")

print("\n--- Otro uso del temporizador ---")
with temporizador("Cálculo"):
    total = sum(range(1, 1000000))
    print(f"Cálculo completado. Suma: {total}")

print("\n--- Temporizador con error ---")
try:
    with temporizador("Bloque con error"):
        print("Intentando algo que puede fallar...")
        raise ValueError("¡Error intencional!")
except ValueError as e:
    print(f"Excepción capturada fuera del bloque: {e}")
    # Nota que el finally del temporizador igual se ejecuta