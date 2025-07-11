nombre = "Python"
ancho = 20

print(f"|{nombre:<{ancho}}|") # Alineación a la izquierda, relleno con espacios
print(f"|{nombre:>{ancho}}|") # Alineación a la derecha, relleno con espacios
print(f"|{nombre:^{ancho}}|") # Alineación al centro, relleno con espacios

# Relleno con un carácter específico
print(f"|{nombre:-<{ancho}}|") # Relleno con guiones
print(f"|{nombre:*>{ancho}}|") # Relleno con asteriscos
print(f"|{nombre:=^{ancho}}|") # Relleno con signos de igual