def mergeDicts(dict1, dict2):
    #Combina dos diccionarios
    return {**dict1, **dict2}

def getKeys(dictionary):
    #Devuelve una lista con las claves del diccionario
    return list(dictionary.keys())

if __name__ == "__main__":
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    
    print(mergeDicts(dict1, dict2))
    print(getKeys(dict2))