nombre = "María"
edad = 25
salario = 55000.50

# Uso básico, incrustando variables directamente
print(f"La empleada se llama {nombre}, tiene {edad} años y su salario es de ${salario}.")

# Puedes incrustar expresiones de Python
print(f"El próximo año, {nombre} tendrá {edad + 1} años.")

# También puedes llamar a funciones
def es_mayor_de_edad(edad):
    return "sí" if edad >= 18 else "no"

print(f"¿Es {nombre} mayor de edad? La respuesta es {es_mayor_de_edad(edad)}.")