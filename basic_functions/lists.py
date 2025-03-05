def removeDuplicates(lst):
    #Elimina duplicados de una lista
    return list(set(lst))

def findMax(lst):
    #Devuelve el numero maximo de una lista
    return max(lst) if lst else None

def findMin(lst):
    #Devuelve el numero minimo de una lista
    return min(lst) if lst else None

if __name__ == "__main__":
    print(removeDuplicates([1, 2, 2, 3, 3, 3, 4, 5]))
    print(findMax([10, 20, 5, 30]))
    print(findMin([1, 5, 87, 3]))