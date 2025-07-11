# Funciones

Las funciones en Python son objetos de primera clase, lo que significa que pueden ser tratadas como cualquier otra variable: pueden ser pasadas como argumentos, devueltas por otras funciones y asignadas a variables.

## Definición de una Función

Una función se define usando la palabra clave `def`, seguida del nombre de la función, paréntesis para los parámetros y dos puntos. El cuerpo de la función debe estar indentado.

```python
def nombre_de_la_funcion(parametro1, parametro2, ...):
    """
    Docstring: Breve descripción de lo que hace la función.
    Esta es una buena práctica para documentar tu código.
    """
    # Cuerpo de la función
    # Realiza operaciones
    return valor_opcional # La declaración return devuelve un valor y termina la función
```

## Tipos de Argumentos

Python es muy flexible con los argumentos de las funciones. Puedes definir funciones que acepten diferentes tipos de argumentos:

1. **Argumentos Posicionales Obligatorios**

Son los argumentos que deben pasarse en el orden correcto y son obligatorios.

```python
def sumar(a, b):
    return a + b

print(sumar(5, 3)) # a=5, b=3
```

1. **Argumentos por Defecto (Opcionales)**

Permiten especificar un valor por defecto para un parámetro. Si el llamador no proporciona un valor para ese parámetro, se usa el valor por defecto. Los argumentos por defecto deben ir después de los argumentos posicionales.

```python
def saludar_ciudad(nombre, ciudad="Mundo"):
    return f"Hola {nombre} de {ciudad}."

print(saludar_ciudad("Carlos"))        # Salida: Hola Carlos de Mundo.
print(saludar_ciudad("Ana", "Bogotá")) # Salida: Hola Ana de Bogotá.
```

3. **Argumentos de Palabra Clave (Keyword Arguments)**

Permiten pasar argumentos usando su nombre, lo que mejora la legibilidad y permite cambiar el orden.

```python
def describir_persona(nombre, edad, ocupacion):
    return f"{nombre} tiene {edad} años y es {ocupacion}."

print(describir_persona(nombre="Sofía", ocupacion="Ingeniera", edad=30))
# Salida: Sofía tiene 30 años y es Ingeniera. (El orden no importa al usar palabras clave)
```

4. **Argumentos de Longitud Variable (`*args` y `**kwargs`)\*\*

- `*args` **(Argumentos Posicionales Arbitrarios):** Permite que una función acepte un número variable de argumentos posicionales. Estos se agrupan en una tupla dentro de la función.
- `**kwargs` **(Argumentos de Palabra Clave Arbitrarios):** Permite que una función acepte un número variable de argumentos de palabra clave. Estos se agrupan en un diccionario dentro de la función.

```python
def funcion_args_kwargs(*args, **kwargs):
    # args será una tupla
    # kwargs será un diccionario
    pass
```

## Valores de Retorno

Las funciones pueden devolver uno o más valores utilizando la palabra clave `return`. Si una función no tiene una sentencia `return` explícita, automáticamente devuelve `None`.

```python
def funcion_sin_retorno():
    print("Solo imprimo")

def funcion_con_un_retorno(a, b):
    return a * b

def funcion_con_multiples_retornos(x, y):
    suma = x + y
    resta = x - y
    return suma, resta # Devuelve una tupla implícitamente
```

## Variables Globales y Locales

El **ámbito (scope)** de una variable determina dónde puede ser accedida y modificada en tu código.

- **Variable Local:** Una variable definida dentro de una función es local a esa función. Solo puede ser accedida desde dentro de esa función. Diferentes funciones pueden tener variables locales con el mismo nombre sin conflicto.
- **Variable Global:** Una variable definida fuera de cualquier función (a nivel de módulo) es global. Puede ser accedida desde cualquier parte del código, incluyendo dentro de funciones. Sin embargo, para modificar una variable global dentro de una función, necesitas la declaración `global`.

### Declaración `global`

La declaración `global` se utiliza dentro de una función para indicar que una variable específica no es local, sino que se refiere a una variable global existente. Esto te permite modificar el valor de una variable global desde dentro de una función.

```python
variable_global = 10

def mi_funcion():
    global variable_global
    # Ahora puedes modificar variable_global
    variable_global = 20
```

## Funciones Lambda (Funciones Anónimas)

Las funciones lambda son pequeñas funciones anónimas (sin nombre) que se definen con la palabra clave lambda. Son útiles para tareas cortas y simples que solo requieren una expresión, y no una definición de función completa (`def`).

```python
lambda argumentos: expresion
```

- `argumentos:` Pueden ser cero o más argumentos, separados por comas.
- `expresion:` Una única expresión. El resultado de esta expresión es el valor de retorno de la función lambda.

### Características

- Solo pueden contener una única expresión.
- No pueden contener sentencias como `if`, `for`, `while`, `return`, etc. (solo la expresión).
- Se suelen usar en contextos donde se espera una función como argumento (por ejemplo, con `map()`, `filter()`, `sorted()`).
