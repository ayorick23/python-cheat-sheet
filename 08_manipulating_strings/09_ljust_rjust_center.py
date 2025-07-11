item = "Laptop"
precio = "1200"
ancho_columna = 15

print("--- Justificación de texto ---")
print(f"| {item.ljust(ancho_columna)} | {precio.rjust(ancho_columna)} |")
# Salida: | Laptop          |          1200 |

nombre = "Alice"
ancho_total = 20

print(f"'{nombre.ljust(ancho_total, '-')}'") # Salida: 'Alice---------------'
print(f"'{nombre.rjust(ancho_total, '*')}'") # Salida: '***************Alice'
print(f"'{nombre.center(ancho_total, '=')}'") # Salida: '=======Alice========'

print("\n--- Ejemplo de tabla ---")
headers = ["Producto", "Cantidad", "Precio Unitario"]
data = [
    ["Manzanas", "10", "1.50"],
    ["Peras", "5", "2.00"],
    ["Naranjas", "25", "0.75"]
]

print(f"{headers[0].ljust(15)} {headers[1].center(10)} {headers[2].rjust(15)}")
print("-" * 40)
for row in data:
    print(f"{row[0].ljust(15)} {row[1].center(10)} {row[2].rjust(15)}")