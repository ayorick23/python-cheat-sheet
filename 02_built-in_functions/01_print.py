# Imprimir una cadena simple
print("Hola, mundo!")

# Imprimir variables
nombre = "Dereck"
edad = 25
print("Nombre:", nombre, "Edad:", edad)

# Usando f-strings (una forma moderna y recomendada para formatear cadenas)
print(f"Me llamo {nombre} y tengo {edad} años.")

# Cambiar el separador
print("Manzana", "Pera", "Uva", sep="-")

# Cambiar el final de línea
print("Esto está en la primera línea.", end=" ")
print("Esto continúa en la misma línea.")

# Imprimir en un archivo (ejemplo básico)
with open("salida.txt", "w") as f:
    print("Este texto va al archivo.", file=f)
print("Revisa el archivo 'salida.txt' para ver la salida.")