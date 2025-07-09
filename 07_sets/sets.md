# Sets

Los conjuntos son mutables (puedes añadir o eliminar elementos) y se definen utilizando llaves `{}` (similar a los diccionarios, pero sin pares clave-valor) o la función `set()`.

```python
mi_conjunto = {item1, item2, item3, ...}
conjunto_vacio = set() # Importante: {} crea un diccionario vacío, no un conjunto vacío.
```

## Inicialización, Duplicados e Índices

1. **Inicialización:** Puedes crear un conjunto a partir de una lista, tupla o directamente con llaves.
2. **Manejo de Duplicados:** Una característica clave de los conjuntos es que no permiten elementos duplicados. Si intentas añadir un elemento que ya existe, simplemente se ignora.
3. **Manejo de Índices:** Los conjuntos son desordenados, lo que significa que no mantienen un orden específico de los elementos y, por lo tanto, no soportan indexación ni slicing como las listas o tuplas.

## Métodos para Modificar Conjuntos

- `set.add(elemento)`: Añade un único elemento al conjunto. Si el elemento ya existe, no hace nada.
- `set.update(iterable)`: Añade múltiples elementos al conjunto. El argumento puede ser cualquier iterable (lista, tupla, otro conjunto, etc.). Los elementos duplicados se ignoran.
- `set.remove(elemento)`: Elimina el elemento especificado del conjunto. Si el elemento no existe, lanza un `KeyError`.
- `set.discard(elemento)`: Elimina el elemento especificado del conjunto. Si el elemento no existe, no hace nada (no lanza un error).

## Operaciones de Conjuntos

Estas operaciones son la razón principal para usar conjuntos, ya que son muy eficientes y se basan en la teoría de conjuntos.

- **`set.union(otro_set, ...)` / Operador `|`:** Devuelve un nuevo conjunto con todos los elementos de ambos (o más) conjuntos, sin duplicados.
- **`set.intersection(otro_set, ...)` / Operador `&`:** Devuelve un nuevo conjunto con solo los elementos comunes a ambos (o más) conjuntos.
- **`set.difference(otro_set, ...)` / Operador `-`:** Devuelve un nuevo conjunto con los elementos del primer conjunto que no están en el segundo (o subsiguientes).
- **`set.symmetric_difference(otro_set)` / Operador `^`:** Devuelve un nuevo conjunto con todos los elementos que están en uno de los conjuntos, pero no en ambos (elementos únicos de cada conjunto).
