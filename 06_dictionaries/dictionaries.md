# Dictionaries

Los **diccionarios** son mutables y se definen utilizando llaves `{}`. Cada par clave-valor se separa por comas, y la clave se separa del valor por dos puntos `:`. Las claves deben ser únicas e inmutables (como cadenas, números o tuplas), mientras que los valores pueden ser de cualquier tipo.

```python
mi_diccionario = {clave1: valor1, clave2: valor2, clave3: valor3, ...}
```

## Obtención de Valores con el Operador `[]`

Puedes acceder a un valor en un diccionario utilizando su clave dentro de corchetes.

```python
valor = mi_diccionario[clave]
```

**Importante:** Si intentas acceder a una clave que no existe, Python lanzará un `KeyError`.

## Métodos para Obtener Vistas

Estos métodos devuelven "vistas" dinámicas de las claves, valores o pares clave-valor del diccionario. Una vista es un objeto que refleja los cambios en el diccionario subyacente.

- `dict.keys()`: Devuelve una vista de todas las claves del diccionario.
- `dict.values()`: Devuelve una vista de todos los valores del diccionario.
- `dict.items()`: Devuelve una vista de todos los pares clave-valor (como tuplas (clave, valor)) del diccionario.

## Obtención de Valores de Forma Segura

El método `get()` permite acceder a un valor asociado a una clave de forma más segura que el operador `[]`, ya que puedes especificar un valor por defecto que se devuelve si la clave no se encuentra.

```python
valor = mi_diccionario.get(clave, valor_por_defecto)
```

- `clave`: La clave del elemento que se desea obtener.
- `valor_por_defecto`: (Opcional) El valor a devolver si la clave no se encuentra. Si se omite, el valor por defecto es `None`.

## Uso de Diccionarios en Bucles `for`

Puedes iterar sobre diccionarios de varias maneras utilizando bucles for, combinándolos con los métodos `keys()`, `values()` e `items()`.

## Añadir y Modificar Elementos de Forma Condicional

El método `setdefault()` permite obtener el valor de una clave. Si la clave no existe, la inserta con un valor por defecto y luego devuelve ese valor. Es útil cuando quieres asegurarte de que una clave existe antes de intentar acceder a ella.

```python
valor = mi_diccionario.setdefault(clave, valor_por_defecto)
```

## Eliminación de Elementos

- `dict.pop(clave[, valor_por_defecto])`: Elimina la clave especificada y devuelve su valor. Si la clave no se encuentra, devuelve `valor_por_defecto` si se proporciona, de lo contrario, lanza un `KeyError`.
- `dict.popitem()`: Elimina y devuelve un par clave-valor arbitrario (generalmente el último par insertado en Python 3.7+). Lanza un `KeyError` si el diccionario está vacío.
- `del sentencia`: Elimina un elemento por su clave. También puede eliminar el diccionario completo. Lanza `KeyError` si la clave no existe.
- `dict.clear()`: Elimina todos los elementos del diccionario, dejándolo vacío.

## Pretty Printing

Para diccionarios complejos o anidados, la salida por defecto de `print()` puede ser difícil de leer. El módulo `pprint` (_pretty-print_) proporciona una forma de imprimir estructuras de datos de manera legible y bien formateada.

```python
import pprint

pprint.pprint(diccionario, indent=num_espacios, width=ancho_maximo)
```

- `indent`: (Opcional) Número de espacios para la indentación.
- `width`: (Opcional) Ancho máximo de línea antes de envolver el texto.

## Unión de Diccionarios

Python 3.5 introdujo el operador de desempaquetado de diccionario (`**`) para fusionar diccionarios, y Python 3.9 introdujo el operador de unión de diccionarios (`|`).

### Operador de Desempaquetado (`**`)

Permite fusionar diccionarios al crear uno nuevo. Si hay claves duplicadas, el valor del diccionario más a la derecha "gana".

```python
nuevo_diccionario = {**diccionario1, **diccionario2, ...}
```

### Operador de Unión (`|`) y Actualización (`|=)`

- `|` (Operador de Unión): Crea un nuevo diccionario fusionando dos o más diccionarios.
- `|=` (Operador de Actualización): Fusiona un diccionario en otro en su lugar (modifica el diccionario de la izquierda).

```python
# Unión:
nuevo_diccionario = diccionario1 | diccionario2

# Actualización in-place:
diccionario1 |= diccionario2
```
