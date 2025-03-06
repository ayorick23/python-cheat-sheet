#Factorial de un numero
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

#Fibonacci recursivo
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)