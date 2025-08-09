# algoritmo_busqueda_lineal.py

def busqueda_lineal(lista, objetivo):
    """
    Implementa el algoritmo de búsqueda lineal.
    Retorna el índice del objetivo si se encuentra, de lo contrario -1.
    """
    print(f"Buscando '{objetivo}' en {lista} (Búsqueda Lineal)")
    for i in range(len(lista)):
        if lista[i] == objetivo:
            print(f"Encontrado '{objetivo}' en el índice {i}.")
            return i
    print(f"'{objetivo}' no encontrado en la lista.")
    return -1

print("--- Demostración de Búsqueda Lineal ---")
mi_lista = [4, 2, 7, 1, 9, 5, 3]

busqueda_lineal(mi_lista, 9)  # Encontrado en índice 4
busqueda_lineal(mi_lista, 6)  # No encontrado
busqueda_lineal(mi_lista, 4)  # Encontrado en índice 0