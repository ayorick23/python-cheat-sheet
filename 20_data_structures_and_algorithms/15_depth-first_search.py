# Reutilizamos la clase Grafo
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

def dfs(grafo, nodo_inicial):
    """
    Implementa el algoritmo de Búsqueda en Profundidad (DFS) de forma recursiva.
    Retorna la lista de nodos visitados en orden DFS.
    """
    if nodo_inicial not in grafo.adj:
        print(f"El nodo inicial '{nodo_inicial}' no existe en el grafo.")
        return []

    visitados = set()
    recorrido_dfs = []

    print(f"\n--- Iniciando DFS desde el nodo '{nodo_inicial}' ---")
    _dfs_recursivo(grafo, nodo_inicial, visitados, recorrido_dfs)
    
    print(f"\nOrden de recorrido DFS: {recorrido_dfs}")
    return recorrido_dfs

def _dfs_recursivo(grafo, nodo_actual, visitados, recorrido_dfs):
    visitados.add(nodo_actual)
    recorrido_dfs.append(nodo_actual)
    print(f"  Visitando: {nodo_actual}")

    for vecino in grafo.adj[nodo_actual]:
        if vecino not in visitados:
            _dfs_recursivo(grafo, vecino, visitados, recorrido_dfs)

print("--- Demostración de Búsqueda en Profundidad (DFS) ---")
mi_grafo_dfs = Grafo()
mi_grafo_dfs.agregar_arista("A", "B")
mi_grafo_dfs.agregar_arista("A", "C")
mi_grafo_dfs.agregar_arista("B", "D")
mi_grafo_dfs.agregar_arista("B", "E")
mi_grafo_dfs.agregar_arista("C", "F")
mi_grafo_dfs.agregar_arista("E", "G")
mi_grafo_dfs.agregar_arista("F", "H")

mi_grafo_dfs.imprimir_grafo()
dfs(mi_grafo_dfs, "A")