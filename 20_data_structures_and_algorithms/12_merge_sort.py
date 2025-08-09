def merge_sort(lista):
    """Implementa el algoritmo de ordenamiento por mezcla (Merge Sort)."""
    if len(lista) <= 1:
        return lista # Una lista con 0 o 1 elemento ya está ordenada

    print(f"Dividiendo: {lista}")
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    # Llamadas recursivas para dividir
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    # Fusionar las dos mitades ordenadas
    return fusionar(izquierda, derecha)

def fusionar(izquierda, derecha):
    """Fusiona dos listas ordenadas en una sola lista ordenada."""
    resultado = []
    i = 0 # Índice para la lista izquierda
    j = 0 # Índice para la lista derecha

    print(f"  Fusionando Izquierda: {izquierda} y Derecha: {derecha}")

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Añadir los elementos restantes (si los hay)
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    print(f"  Resultado de la fusión: {resultado}")
    return resultado

print("--- Demostración de Ordenamiento por Mezcla (Merge Sort) ---")
mi_lista = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = merge_sort(mi_lista)
print(f"\nLista original: {mi_lista}") # Nota: La lista original no se modifica si no se reasigna.
print(f"Lista final ordenada: {lista_ordenada}")

print("\n--- Otro ejemplo ---")
otra_lista = [5, 1, 4, 2, 8]
otra_lista_ordenada = merge_sort(otra_lista)
print(f"Lista final ordenada: {otra_lista_ordenada}")