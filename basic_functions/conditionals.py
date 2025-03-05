def isAdult(age):
    #Verifica si la edad corresponde a un adulto
    return "Adulto" if age >= 18 else "Menor de edad"

if __name__ == "__main__":
    print(isAdult(20))
    print(isAdult(15))