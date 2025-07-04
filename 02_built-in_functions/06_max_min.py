# Encontrar el máximo y mínimo de una lista de números
numeros = [10, 5, 80, 25, 7]
print(f"Números: {numeros}")
print(f"El número máximo es: {max(numeros)}") # Salida: 80
print(f"El número mínimo es: {min(numeros)}") # Salida: 5

# Encontrar el máximo y mínimo de un conjunto de argumentos
print(f"El máximo entre 10, 50, 20 es: {max(10, 50, 20)}") # Salida: 50
print(f"El mínimo entre 'manzana', 'banana', 'kiwi' es: {min('manzana', 'banana', 'kiwi')}") # Salida: banana (orden alfabético)

# Usando el argumento 'key' para ordenar por una propiedad específica
personas = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "Marta", "edad": 35}
]

# Persona con la edad máxima
persona_mas_vieja = max(personas, key=lambda p: p['edad'])
print(f"La persona más vieja es: {persona_mas_vieja['nombre']} con {persona_mas_vieja['edad']} años.") # Salida: Marta con 35 años.

# Persona con la edad mínima
persona_mas_joven = min(personas, key=lambda p: p['edad'])
print(f"La persona más joven es: {persona_mas_joven['nombre']} con {persona_mas_joven['edad']} años.") # Salida: Luis con 25 años.