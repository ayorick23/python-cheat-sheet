import re

texto = "AA ABBBBBA CCCCC DD EEEEEEE"

# Exactamente 2 'A'
patron_a_doble = re.compile(r'A{2}')
print(f"Coincidencias de 'A' dos veces: {patron_a_doble.findall(texto)}") # Salida: ['AA']

# 3 o más 'B'
patron_b_min_3 = re.compile(r'B{3,}')
print(f"Coincidencias de 'B' 3 o más veces: {patron_b_min_3.findall(texto)}") # Salida: ['BBBBB']

# Entre 2 y 5 'C'
patron_c_rango = re.compile(r'C{2,5}')
print(f"Coincidencias de 'C' entre 2 y 5 veces: {patron_c_rango.findall(texto)}") # Salida: ['CCCCC']

# 5 o más 'E'
patron_e_min_5 = re.compile(r'E{5,}')
print(f"Coincidencias de 'E' 5 o más veces: {patron_e_min_5.findall(texto)}") # Salida: ['EEEEEEE']