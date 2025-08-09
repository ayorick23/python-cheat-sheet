# algoritmo_bubble_sort.py

def bubble_sort(lista):
    """Implementa el algoritmo de ordenamiento de burbuja."""
    n = len(lista)
    print(f"Lista original: {lista}")

    for i in range(n - 1): # Bucle para las pasadas
        intercambiado = False # Bandera para optimización
        print(f"\n--- Pasada {i+1} ---")
        for j in range(n - 1 - i): # Bucle para comparaciones en la pasada actual
            print(f"  Comparando {lista[j]} y {lista[j+1]}")
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] # Intercambio
                intercambiado = True
                print(f"    Intercambio! Lista ahora: {lista}")
            else:
                print(f"    No se necesita intercambio. Lista: {lista}")
        
        if not intercambiado:
            print("No hubo intercambios en esta pasada, la lista está ordenada.")
            break # Si no hubo intercambios en una pasada, la lista ya está ordenada
    print(f"\nLista ordenada: {lista}")
    return lista

print("--- Demostración de Ordenamiento de Burbuja ---")
mi_lista = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(mi_lista)

print("\n--- Otro ejemplo ---")
otra_lista = [5, 1, 4, 2, 8]
bubble_sort(otra_lista)