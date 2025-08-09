# algoritmo_bfs.py
from collections import deque

# Reutilizamos la clase Grafo del ejemplo de estructuras de datos
class Grafo:
    def __init__(self):
        self.adj = {} # Lista de adyacencia

    def agregar_vertice(self, vertice):
        if vertice not in self.adj:
            self.adj[vertice] = []

    def agregar_arista(self, u, v):
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if u not in self.adj[v]:
            self.adj[v].append(u)

    def imprimir_grafo(self):
        print("--- Representación del Grafo ---")
        for vertice, vecinos in self.adj.items():
            print(f"{vertice}: {vecinos}")

def bfs(grafo, nodo_inicial):
    """
    Implementa el algoritmo de Búsqueda en Amplitud (BFS).
    Retorna la lista de nodos visitados en orden BFS.
    """
    if nodo_inicial not in grafo.adj:
        print(f"El nodo inicial '{nodo_inicial}' no existe en el grafo.")
        return []

    visitados = set()
    cola = deque()

    visitados.add(nodo_inicial)
    cola.append(nodo_inicial)
    
    recorrido_bfs = []

    print(f"\n--- Iniciando BFS desde el nodo '{nodo_inicial}' ---")
    while cola:
        nodo_actual = cola.popleft() # Saca el primero (FIFO)
        recorrido_bfs.append(nodo_actual)
        print(f"  Visitando: {nodo_actual}")

        for vecino in grafo.adj[nodo_actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
                print(f"    Añadiendo a cola: {vecino}")
    
    print(f"\nOrden de recorrido BFS: {recorrido_bfs}")
    return recorrido_bfs

print("--- Demostración de Búsqueda en Amplitud (BFS) ---")
mi_grafo_bfs = Grafo()
mi_grafo_bfs.agregar_arista("A", "B")
mi_grafo_bfs.agregar_arista("A", "C")
mi_grafo_bfs.agregar_arista("B", "D")
mi_grafo_bfs.agregar_arista("B", "E")
mi_grafo_bfs.agregar_arista("C", "F")
mi_grafo_bfs.agregar_arista("E", "G")
mi_grafo_bfs.agregar_arista("F", "H")

mi_grafo_bfs.imprimir_grafo()
bfs(mi_grafo_bfs, "A")