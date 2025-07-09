# Manipulación de Cadenas (Strings)

Las cadenas en Python son secuencias inmutables de caracteres Unicode. Inmutable significa que, una vez creadas, no se pueden modificar en su lugar. Cualquier operación que "modifique" una cadena en realidad crea una nueva cadena.

## Caracteres de Escape

Un carácter de escape se crea escribiendo una barra invertida \ seguida del carácter que desea insertar.

| Caracter de Escape | Impresión |
| ------------------ | --------- |
| `\'`               |

## Cadenas Multilínea

Puedes crear cadenas que abarcan varias líneas utilizando comillas triples (`'''` o `"""`). Esto es muy útil para bloques de texto largos, como documentación o mensajes.

```python
cadena_multilinea = """
Este es un texto
que ocupa varias líneas.
Es muy útil para párrafos largos.
"""
```

## Indexación y Slicing

Al igual que las listas y las tuplas, las cadenas son secuencias y, por lo tanto, admiten indexación y slicing para acceder a caracteres o subcadenas.

- **Indexación:** Accede a un carácter individual por su posición. El primer carácter está en el índice `0`. Los índices negativos cuentan desde el final (`-1` es el último carácter).
- **Slicing (Rebanado):** Extrae una porción de la cadena.

```python
cadena[inicio:fin:paso]
```

- `inicio`: (Opcional) Índice de inicio (incluido).
- `fin`: (Opcional) Índice de fin (excluido).
- `paso`: (Opcional) Tamaño del salto entre caracteres (por defecto `1`).

## Métodos de Cambio de Caso

Estos métodos devuelven una nueva cadena con el caso de los caracteres modificado.

- `str.upper()`: Convierte todos los caracteres de la cadena a mayúsculas.
- `str.lower()`: Convierte todos los caracteres de la cadena a minúsculas.
- `str.capitalize()`: Convierte el primer carácter de la cadena a mayúscula y el resto a minúsculas.
- `str.title()`: Convierte la primera letra de cada palabra de la cadena a mayúscula y el resto a minúsculas.

## Métodos de Verificación de Caso

Estos métodos devuelven un valor booleano (`True` o `False`) indicando si todos los caracteres alfabéticos de la cadena están en un caso específico. Ignoran caracteres no alfabéticos.

- `str.isupper()`: Devuelve `True` si todos los caracteres alfabéticos de la cadena están en mayúsculas.
- `str.islower()`: Devuelve `True` si todos los caracteres alfabéticos de la cadena están en minúsculas.

## Métodos de Verificación `isX`

Python proporciona varios métodos `isX` para verificar el tipo de contenido de una cadena. Todos devuelven `True` si todos los caracteres de la cadena (y la cadena no está vacía) cumplen la condición, de lo contrario `False`.

- `str.isalpha()`: ¿Todos los caracteres son letras?
- `str.isdigit()`: ¿Todos los caracteres son dígitos (0-9)?
- `str.isalnum()`: ¿Todos los caracteres son alfanuméricos (letras o dígitos)?
- `str.isspace()`: ¿Todos los caracteres son espacios en blanco?
- `str.istitle()`: ¿La cadena está en formato título? (primera letra de cada palabra en mayúscula, el resto en minúscula).
- `str.isdecimal()`, str.isnumeric(), `str.isascii()`: Variantes para tipos de números o caracteres ASCII.

## Métodos `startswith()` y `endswith()`

Estos métodos verifican si una cadena comienza o termina con una subcadena específica.

- `str.startswith(prefijo[, inicio[, fin]])`: Devuelve `True` si la cadena comienza con el `prefijo` especificado.
- `str.endswith(sufijo[, inicio[, fin]])`: Devuelve `True` si la cadena termina con el `sufijo` especificado.

Puedes opcionalmente especificar un rango (`inicio`, `fin`) para la búsqueda.

## Métodos `join()` y `split()`

Estos son dos de los métodos de cadena más utilizados para trabajar con listas de cadenas.

- `str.join(iterable)`: Une los elementos de un iterable (donde los elementos son cadenas) en una sola cadena, utilizando la cadena en la que se llama el método como separador.
- `str.split([separador[, maxsplit]])`: Divide la cadena en una lista de subcadenas.
  - `separador`: (Opcional) El delimitador por el que dividir. Si se omite, divide por cualquier secuencia de espacios en blanco y elimina cadenas vacías.
  - `maxsplit`: (Opcional) El número máximo de divisiones a realizar.

## Justificación de Texto

Estos métodos devuelven una nueva cadena que es la original justificada a la izquierda, derecha o centrada, rellenando con un carácter (por defecto, espacio) hasta un ancho total especificado.

- `str.ljust(ancho[, caracter_relleno])`: Justifica a la izquierda.
- `str.rjust(ancho[, caracter_relleno])`: Justifica a la derecha.
- `str.center(ancho[, caracter_relleno])`: Centra el texto.

## Métodos para Eliminar Espacios

Estos métodos eliminan caracteres (por defecto, espacios en blanco) del inicio y/o final de una cadena.

- `str.strip([caracteres])`: Elimina caracteres del principio y del final de la cadena.
- `str.lstrip([caracteres])`: Elimina caracteres solo del principio (izquierda) de la cadena.
- `str.rstrip([caracteres])`: Elimina caracteres solo del final (derecha) de la cadena.

Si se proporciona el argumento `caracteres`, solo se eliminan esos caracteres específicos.

## `count()`

El método `count()` devuelve el número de veces que una subcadena específica aparece en la cadena.

```python
str.count(sub[, inicio[, fin]])
```

- `sub`: La subcadena a buscar.
- `inicio`, `fin`: (Opcional) Rango de índices donde buscar.

## `replace()`

El método replace() devuelve una nueva cadena donde todas las ocurrencias de una subcadena antigua son reemplazadas por una subcadena nueva.

```python
str.replace(antigua, nueva[, count])
```

- `antigua`: La subcadena a reemplazar.
- `nueva`: La subcadena por la que reemplazar.
- `count`: (Opcional) El número máximo de reemplazos a realizar. Si se omite, se reemplazan todas las ocurrencias.
