class Grafo:
    def __init__(self):
        # Usamos un diccionario donde la clave es un nodo y el valor es una lista de sus vecinos.
        self.adj = {} # Lista de adyacencia

    def agregar_vertice(self, vertice):
        """Añade un vértice al grafo si no existe."""
        if vertice not in self.adj:
            self.adj[vertice] = []
            print(f"Agregado vértice: {vertice}")

    def agregar_arista(self, u, v):
        """
        Añade una arista entre dos vértices (u y v).
        Para un grafo no dirigido, añadimos la conexión en ambas direcciones.
        """
        self.agregar_vertice(u) # Asegura que los vértices existan
        self.agregar_vertice(v)

        if v not in self.adj[u]:
            self.adj[u].append(v)
            print(f"Agregada arista: {u} -> {v}")
        if u not in self.adj[v]: # Para grafos no dirigidos
            self.adj[v].append(u)
            print(f"Agregada arista: {v} -> {u}")

    def imprimir_grafo(self):
        """Imprime la representación del grafo."""
        print("--- Representación del Grafo ---")
        for vertice, vecinos in self.adj.items():
            print(f"{vertice}: {vecinos}")

    def obtener_vecinos(self, vertice):
        """Retorna la lista de vecinos de un vértice dado."""
        return self.adj.get(vertice, [])

print("--- Demostración de Grafo (no dirigido) ---")
mi_grafo = Grafo()

mi_grafo.agregar_arista("A", "B")
mi_grafo.agregar_arista("A", "C")
mi_grafo.agregar_arista("B", "D")
mi_grafo.agregar_arista("C", "E")
mi_grafo.agregar_arista("D", "E")
mi_grafo.agregar_arista("F", "G") # Grafo desconectado

mi_grafo.imprimir_grafo()

print(f"\nVecinos de 'A': {mi_grafo.obtener_vecinos('A')}")
print(f"Vecinos de 'E': {mi_grafo.obtener_vecinos('E')}")
print(f"Vecinos de 'Z' (no existe): {mi_grafo.obtener_vecinos('Z')}")