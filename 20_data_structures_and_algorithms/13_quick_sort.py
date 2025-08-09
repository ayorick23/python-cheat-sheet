def quick_sort(lista):
    """Implementa el algoritmo de ordenamiento rápido (Quick Sort)."""
    if len(lista) <= 1:
        return lista

    # Elegir un pivote (aquí elegimos el elemento del medio para simplicidad)
    # Una mejor elección del pivote es crucial para el rendimiento.
    pivote = lista[len(lista) // 2]
    
    print(f"\n--- Ordenando: {lista}, Pivote: {pivote} ---")

    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    print(f"  Menores: {menores}")
    print(f"  Iguales: {iguales}")
    print(f"  Mayores: {mayores}")

    # Llamadas recursivas
    resultado = quick_sort(menores) + iguales + quick_sort(mayores)
    print(f"  Resultado de ordenamiento parcial: {resultado}")
    return resultado

print("--- Demostración de Ordenamiento Rápido (Quick Sort) ---")
mi_lista = [3, 6, 8, 10, 1, 2, 1]
lista_ordenada = quick_sort(mi_lista)
print(f"\nLista original: {mi_lista}")
print(f"Lista final ordenada: {lista_ordenada}")

print("\n--- Otro ejemplo ---")
otra_lista = [10, 7, 8, 9, 1, 5]
otra_lista_ordenada = quick_sort(otra_lista)
print(f"Lista final ordenada: {otra_lista_ordenada}")