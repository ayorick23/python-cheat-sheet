# Context Managers

Un gestor de contexto es un objeto que define el comportamiento de entrada y salida de un contexto runtime. Básicamente, se encarga de configurar un recurso antes de usarlo y de asegurar que se cierre o libere después, sin importar cómo termine el bloque de código.

## Declaración `with`

La declaración `with` es la forma más común de usar un gestor de contexto. Simplifica el manejo de la adquisición y liberación de recursos, como archivos, conexiones de red o bloqueos. Python garantiza que el método de limpieza se ejecutará al final del bloque `with`, incluso si una excepción se lanza dentro del bloque.

```python
with expresion_gestor_contexto as variable:
    # Código que usa el recurso
    pass
# El recurso se limpia automáticamente aquí
```

El gestor de contexto es un objeto que debe implementar dos métodos especiales:

- `__enter__(self)`: Se ejecuta al principio del bloque `with`. Su valor de retorno (si lo hay) se asigna a la variable después de `as`.
- `__exit__(self, exc_type, exc_val, exc_tb)`: Se ejecuta al final del bloque `with`, incluso si ocurre una excepción. Recibe información sobre la excepción si esta ocurrió. Si `__exit__` devuelve `True`, la excepción se suprime; si devuelve `False` (o nada), la excepción se vuelve a lanzar.

## Creando tu Propio Gestor de Contexto (`contextlib.contextmanager`)

Para crear tus propios gestores de contexto de una manera más sencilla (sin tener que definir una clase completa con `__enter__` y `__exit__`), puedes usar el decorador `@contextlib.contextmanager` del módulo `contextlib`.

Este decorador te permite escribir un gestor de contexto como una simple función generadora. La parte del código antes de `yield` actúa como el método `__enter__`, y la parte después de `yield` (en el bloque `finally` para asegurar la limpieza) actúa como el método `__exit__`.

```python
import contextlib

@contextlib.contextmanager
def mi_gestor_funcion(recurso):
    # Lógica de entrada (lo que ocurriría en __enter__)
    print(f"Adquiriendo recurso: {recurso}")
    try:
        yield recurso # El valor que se asigna a la variable 'as'
    finally:
        # Lógica de salida/limpieza (lo que ocurriría en __exit__)
        print(f"Liberando recurso: {recurso}")

with mi_gestor_funcion("Mi Base de Datos") as db:
    # Usar db
    pass
```

## Clases Basadas en Gestor de Contexto

Aunque `contextlib.contextmanager` es muy conveniente para casos sencillos, para gestores de contexto más complejos que necesitan mantener un estado o tener una lógica más sofisticada, es mejor crear una clase que implemente los métodos `__enter__` y `__exit__`.

```python
class MiGestorDeContextoClase:
    def __init__(self, parametro):
        self.parametro = parametro
        # Inicialización de estado

    def __enter__(self):
        # Lógica de entrada
        print(f"Entrando en el contexto con parámetro: {self.parametro}")
        # Retornar el recurso que se asignará a 'as'
        return self.parametro.upper()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Lógica de salida/limpieza
        if exc_type:
            print(f"Saliendo del contexto debido a un error: {exc_type.__name__}: {exc_val}")
            # Retornar True para suprimir la excepción, False (o None) para relanzarla
            # return True
        else:
            print("Saliendo del contexto normalmente.")
        return False # No suprimir la excepción por defecto
```
