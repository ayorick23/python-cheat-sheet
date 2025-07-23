# Debugging

La depuración implica encontrar y resolver errores en tu código. Python ofrece varias herramientas y técnicas para hacer este proceso más eficiente.

## Declaración `raise`

La declaración `raise` se usa para lanzar (raise) una excepción explícitamente. Esto es útil cuando una condición de error ocurre y quieres detener la ejecución del programa o pasar el control a un bloque `except` superior.

```python
raise TipoDeExcepcion("Mensaje de error opcional")
```

## Obtener el Traceback como un String

Cuando ocurre una excepción y no se maneja, Python imprime un "traceback" (rastreo de pila) que muestra la secuencia de llamadas a funciones que llevaron al error. Puedes obtener este traceback como una cadena de texto usando el módulo `traceback`, lo cual es útil para registrar errores o enviarlos por correo electrónico.

```python
import traceback

try:
    # Código que falla
    pass
except Exception:
    error_traceback = traceback.format_exc()
    print(error_traceback)
```

## Asserciones

Las aserciones son afirmaciones que se hacen en el código sobre condiciones que se espera que sean `True` en un punto particular del programa. Si la condición de la aserción es `False`, Python lanza una excepción `AssertionError`. Son útiles para la depuración y para documentar supuestos en el código.

```python
assert condicion, "Mensaje de error opcional si la condición es falsa"
```

Las aserciones pueden ser deshabilitadas globalmente si Python se ejecuta con la opción `-O` (modo optimizado), lo que las hace adecuadas para verificaciones de desarrollo pero no para validaciones críticas de entrada de usuario.

## `logging`

El módulo `logging` es la forma estándar y más potente de Python para registrar eventos que ocurren mientras una aplicación se ejecuta. A diferencia de `print()`, que es para depuración rápida, `logging` permite registrar mensajes con diferentes niveles de severidad, dirigir la salida a múltiples destinos (consola, archivo, red) y formatear los mensajes de forma flexible.

### Niveles de Logging

El módulo logging tiene varios niveles de severidad predefinidos, en orden ascendente de prioridad:

1. `DEBUG`: Información detallada, típicamente de interés solo al diagnosticar problemas.
2. `INFO`: Confirmación de que las cosas están funcionando como se esperaba.
3. `WARNING`: Indicación de que algo inesperado ha ocurrido, o indicación de algún problema en el futuro cercano (por ejemplo, 'espacio en disco bajo'). El software sigue funcionando como se esperaba.
4. `ERROR`: Debido a un problema más serio, el software no ha podido realizar alguna función.
5. `CRITICAL`: Un error grave, que indica que el programa mismo no puede continuar ejecutándose.

**Configuración básica:**

```python
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
```

### Deshabilitación de Logging

Puedes deshabilitar temporalmente los mensajes de logging o establecer un nivel de deshabilitación global para suprimir mensajes por debajo de cierto umbral.

```python
logging.disable(logging.CRITICAL) # Deshabilita todos los mensajes por debajo de CRITICAL
logging.disable(logging.NOTSET)   # Vuelve a habilitar el logging
```

### Logging en un Archivo

Es muy común dirigir los mensajes de log a un archivo en lugar de (o además de) la consola. Esto es crucial para la depuración de aplicaciones en producción.

```python
logging.basicConfig(filename='mi_aplicacion.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
```

- `filename`: Especifica el nombre del archivo de log.
- `filemode`: `'a'` (append, por defecto) o `'w'` (write, sobrescribe).
