import functools

def repetir(num_veces):
    """
    Un decorador que repite la ejecución de la función decorada 'num_veces'.
    """
    def decorador_real(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            resultados = []
            print(f"DEBUG: Repitiendo '{func.__name__}' {num_veces} veces.")
            for _ in range(num_veces):
                res = func(*args, **kwargs)
                resultados.append(res)
            return resultados # Devuelve una lista de resultados
        return wrapper
    return decorador_real

@repetir(num_veces=3)
def lanzar_dado():
    """Simula el lanzamiento de un dado."""
    import random
    valor = random.randint(1, 6)
    print(f"Lanzamiento de dado: {valor}")
    return valor

@repetir(num_veces=2)
def mostrar_mensaje(mensaje):
    """Muestra un mensaje dado."""
    print(f"Mensaje: {mensaje}")
    return mensaje

print("--- Lanzando el dado 3 veces ---")
resultados_dados = lanzar_dado()
print(f"Resultados finales de los dados: {resultados_dados}")

print("\n--- Mostrando mensaje 2 veces ---")
resultados_mensaje = mostrar_mensaje("Hola mundo!")
print(f"Resultados finales del mensaje: {resultados_mensaje}")