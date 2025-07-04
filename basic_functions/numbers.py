def isEven(num):
    #Devuelve True si el numero es par
    return num % 2 == 0

def factorial(num):
    #Calcula el factorial de un numero
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

if __name__ == "__main__":
    print(isEven(20))
    print(factorial(23))