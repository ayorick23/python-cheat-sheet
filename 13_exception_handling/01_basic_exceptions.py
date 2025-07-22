# División por cero
print("--- Ejemplo 1: División por cero ---")
try:
    resultado = 10 / 0
    print(f"El resultado es: {resultado}") # Esta línea no se ejecutará
except ZeroDivisionError:
    print("¡Error: No se puede dividir por cero!")

# Acceso a índice fuera de rango
print("\n--- Ejemplo 2: Acceso a índice fuera de rango ---")
mi_lista = [1, 2, 3]
try:
    elemento = mi_lista[5]
    print(f"El elemento es: {elemento}") # Esta línea no se ejecutará
except IndexError:
    print("¡Error: Intentaste acceder a un índice que no existe en la lista!")

# Archivo no encontrado
print("\n--- Ejemplo 3: Archivo no encontrado ---")
try:
    with open("archivo_inexistente.txt", "r") as f:
        contenido = f.read()
    print("Contenido del archivo:", contenido)
except FileNotFoundError:
    print("¡Error: El archivo especificado no fue encontrado!")

# Capturar cualquier excepción genérica (no recomendado para control de flujo)
print("\n--- Ejemplo 4: Captura genérica (¡Usar con precaución!) ---")
try:
    # Intenta hacer algo que cause un error, por ejemplo, una variable no definida
    print(variable_no_definida)
except Exception as e: # 'Exception' captura la mayoría de los errores
    print(f"Ocurrió un error inesperado: {e}")