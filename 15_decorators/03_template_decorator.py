import functools

def mi_decorador_con_wraps(func):
    """Este es un decorador de plantilla que usa @functools.wraps."""
    @functools.wraps(func) # Aquí está la magia
    def wrapper(*args, **kwargs):
        print(f"Antes de llamar a {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"Después de llamar a {func.__name__}")
        return resultado
    return wrapper

@mi_decorador_con_wraps
def funcion_ejemplo(a, b):
    """Esta es la docstring de funcion_ejemplo."""
    return a * b

print("--- Examinando metadatos de la función decorada ---")
print(f"Nombre de la función: {funcion_ejemplo.__name__}")
print(f"Docstring de la función: {funcion_ejemplo.__doc__}")

print("\n--- Ejecutando la función decorada ---")
res = funcion_ejemplo(4, 5)
print(f"Resultado: {res}")

# Sin @functools.wraps, __name__ sería 'wrapper' y __doc__ sería el docstring del wrapper.