# Función que devuelve un solo valor
def cuadrado(numero):
    return numero * numero

resultado_cuadrado = cuadrado(7)
print(f"El cuadrado de 7 es: {resultado_cuadrado}") # Salida: 49

# Función que devuelve múltiples valores (como una tupla)
def obtener_estadisticas(lista_numeros):
    if not lista_numeros:
        return 0, 0, 0 # Retornamos valores por defecto si la lista está vacía
    min_val = min(lista_numeros)
    max_val = max(lista_numeros)
    promedio = sum(lista_numeros) / len(lista_numeros)
    return min_val, max_val, promedio

numeros = [10, 20, 5, 30, 15]
minimo, maximo, promedio = obtener_estadisticas(numeros) # Desempaquetado de tupla
print(f"En la lista {numeros}:")
print(f"Mínimo: {minimo}")   # Salida: 5
print(f"Máximo: {maximo}")   # Salida: 30
print(f"Promedio: {promedio:.2f}") # Salida: 16.00

# Función con retorno condicional
def verificar_edad(edad):
    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"

print(f"Una persona de 20 años es: {verificar_edad(20)}") # Salida: Mayor de edad
print(f"Una persona de 16 años es: {verificar_edad(16)}") # Salida: Menor de edad