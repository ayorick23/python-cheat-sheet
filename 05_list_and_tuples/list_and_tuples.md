# List and Tuples

## Listas

Las **listas** son colecciones ordenadas y mutables (_es decir, pueden modificarse después de su creación_) de ítems. Los ítems pueden ser de cualquier tipo de dato y no es necesario que sean del mismo tipo. Se definen utilizando corchetes `[]`.

```python
mi_lista = [item1, item2, item3, ...]
```

### Índices y Slicing (_Rebanado_)

Las listas son secuencias, lo que significa que sus elementos están ordenados y se pueden acceder a ellos mediante índices.

1. **Indexación:** Cada elemento en una lista tiene una posición numérica, comenzando desde 0 para el primer elemento. Los índices negativos cuentan desde el final de la lista, con -1 siendo el último elemento.

   **Sintaxis:** `mi_lista[indice]`

2. **Slicing (Rebanado):** Permite extraer una subsección (una "rebanada") de la lista. Crea una nueva lista.

   **Sintaxis:** `mi_lista[inicio:fin:paso]`

   - `inicio`: (Opcional) Índice donde comienza el rebanado (incluido). Por defecto es `0`.
   - `fin`: (Opcional) Índice donde termina el rebanado (excluido). Por defecto es el final de la lista.
   - `paso`: (Opcional) Intervalo entre los elementos (por defecto es `1`). Puede ser negativo para rebanar hacia atrás.

### Concatenación y Replicación

- **Concatenación (`+`)**: Une dos o más listas para crear una nueva lista.
- **Replicación (`*`)**: Crea una nueva lista repitiendo los elementos de una lista existente un número específico de veces.

### Uso del Bucle `for` con `enumerate` y `zip`

- `for` con `enumerate()`: Permite iterar sobre una lista (u otro iterable) obteniendo tanto el índice como el valor de cada elemento.

```python
for indice, valor in enumerate(mi_lista):
    # ...
```

- `for` con `zip()`: Permite iterar simultáneamente sobre múltiples listas (u otros iterables), emparejando elementos correspondientes. La iteración se detiene cuando el iterable más corto se agota.

```python
for item1, item2, ... in zip(lista1, lista2, ...):
    # ...
```

### Métodos para Modificar Listas

Las listas son mutables, lo que significa que puedes añadir, eliminar o modificar elementos directamente.

- `append(item)`: Añade un elemento al final de la lista.
- `insert(indice, item)`: Inserta un elemento en una posición específica de la lista.
- `del sentencia`: Elimina un elemento por su índice o un slice de la lista.
- `remove(valor)`: Elimina la primera aparición de un valor específico de la lista. Si el valor no existe, lanza un ValueError.
- `pop([indice])`: Elimina y devuelve el elemento en el índice dado. Si no se proporciona un índice, elimina y devuelve el último elemento.

### Ordenamiento de Listas

Python ofrece dos formas principales de ordenar listas:

- **Método `list.sort()`:** Ordena la lista en su lugar (modifica la lista original) y no devuelve nada (`None`).
- **Función built-in `sorted()`:** Crea y devuelve una nueva lista ordenada, dejando la lista original sin cambios.

Ambos aceptan argumentos opcionales:

- `reverse=True`: Para ordenar en orden descendente.
- `key=funcion`: Una función de un argumento para personalizar el criterio de ordenación (similar a `max()`/`min()`).

## Tuplas

Las **tuplas** son colecciones ordenadas e inmutables de ítems. Una vez creadas, sus elementos no pueden ser modificados, añadidos o eliminados. Se definen utilizando paréntesis `()`.

```python
mi_tupla = (item1, item2, item3, ...)
```

- Para una tupla de un solo elemento, es crucial añadir una coma: (`item,`). Sin la coma, Python lo interpreta como una expresión entre paréntesis.

### Características Clave

- **Inmutabilidad:** Su contenido no puede cambiar. Esto las hace ideales para datos que no deben ser alterados (ej. coordenadas, claves de diccionario compuestas).
- **Ordenadas:** Los elementos mantienen su orden de inserción.
- **Permiten duplicados:** Pueden contener elementos repetidos.
- **Heterogéneas:** Pueden contener elementos de diferentes tipos de datos.

### Conversión entre Listas y Tuplas

Puedes convertir una lista en una tupla y viceversa utilizando las funciones `list()` y `tuple()`.

```python
mi_tupla = tuple(mi_lista)
mi_lista = list(mi_tupla)
```
