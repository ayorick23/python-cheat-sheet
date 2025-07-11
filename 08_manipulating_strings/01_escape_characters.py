import time

# Comillas simples
print('Esto es una cadena con \'comilla simple\'')  # Imprime: Esto es una cadena con 'comilla simple'

# Comillas dobles
print("Esto es una cadena con \"comilla doble\"")  # Imprime: Esto es una cadena con "comilla doble"

# Tabulación
print("Hola\tMundo")  # Imprime: Hola  Mundo

# Salto de línea
print("Hola\nMundo")  # Imprime: Hola
                      #         Mundo

# Barra invertida
print("La ruta es: C:\\Carpeta\\Archivo.txt")  # Imprime: La ruta es: C:\Carpeta\Archivo.txt

# Retroceso de cursor
print("Hola\bMundo")  # Imprime "HolaMundo", pero el cursor retrocede una posición después de "Hola"

# Caracter de valor octal
print("\110\145\154\154\157") # Imprime: Hello (código ASCII en octal)
print("\127\117\122\114\104") # Imprime: World (código ASCII en octal)

# Retorno de carro
for i in range(10):
    print(f"\rProgreso: {i+1}/10", end="")
    time.sleep(1)

print() # Imprime un salto de línea al final