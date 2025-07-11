producto = "computadora"
precio = 1250.75

# Marcadores de posición por posición
print("El {} cuesta ${}.".format(producto, precio))

# Marcadores de posición por índice (útil para repetir variables)
print("La {0} es un producto. El precio de la {0} es ${1}.".format(producto, precio))

# Marcadores de posición con nombre (más legible)
print("El {prod} cuesta ${prec:.2f}.".format(prec=precio, prod=producto))

# Se pueden usar para formatear números, rellenar espacios, etc.
# Formato de número con 2 decimales
print("El precio con 2 decimales es ${:.2f}.".format(precio))

# Relleno y alineación
print("Alineado a la derecha: |{:>15}|".format("hola"))
print("Alineado al centro: |{:^15}|".format("mundo"))