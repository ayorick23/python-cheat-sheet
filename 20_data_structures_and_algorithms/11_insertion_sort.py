def insertion_sort(lista):
    """Implementa el algoritmo de ordenamiento por inserción."""
    n = len(lista)
    print(f"Lista original: {lista}")

    for i in range(1, n): # Empezamos desde el segundo elemento
        valor_actual = lista[i]
        posicion = i
        print(f"\n--- Procesando elemento: {valor_actual} (en índice {i}) ---")

        # Mueve los elementos de la sublista ordenada que son mayores que valor_actual
        # una posición adelante de su posición actual
        while posicion > 0 and lista[posicion - 1] > valor_actual:
            lista[posicion] = lista[posicion - 1]
            posicion -= 1
            print(f"  Desplazando... Lista actual: {lista}")
        
        lista[posicion] = valor_actual # Inserta el valor actual en su posición correcta
        print(f"  Insertado {valor_actual} en índice {posicion}. Lista: {lista}")

    print(f"\nLista ordenada: {lista}")
    return lista

print("--- Demostración de Ordenamiento por Inserción ---")
mi_lista = [12, 11, 13, 5, 6]
insertion_sort(mi_lista)

print("\n--- Otro ejemplo ---")
otra_lista = [5, 1, 4, 2, 8]
insertion_sort(otra_lista)