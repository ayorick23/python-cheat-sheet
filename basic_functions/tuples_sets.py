def countOccurrences(tpl, item):
    #Cuenta cuantas veces aparece un elemento en una tupla
    return tpl.count(item)

def unionSets(set1, set2):
    #Devuelve la union de dos conjuntos
    return set1 | set2

if __name__ == "__main__":
    print(countOccurrences((1, 2, 3, 1, 1, 4), 1))
    print(unionSets({1, 2, 3}, {3, 4, 5}))