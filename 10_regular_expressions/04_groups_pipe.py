import re

texto_colores = "El color favorito es rojo. También me gusta el azul o el verde."
patron_colores = re.compile(r'favorito es (rojo|azul|verde|amarillo)')

coincidencia = patron_colores.search(texto_colores)

if coincidencia:
    print(f"Color favorito encontrado: {coincidencia.group(1)}") # Salida: rojo
else:
    print("Ningún color favorito conocido encontrado.")

# Usando findall para múltiples ocurrencias
coincidencias_multiples = re.findall(r'(rojo|azul|verde)', texto_colores)
print(f"Todos los colores mencionados: {coincidencias_multiples}") # Salida: ['rojo', 'azul', 'verde']