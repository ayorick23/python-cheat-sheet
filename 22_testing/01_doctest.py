def sumar(a, b):
    """
    Suma dos números y retorna el resultado.

    >>> sumar(2, 3)
    5
    >>> sumar(-1, 1)
    0
    >>> sumar(1.5, 2.5)
    4.0
    """
    return a + b

def concatenar(cadena1, cadena2):
    """
    Concatena dos cadenas.

    >>> concatenar("Hola", " Mundo")
    'Hola Mundo'
    """
    return cadena1 + cadena2

# Para ejecutar las pruebas desde el script
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
# Si todas las pruebas pasan, no habrá salida. Si alguna falla, verás un informe detallado del error.