class NodoArbol:
    def __init__(self, clave):
        self.clave = clave
        self.izquierda = None
        self.derecha = None

class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        """Inserta una nueva clave en el BST."""
        if self.raiz is None:
            self.raiz = NodoArbol(clave)
            print(f"Insertado {clave} como raíz.")
        else:
            self._insertar_recursivo(self.raiz, clave)

    def _insertar_recursivo(self, nodo_actual, clave):
        if clave < nodo_actual.clave:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = NodoArbol(clave)
                print(f"Insertado {clave} a la izquierda de {nodo_actual.clave}.")
            else:
                self._insertar_recursivo(nodo_actual.izquierda, clave)
        elif clave > nodo_actual.clave:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = NodoArbol(clave)
                print(f"Insertado {clave} a la derecha de {nodo_actual.clave}.")
            else:
                self._insertar_recursivo(nodo_actual.derecha, clave)
        else:
            print(f"Clave {clave} ya existe en el árbol.")

    def buscar(self, clave):
        """Busca una clave en el BST y retorna True si la encuentra, False en caso contrario."""
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, nodo_actual, clave):
        if nodo_actual is None:
            return False
        if nodo_actual.clave == clave:
            return True
        elif clave < nodo_actual.clave:
            return self._buscar_recursivo(nodo_actual.izquierda, clave)
        else:
            return self._buscar_recursivo(nodo_actual.derecha, clave)

    def recorrido_en_orden(self):
        """Realiza un recorrido en orden (izquierda, raíz, derecha) e imprime los nodos."""
        elementos = []
        self._recorrido_en_orden_recursivo(self.raiz, elementos)
        print("Recorrido en Orden:", " ".join(map(str, elementos)))

    def _recorrido_en_orden_recursivo(self, nodo_actual, elementos):
        if nodo_actual:
            self._recorrido_en_orden_recursivo(nodo_actual.izquierda, elementos)
            elementos.append(nodo_actual.clave)
            self._recorrido_en_orden_recursivo(nodo_actual.derecha, elementos)

print("--- Demostración de Árbol de Búsqueda Binaria (BST) ---")
mi_bst = BST()
mi_bst.insertar(50)
mi_bst.insertar(30)
mi_bst.insertar(70)
mi_bst.insertar(20)
mi_bst.insertar(40)
mi_bst.insertar(60)
mi_bst.insertar(80)
mi_bst.insertar(50) # Intentar insertar duplicado

mi_bst.recorrido_en_orden() # Debería imprimir en orden ascendente: 20 30 40 50 60 70 80

print(f"¿Buscar 40? {mi_bst.buscar(40)}") # True
print(f"¿Buscar 90? {mi_bst.buscar(90)}") # False