# Ejemplos de acceso por índice y slicing en listas de Python
# Lista de ejemplo
frutas = ["Manzana", "Banana", "Cereza", "Naranja", "Kiwi", "Melón"]

# Acceso por índice positivo
print(f"Primera fruta: {frutas[0]}")  # Salida: Manzana
print(f"Tercera fruta: {frutas[2]}")  # Salida: Cereza

# Acceso por índice negativo
print(f"Última fruta: {frutas[-1]}")  # Salida: Melón
print(f"Penúltima fruta: {frutas[-2]}") # Salida: Kiwi

# Slicing básico
print(f"Frutas de la segunda a la cuarta (excl.): {frutas[1:4]}") # Salida: ['Banana', 'Cereza', 'Naranja']
print(f"Las tres primeras frutas: {frutas[:3]}")  # Salida: ['Manzana', 'Banana', 'Cereza']
print(f"Desde la cuarta fruta hasta el final: {frutas[3:]}")  # Salida: ['Naranja', 'Kiwi', 'Melón']
print(f"Copia completa de la lista: {frutas[:]}") # Salida: ['Manzana', 'Banana', 'Cereza', 'Naranja', 'Kiwi', 'Melón']

# Slicing con paso
print(f"Frutas alternas: {frutas[::2]}") # Salida: ['Manzana', 'Cereza', 'Kiwi']
print(f"Frutas en orden inverso: {frutas[::-1]}") # Salida: ['Melón', 'Kiwi', 'Naranja', 'Cereza', 'Banana', 'Manzana']

# Slicing con índices negativos
print(f"Del penúltimo al segundo (inv.): {frutas[-2:0:-1]}") # Salida: ['Kiwi', 'Naranja', 'Cereza', 'Banana']