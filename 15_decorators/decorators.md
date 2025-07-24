# Decorators

En esencia, un decorador es una función que toma otra función como argumento, le añade alguna funcionalidad, y devuelve la función modificada. Se utilizan con la sintaxis `@nombre_decorador` justo encima de la definición de una función o clase.

## Decoradores Básicos

Un decorador básico es una función que acepta otra función, define una función interna (el "wrapper") que añade la lógica deseada y luego llama a la función original, y finalmente devuelve esta función interna.

```python
def mi_decorador(funcion_original):
    def funcion_wrapper(*args, **kwargs):
        # Lógica ANTES de la función original
        resultado = funcion_original(*args, **kwargs)
        # Lógica DESPUÉS de la función original
        return resultado
    return funcion_wrapper

@mi_decorador
def mi_funcion():
    pass
```

## Decorador para una Función con Parámetros

Si la función que vas a decorar acepta argumentos, tu función `wrapper` dentro del decorador también debe ser capaz de aceptar esos argumentos. Para ello, usamos `*args` y `**kwargs`.

- `*args`: Recoge un número variable de argumentos posicionales en una tupla.
- `**kwargs`: Recoge un número variable de argumentos de palabra clave en un diccionario.

## Plantillas para Decoradores (`functools.wraps`)

Cuando usas decoradores, la función `wrapper` que devuelve el decorador reemplaza a la función original. Esto significa que los metadatos de la función original (como su nombre, docstring, etc.) se pierden. Para preservar estos metadatos, usamos el decorador `@functools.wraps` del módulo `functools`.

```python
import functools

def mi_decorador(funcion_original):
    @functools.wraps(funcion_original) # ¡Importante para preservar metadatos!
    def funcion_wrapper(*args, **kwargs):
        # Lógica...
        return funcion_original(*args, **kwargs)
    return funcion_wrapper
```

## Decorador con Parámetros

A veces, necesitas que tu decorador acepte sus propios argumentos además de la función que va a decorar. Esto se logra anidando una función adicional en la estructura del decorador.

```python
def decorador_con_parametros(param1, param2):
    def mi_decorador(funcion_original):
        @functools.wraps(funcion_original)
        def funcion_wrapper(*args, **kwargs):
            # Lógica que usa param1, param2 y la funcion_original
            return funcion_original(*args, **kwargs)
        return funcion_wrapper
    return mi_decorador

@decorador_con_parametros(param1="valor1", param2="valor2")
def mi_funcion():
    pass
```

## Decoradores de Clase

Los decoradores no solo se aplican a funciones, también pueden aplicarse a clases. Un decorador de clase toma una clase como argumento y devuelve una clase modificada (o una nueva clase). Esto es útil para modificar el comportamiento de todas las instancias de una clase, añadir métodos, o imponer ciertas propiedades.

```python
def decorador_de_clase(ClaseOriginal):
    # Modificar ClaseOriginal aquí, o crear una nueva
    class NuevaClase(ClaseOriginal):
        def nuevo_metodo(self):
            print("Método añadido por el decorador de clase.")
    return NuevaClase

@decorador_de_clase
class MiClase:
    pass
```
