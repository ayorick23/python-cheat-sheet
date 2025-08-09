class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None # Puntero al siguiente nodo

class LinkedList:
    def __init__(self):
        self.cabeza = None # El primer nodo de la lista

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_al_principio(self, dato):
        """Agrega un nuevo nodo al principio de la lista."""
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        print(f"Agregado '{dato}' al principio.")

    def agregar_al_final(self, dato):
        """Agrega un nuevo nodo al final de la lista."""
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            print(f"Agregado '{dato}' al final (lista estaba vacía).")
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
        print(f"Agregado '{dato}' al final.")

    def insertar_despues_de(self, dato_existente, nuevo_dato):
        """Inserta un nuevo nodo después de un nodo con un dato específico."""
        actual = self.cabeza
        while actual and actual.dato != dato_existente:
            actual = actual.siguiente
        if actual:
            nuevo_nodo = Nodo(nuevo_dato)
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            print(f"Insertado '{nuevo_dato}' después de '{dato_existente}'.")
        else:
            print(f"ERROR: '{dato_existente}' no encontrado en la lista.")

    def eliminar_nodo(self, dato):
        """Elimina el primer nodo que contenga el dato especificado."""
        if self.esta_vacia():
            print("Lista vacía, no se puede eliminar.")
            return

        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            print(f"Eliminado '{dato}' de la cabeza.")
            return

        actual = self.cabeza
        anterior = None
        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente

        if actual:
            anterior.siguiente = actual.siguiente
            print(f"Eliminado '{dato}'.")
        else:
            print(f"ERROR: '{dato}' no encontrado para eliminar.")

    def imprimir_lista(self):
        """Imprime todos los elementos de la lista."""
        if self.esta_vacia():
            print("Lista: Vacía")
            return
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print("Lista:", " -> ".join(elementos))

print("--- Demostración de Lista Enlazada Simple (Singly Linked List) ---")
mi_lista_enlazada = LinkedList()
mi_lista_enlazada.imprimir_lista()

mi_lista_enlazada.agregar_al_principio(10)
mi_lista_enlazada.agregar_al_final(30)
mi_lista_enlazada.agregar_al_principio(5)
mi_lista_enlazada.imprimir_lista() # Salida esperada: 5 -> 10 -> 30

mi_lista_enlazada.insertar_despues_de(10, 20)
mi_lista_enlazada.imprimir_lista() # Salida esperada: 5 -> 10 -> 20 -> 30

mi_lista_enlazada.eliminar_nodo(10)
mi_lista_enlazada.imprimir_lista() # Salida esperada: 5 -> 20 -> 30

mi_lista_enlazada.eliminar_nodo(5)
mi_lista_enlazada.imprimir_lista() # Salida esperada: 20 -> 30

mi_lista_enlazada.eliminar_nodo(40) # Intentar eliminar algo que no existe
mi_lista_enlazada.eliminar_nodo(30)
mi_lista_enlazada.eliminar_nodo(20)
mi_lista_enlazada.imprimir_lista() # Salida esperada: Lista: Vacía