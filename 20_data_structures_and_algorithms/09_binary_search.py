# algoritmo_busqueda_binaria.py

def busqueda_binaria(lista, objetivo):
    """
    Implementa el algoritmo de búsqueda binaria (iterativo).
    Requiere que la lista esté ordenada.
    Retorna el índice del objetivo si se encuentra, de lo contrario -1.
    """
    izquierda = 0
    derecha = len(lista) - 1
    print(f"Buscando '{objetivo}' en {lista} (Búsqueda Binaria)")

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        print(f"  Analizando sub-lista: {lista[izquierda:derecha+1]}, medio: {valor_medio}")

        if valor_medio == objetivo:
            print(f"Encontrado '{objetivo}' en el índice {medio}.")
            return medio
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else: # valor_medio > objetivo
            derecha = medio - 1
    print(f"'{objetivo}' no encontrado en la lista.")
    return -1

print("--- Demostración de Búsqueda Binaria ---")
mi_lista_ordenada = [10, 20, 30, 40, 50, 60, 70, 80, 90]

busqueda_binaria(mi_lista_ordenada, 30) # Encontrado en índice 2
print("-" * 30)
busqueda_binaria(mi_lista_ordenada, 85) # No encontrado
print("-" * 30)
busqueda_binaria(mi_lista_ordenada, 10) # Encontrado en índice 0
print("-" * 30)
busqueda_binaria(mi_lista_ordenada, 90) # Encontrado en índice 8