from collections import deque

print("--- Demostración de Queue (Cola) con collections.deque ---")

class Queue:
    def __init__(self):
        # deque es altamente optimizado para añadir/eliminar en ambos extremos
        self._items = deque()

    def is_empty(self):
        """Retorna True si la cola está vacía."""
        return len(self._items) == 0

    def enqueue(self, item):
        """Añade un elemento al final de la cola."""
        self._items.append(item)
        print(f"Enqueue: '{item}' (Cola actual: {list(self._items)})")

    def dequeue(self):
        """
        Elimina y retorna el elemento del frente de la cola.
        Lanza IndexError si la cola está vacía.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self._items.popleft() # Eliminar del principio (izquierda)
        print(f"Dequeue: '{item}' (Cola actual: {list(self._items)})")
        return item

    def front(self):
        """
        Retorna el elemento del frente sin eliminarlo.
        Lanza IndexError si la cola está vacía.
        """
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self._items[0]

    def size(self):
        """Retorna el número de elementos en la cola."""
        return len(self._items)

    def __str__(self):
        """Representación en cadena de la cola."""
        return f"Cola: {list(self._items)}"

mi_cola = Queue()
print(f"¿Cola vacía? {mi_cola.is_empty()}") # True

mi_cola.enqueue("cliente 1")
mi_cola.enqueue("cliente 2")
mi_cola.enqueue("cliente 3")

print(f"Tamaño de la cola: {mi_cola.size()}") # 3
print(f"Elemento al frente (front): {mi_cola.front()}") # cliente 1

cliente_atendido = mi_cola.dequeue() # cliente 1
cliente_atendido = mi_cola.dequeue() # cliente 2

print(f"¿Cola vacía? {mi_cola.is_empty()}") # False
print(f"Tamaño de la cola: {mi_cola.size()}") # 1

mi_cola.enqueue("cliente 4")
print(mi_cola) # Cola: ['cliente 3', 'cliente 4']

try:
    mi_cola.dequeue() # cliente 3
    mi_cola.dequeue() # cliente 4
    mi_cola.dequeue() # Esto debería dar un error
except IndexError as e:
    print(f"Error al hacer dequeue en cola vacía: {e}")