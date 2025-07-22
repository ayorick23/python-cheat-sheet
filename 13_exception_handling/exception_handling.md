# Exception Handling

El **manejo de excepciones** es el proceso de responder a eventos (_excepciones_) que alteran el flujo normal de un programa. Python utiliza los bloques `try`, `except`, `else` y `finally` para gestionar estos errores.

## Manejo de Excepciones Básico

La forma más fundamental de manejar excepciones es utilizando los bloques `try` y `except`.

- El código que podría generar una excepción se coloca dentro del bloque `try`.
- Si ocurre una excepción dentro del `try`, la ejecución de ese bloque se detiene y el control pasa al bloque `except` correspondiente.
- Si no ocurre ninguna excepción, el bloque `except` se omite.

```python
try:
    # Código que podría generar una excepción
    pass
except TipoDeExcepcion:
    # Código a ejecutar si ocurre TipoDeExcepcion
    pass
```

## Múltiples Excepciones

Puedes manejar diferentes tipos de excepciones para el mismo bloque `try`.

- Puedes especificar múltiples bloques `except`, cada uno para un tipo de excepción diferente.
- Puedes agrupar múltiples tipos de excepciones en una sola tupla en un mismo `except`.
- Es una buena práctica capturar las excepciones más específicas primero, y las más generales después.

```python
try:
    # Código
except TipoDeExcepcion1:
    # Manejar TipoDeExcepcion1
except TipoDeExcepcion2:
    # Manejar TipoDeExcepcion2
except (TipoDeExcepcion3, TipoDeExcepcion4):
    # Manejar TipoDeExcepcion3 o TipoDeExcepcion4
except Exception as e: # Captura cualquier otra excepción
    # Manejar excepciones genéricas y acceder al objeto de excepción
    pass
```

## Bloque `finally`

El bloque `finally` se ejecuta siempre, sin importar si ocurrió una excepción o no, y si fue manejada o no. Es ideal para limpiar recursos, como cerrar archivos o conexiones de red.

```python
try:
    # Código
except TipoDeExcepcion:
    # Manejo de la excepción
finally:
    # Código que siempre se ejecuta
```

**Nota:** También existe el bloque `else`. Se ejecuta si el bloque `try` se completa sin que ocurra ninguna excepción. Se coloca después de todos los bloques except.

```python
try:
    # Código
except AlgunaExcepcion:
    # Manejar excepción
else:
    # Se ejecuta si NO hubo excepción en el 'try'
finally:
    # Siempre se ejecuta
```

## Creación de Excepciones Personalizadas

A veces, las excepciones incorporadas de Python no son lo suficientemente específicas para los errores de tu aplicación. Puedes crear tus propias excepciones personalizadas heredando de la clase `Exception` (o de una de sus subclases, como `ValueError`).

```python
class MiExcepcionPersonalizada(Exception):
    def __init__(self, mensaje="Ha ocurrido mi excepción personalizada"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Para levantarla:
raise MiExcepcionPersonalizada("Algo salió mal específicamente aquí.")
```

## Excepciones Comunes

| Excepción           | Significado                                                                                  | Cuándo ocurre                                                                                    |
| ------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `SyntaxError`       | Error de sintaxis; el código no es válido Python.                                            | Olvidar un `)`, `:` o una comilla; indentación incorrecta (cuando no es `IndentationError`).     |
| `IdentationError`   | El código tiene una indentación incorrecta.                                                  | Mezclar espacios y tabs; indentación inesperada o faltante.                                      |
| `NameError`         | Se hace referencia a una variable o función que no ha sido definida.                         | `print(variable_no_existente)`                                                                   |
| `TypeError`         | Operación o función aplicada a un objeto de tipo inapropiado.                                | `len(5)`; `2 + "hola"`; llamar a un entero como función.                                         |
| `ValueError`        | Una función recibe un argumento del tipo correcto, pero con un valor inapropiado.            | `int("abc")`; `math.sqrt(-1)` (para raíces reales).                                              |
| `ZeroDivisionError` | Intento de dividir un número por cero.                                                       | `10 / 0`.                                                                                        |
| `IndexError`        | Se intenta acceder a un índice fuera de los límites de una secuencia (lista, tupla, cadena). | `mi_lista[5]` si `len(mi_lista)` es 3.                                                           |
| `KeyError`          | Se intenta acceder a una clave que no existe en un diccionario.                              | `mi_diccionario['clave_inexistente']`.                                                           |
| `FileNotFoundError` | El archivo o directorio especificado no existe.                                              | `open("no_existe.txt", "r")`.                                                                    |
| `IOError`           | Error genérico de entrada/salida (antes de `FileNotFoundError` y `PermissionError`).         | Problemas al leer/escribir en disco, dispositivos.                                               |
| `PermissionError`   | Intento de acceder a un archivo o directorio sin los permisos adecuados.                     | Intentar escribir en un archivo de solo lectura.                                                 |
| `AttributeError`    | Se intenta acceder a un atributo o método que no existe en un objeto.                        | `mi_objeto.atributo_inexistente`; `mi_lista.append(5).sort()`.                                   |
| `StopIteration`     | Un iterador no tiene más elementos.                                                          | Cuando `next()` se llama en un iterador agotado. (Internamente manejada por for loops).          |
| `MemoryError`       | Una operación se queda sin memoria.                                                          | Crear una lista enorme `[0] * (10**10)`.                                                         |
| `RecursionError`    | Una función recursiva se llama a sí misma demasiadas veces (límite de recursión excedido).   | Funciones recursivas sin caso base o con un caso base incorrecto.                                |
| `SystemExit`        | Solicitud de salida del intérprete Python.                                                   | Levantada por `sys.exit()`.                                                                      |
| `KeyboardInterrupt` | El usuario interrumpe la ejecución del programa (Ctrl+C).                                    | Cuando el usuario presiona Ctrl+C.                                                               |
| `Exception`         | Clase base para la mayoría de las excepciones no relacionadas con el sistema.                | Se usa para capturar una amplia gama de errores genéricos (aunque se prefiere la especificidad). |
