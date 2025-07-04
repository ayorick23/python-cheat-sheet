# Ver el tipo de diferentes variables
entero = 10
flotante = 3.14
cadena = "Hola"
lista = [1, 2, 3]
booleano = True
ninguno = None

print(f"El tipo de {entero} es: {type(entero)}")       # Salida: <class 'int'>
print(f"El tipo de {flotante} es: {type(flotante)}")     # Salida: <class 'float'>
print(f"El tipo de '{cadena}' es: {type(cadena)}")     # Salida: <class 'str'>
print(f"El tipo de {lista} es: {type(lista)}")       # Salida: <class 'list'>
print(f"El tipo de {booleano} es: {type(booleano)}")   # Salida: <class 'bool'>
print(f"El tipo de {ninguno} es: {type(ninguno)}")     # Salida: <class 'NoneType'>

# Ver el tipo de una función
def mi_funcion():
    pass
print(f"El tipo de mi_funcion es: {type(mi_funcion)}") # Salida: <class 'function'>

# Ver el tipo de un objeto de clase
class MiClase:
    pass
objeto = MiClase()
print(f"El tipo de objeto es: {type(objeto)}")       # Salida: <class '__main__.MiClase'>