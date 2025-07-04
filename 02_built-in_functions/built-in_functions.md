# Built-in Functions

Python incluye una gran cantidad de funciones built-in que realizan tareas esenciales. A continuación, exploraremos algunas de las más comunes y útiles, con su sintaxis y ejemplos prácticos.

## `print()`

La función `print()` se utiliza para mostrar datos en la consola de salida estándar.

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

- `objects`: Uno o más objetos a imprimir. Se pueden separar por comas.
- `sep`: (Opcional) Una cadena de texto para usar como separador entre los objetos. Por defecto es un espacio.
- `end`: (Opcional) Una cadena de texto que se añade al final de la salida. Por defecto es un salto de línea (`\n`).
- `file`: (Opcional) Un objeto con un método `write()` (como un archivo) al que se enviará la salida. Por defecto es `sys.stdout` (la consola).
- `flush`: (Opcional) Un booleano que, si es `True`, fuerza la "descarga" del búfer de salida.

## `input()`

La función `input()` se utiliza para obtener entrada de datos del usuario a través de la consola. Siempre devuelve la entrada como una cadena de texto.

```python
input([prompt])
```

- `prompt`: (Opcional) Una cadena de texto que se mostrará al usuario antes de esperar la entrada.

## `len()`

La función `len()` devuelve la longitud (el número de ítems) de un objeto. Funciona con secuencias (cadenas, tuplas, listas, rangos) y colecciones (diccionarios, conjuntos).

```python
len(object)
```

- `object`: El objeto del cual se desea conocer la longitud.

## `type()`

La función `type()` devuelve el tipo de un objeto. Es muy útil para la depuración y para entender cómo Python maneja los datos.

```python
type(object)
type(name, bases, dict) # Forma avanzada para crear tipos dinámicamente, menos común
```

- `object`: El objeto cuyo tipo se desea conocer.

## `int()`, `float()`, `str()`, `bool()`

Estas funciones se utilizan para la conversión de tipos (_Type Casting_). Permiten convertir un valor de un tipo de datos a otro.

```python
int(x, base=10) # Convierte a entero
float(x)        # Convierte a flotante
str(object)     # Convierte a cadena
bool(x)         # Convierte a booleano
```

- `x`: El valor a convertir.
- `base`: (Opcional para `int()`) La base del número si `x` es una cadena (ej. `int("101", 2)` para binario).

## `max()` y `min()`

Las funciones `max()` y `min()` se utilizan para encontrar el elemento más grande y el más pequeño, respectivamente, de un iterable o entre varios argumentos.

```python
max(iterable, *[, key, default])
max(arg1, arg2, *args[, key])

min(iterable, *[, key, default])
min(arg1, arg2, *args[, key])
```

- `iterable`: Un objeto iterable (lista, tupla, etc.).
- `arg1`, `arg2`, `*args`: Dos o más argumentos para comparar.
- `key`: (Opcional) Una función de un argumento que se usa para extraer una clave de comparación de cada elemento.
- `default`: (Opcional) El valor a devolver si el iterable está vacío.

## `sum()`

La función `sum()` se utiliza para sumar los elementos de un iterable (normalmente una lista o tupla de números).

```python
sum(iterable, start=0)
```

- `iterable`: Un objeto iterable cuyos elementos se van a sumar.
- `start`: (Opcional) Un valor inicial al que se le sumarán los elementos del iterable. Por defecto es 0.

## `range()`

La función `range()` se utiliza para generar una secuencia inmutable de números, que a menudo se usa en bucles for. Es muy eficiente en memoria, ya que solo genera los números a medida que se necesitan, en lugar de crearlos todos a la vez.

```python
range(stop)
range(start, stop[, step])
```

- `start`: (Opcional) El número entero desde el cual comenzar la secuencia (incluido). Por defecto es 0.
- `stop`: El número entero hasta el cual llegar la secuencia (excluido).
- `step`: (Opcional) El incremento entre cada número de la secuencia. Por defecto es 1. Puede ser negativo.

## `abs()`

La función `abs()` devuelve el valor absoluto de un número.

```python
abs(x)
```

- `x`: Un número entero, flotante o complejo.

## `round()`

La función `round()` redondea un número a una cantidad específica de decimales.

```python
round(number[, ndigits])
```

- `number`: El número a redondear.
- `ndigits`: (Opcional) El número de decimales a redondear. Si se omite, el número se redondea al entero más cercano. Si es None, se devuelve el mismo entero.

**Notas Importantes:**

- Python 3 usa "redondeo a la mitad par" (_round half to even_) para casos donde un número está exactamente en el medio de dos posibilidades (ej., `.5`). Esto significa que `round(2.5)` es `2` y `round(3.5)` es `4`. Esto es para evitar sesgos acumulativos en cálculos grandes.
- El valor devuelto es un entero si `ndigits` se omite o es `None`, de lo contrario es un flotante.

## `pow()`

La función `pow()` devuelve el resultado de elevar un número a una potencia, opcionalmente con un módulo.

```python
pow(base, exp[, mod])
```

- `base`: La base.
- `exp`: El exponente.
- `mod`: (Opcional) El módulo. Si se proporciona, la función devuelve (base \*\* exp) % mod. Esto es más eficiente que calcular la potencia y luego el módulo por separado, especialmente para números grandes.

## `all()` y `any()`

Estas funciones se utilizan para verificar la verdad de los elementos en un iterable.

- `all()`: Devuelve `True` si todos los elementos de un iterable son verdaderos (o si el iterable está vacío).
- `any()`: Devuelve `True` si al menos un elemento de un iterable es verdadero (o si el iterable no está vacío y contiene al menos un elemento falso si todos los demás son verdaderos).

```python
all(iterable)
any(iterable)
```

- `iterable`: Un objeto iterable (lista, tupla, conjunto, etc.).
