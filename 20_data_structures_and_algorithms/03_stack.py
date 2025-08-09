class Stack:
    def __init__(self):
        self._items = [] # Usamos una lista de Python como base

    def is_empty(self):
        """Retorna True si la pila está vacía, False en caso contrario."""
        return len(self._items) == 0

    def push(self, item):
        """Añade un elemento a la cima de la pila."""
        self._items.append(item)
        print(f"Push: '{item}' (Pila actual: {self._items})")

    def pop(self):
        """
        Elimina y retorna el elemento de la cima de la pila.
        Lanza IndexError si la pila está vacía.
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        item = self._items.pop()
        print(f"Pop: '{item}' (Pila actual: {self._items})")
        return item

    def peek(self):
        """
        Retorna el elemento de la cima sin eliminarlo.
        Lanza IndexError si la pila está vacía.
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]

    def size(self):
        """Retorna el número de elementos en la pila."""
        return len(self._items)

    def __str__(self):
        """Representación en cadena de la pila."""
        return f"Pila: {self._items}"

print("--- Demostración de Stack (Pila) ---")
mi_pila = Stack()

print(f"¿Pila vacía? {mi_pila.is_empty()}") # True

mi_pila.push("libro 1")
mi_pila.push("libro 2")
mi_pila.push("libro 3")

print(f"Tamaño de la pila: {mi_pila.size()}") # 3
print(f"Elemento en la cima (peek): {mi_pila.peek()}") # libro 3

elemento_sacado = mi_pila.pop() # libro 3
elemento_sacado = mi_pila.pop() # libro 2

print(f"¿Pila vacía? {mi_pila.is_empty()}") # False
print(f"Tamaño de la pila: {mi_pila.size()}") # 1

mi_pila.push("libro 4")
print(mi_pila) # Pila: ['libro 1', 'libro 4']

try:
    mi_pila.pop() # libro 4
    mi_pila.pop() # libro 1
    mi_pila.pop() # Esto debería dar un error
except IndexError as e:
    print(f"Error al hacer pop en pila vacía: {e}")