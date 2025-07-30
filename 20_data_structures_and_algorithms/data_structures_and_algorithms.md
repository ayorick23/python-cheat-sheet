# Data Structures

Las **estructuras de datos** son formas especializadas de organizar, procesar, recuperar y almacenar datos. Elegir la estructura de datos adecuada es vital para la eficiencia de tus algoritmos.

## Estructuras Nativas

- **Listas (`list`):** Colecciones ordenadas y mutables de elementos (pueden contener diferentes tipos de datos). Ideales para colecciones donde el orden y la mutabilidad son importantes.

  ```python
  mi_lista = [1, "hola", 3.14, True]
  mi_lista.append(5) # Añadir
  mi_lista[0] = 10   # Modificar
  ```

- **Tuplas (`tuple`):** Colecciones ordenadas e inmutables. Una vez creadas, no se pueden modificar. Útiles para datos que no deben cambiar o como claves de diccionario (si son inmutables).

  ```python
  mi_tupla = (1, "hola", 3.14)
  # mi_tupla[0] = 10 # Esto daría un error
  ```

- **Diccionarios (`dict`):** Colecciones desordenadas de pares clave-valor. Mutables. Optimizados para búsquedas rápidas por clave.

  ```python
  mi_diccionario = {"nombre": "Ana", "edad": 30}
  mi_diccionario["ciudad"] = "Madrid" # Añadir/Modificar
  print(mi_diccionario["nombre"])
  ```

- **Conjuntos (`set`):** Colecciones desordenadas de elementos únicos. Mutables. Útiles para operaciones matemáticas de conjuntos (unión, intersección) y para eliminar duplicados.

  ```python
  mi_set = {1, 2, 3, 2, 4} # {1, 2, 3, 4}
  mi_set.add(5)
  print(3 in mi_set) # True
  ```

## Arrays

En Python, la `list` nativa es muy versátil, pero no es un array estricto en el sentido de otros lenguajes (donde todos los elementos son del mismo tipo y se almacenan de forma contigua en memoria para mayor eficiencia). Python ofrece el módulo `array` para esto, útil cuando se necesita almacenar grandes cantidades de datos del mismo tipo de manera más eficiente en memoria que una lista.

### Características

- Almacenan solo elementos de un tipo específico (definido por un "código de tipo").
- Más eficientes en memoria que las listas para colecciones grandes de tipos homogéneos.
- Acceso por índice como las listas.

```python
import array

# Crear un array de enteros
mi_array = array.array('i', [1, 2, 3, 4, 5]) # 'i' indica enteros

# Acceder a elementos y realizar operaciones similares a las listas
primer_elemento = mi_array[0]
mi_array.append(6)
del mi_array[0]
```

## Linked List (_Listas Enlazadas_)

Una lista enlazada es una colección lineal de elementos de datos, donde cada elemento (llamado **nodo**) apunta al siguiente. A diferencia de los arrays, los elementos no se almacenan en ubicaciones de memoria contiguas.

### Características

- **Inserción/Eliminación eficiente:** Rápida, ya que solo hay que cambiar punteros, no reajustar elementos.
- **Acceso secuencial:** Para acceder a un elemento en particular, se debe recorrer la lista desde el principio hasta el elemento deseado (O(n)).
- **Uso de memoria:** Puede usar más memoria por elemento debido al almacenamiento de punteros.
- No es una estructura nativa de Python, pero se implementa comúnmente con clases.

### Tipos

- **Singly Linked List:** Cada nodo apunta solo al siguiente.
- **Doubly Linked List:** Cada nodo apunta al siguiente y al anterior.
- **Circular Linked List:** El último nodo apunta al primer nodo.

## Stack (_Pila_)

Una pila es una estructura de datos lineal que sigue el principio **LIFO** (_Last In, First Out - Último en Entrar, Primero en Salir_). Piensa en una pila de platos: el último plato que pones es el primero que quitas.

### Operaciones principales

- **`push`:** Añadir un elemento a la cima de la pila.
- **`pop`:** Eliminar y devolver el elemento de la cima de la pila.
- **`peek` (o `top`):** Ver el elemento de la cima sin eliminarlo.
- **`is_empty`:** Comprobar si la pila está vacía.
- **`size`:** Obtener el número de elementos.

**Implementación en Python:** Las listas de Python son excelentes para implementar pilas eficientemente.

## Queue (_Cola_)

Una cola es una estructura de datos lineal que sigue el principio **FIFO** (_First In, First Out - Primero en Entrar, Primero en Salir_). Piensa en una fila en un banco: la primera persona que llega es la primera en ser atendida.

### Operaciones principales

- **`enqueue`:** Añadir un elemento al final de la cola.
- **`dequeue`:** Eliminar y devolver el elemento del frente de la cola.
- **`front` (o `peek`):** Ver el elemento del frente sin eliminarlo.
- **`is_empty`:** Comprobar si la cola está vacía.
- **`size`:** Obtener el número de elementos.

**Implementación en Python:** Las listas pueden usarse, pero no son eficientes para `dequeue` (eliminar del principio) ya que desplaza todos los elementos (O(n)). El módulo `collections.deque` (double-ended queue) es mucho más eficiente para implementar colas.

## Hash Table (_Tabla Hash_)

Una tabla hash (implementada como diccionarios en Python) es una estructura de datos que implementa un array asociativo, es decir, mapea claves a valores. Utiliza una función hash para calcular un índice en un array de "buckets" o "ranuras", donde se almacenan los elementos.

### Características

- **Búsqueda, inserción y eliminación promedio O(1):** Extremadamente rápidas en el caso promedio.
- **Resolución de colisiones:** Manejan cuando dos claves diferentes producen el mismo hash (ej. encadenamiento, sondeo lineal).
- Python implementa sus diccionarios como tablas hash optimizadas.

## Tree (_Árbol_)

Una estructura de datos de árbol es una colección de nodos donde cada nodo tiene cero o más nodos hijos, y solo un padre (excepto el nodo raíz, que no tiene padre). Es una estructura jerárquica no lineal.

### Características

- Jerárquicas.
- Amplia variedad de tipos (árboles binarios, árboles de búsqueda binaria, AVL, B-Trees, etc.).
- Eficientes para búsqueda, inserción y eliminación en promedio (dependiendo del tipo de árbol).

## Graph (Grafo)

Un grafo es una estructura de datos no lineal que consiste en un conjunto de nodos (o vértices) y un conjunto de aristas (o lados) que conectan pares de nodos.

### Características

- Pueden ser dirigidos (las aristas tienen una dirección) o no dirigidos.
- Pueden ser ponderados (las aristas tienen un valor o "peso") o no ponderados.
- Representan relaciones complejas (ej. redes sociales, rutas de carreteras).

**Implementación en Python:** Generalmente se usan diccionarios o listas de adyacencia.

# Algoritmos Fundamentales

Un algoritmo es un conjunto finito de instrucciones bien definidas y no ambiguas para resolver un problema o lograr un objetivo. La eficiencia de un algoritmo se mide a menudo por su complejidad de tiempo (cuánto tarda en ejecutarse) y complejidad de espacio (cuánta memoria consume), generalmente expresada en notación O (Big O notation).

## Algoritmos de Búsqueda

### Búsqueda Lineal (_Sequential Search_)

Recorre una colección elemento por elemento hasta encontrar el objetivo o llegar al final.

- **Complejidad:** O(n) - En el peor caso, debe revisar todos los elementos.
- **Cuándo usar:** Para colecciones pequeñas o desordenadas.

### Búsqueda Binaria (_Binary Search_)

Requiere que la colección esté ordenada. Divide repetidamente por la mitad la porción de la lista donde el objetivo podría estar, eliminando la mitad no relevante en cada paso.

- **Complejidad:** O(log n) - Mucho más rápido que la búsqueda lineal para listas grandes.
- **Cuándo usar:** Para colecciones grandes y ordenadas.

## Algoritmos de Ordenamiento

### Ordenamiento de Burbuja (_Bubble Sort_)

Descripción: Un algoritmo simple que repetidamente recorre la lista, compara elementos adyacentes y los intercambia si están en el orden incorrecto. Las pasadas a través de la lista se repiten hasta que no se necesitan más intercambios, lo que indica que la lista está ordenada.

- **Complejidad:** O($n^2$) - Ineficiente para listas grandes.
- **Cuándo usar:** Principalmente para propósitos educativos debido a su simplicidad.

### Ordenamiento por Inserción (_Insertion Sort_)

Construye la lista final ordenada un elemento a la vez. Recorre la lista, tomando cada elemento y "insertándolo" en su posición correcta en la sublista ya ordenada.

- **Complejidad:** O($n^2$) en el peor y promedio caso, O(n) en el mejor caso (lista ya ordenada).
- **Cuándo usar:** Para listas pequeñas o listas que ya están casi ordenadas.

### Ordenamiento por Mezcla (_Merge Sort_)

Un algoritmo de "divide y vencerás". Divide la lista recursivamente en dos mitades hasta que cada sublista tenga un solo elemento (que por definición está ordenada). Luego, fusiona (mezcla) las sublistas ordenadas para producir listas ordenadas más grandes.

- **Complejidad:** O(n log n) - Mucho más eficiente para listas grandes que los algoritmos O($n^2$).
- **Cuándo usar:** Para ordenar listas grandes de manera eficiente. Es un algoritmo estable (mantiene el orden relativo de elementos iguales).

### Ordenamiento Rápido (_Quick Sort_)

También es un algoritmo de "divide y vencerás". Selecciona un elemento de la lista llamado pivote. Luego, particiona la lista en dos sublistas: elementos menores que el pivote y elementos mayores que el pivote. Recursivamente ordena las sublistas.

- **Complejidad:** O(n log n) en el caso promedio, O($n^2$) en el peor caso (mala elección del pivote).
- **Cuándo usar:** Muy eficiente en la práctica para listas grandes, a menudo más rápido en promedio que Merge Sort, aunque Merge Sort tiene una complejidad de peor caso garantizada de O(n log n). Es un algoritmo in situ (no requiere mucha memoria extra).

## Algoritmos de Recorrido de Grafos/Árboles

### Búsqueda en Amplitud (Breadth-First Search - BFS)

Recorre un grafo (o árbol) nivel por nivel. Empieza en un nodo raíz, luego visita todos sus vecinos, luego todos los vecinos de sus vecinos, y así sucesivamente.

- **Utiliza una cola (Queue)** para gestionar los nodos a visitar.
- **Complejidad:** O(V + E) donde V es el número de vértices y E es el número de aristas.
- **Cuándo usar:** Encontrar el camino más corto en un grafo no ponderado, rastrear niveles de un árbol.

### Búsqueda en Profundidad (Depth-First Search - DFS)

Recorre un grafo (o árbol) yendo tan profundo como sea posible a lo largo de cada rama antes de retroceder.

- **Utiliza una pila (Stack)** implícita (con recursión) o explícita.
- **Complejidad:** O(V + E) donde V es el número de vértices y E es el número de aristas.
- **Cuándo usar:** Detección de ciclos, ordenamiento topológico, encontrar componentes conectados.
