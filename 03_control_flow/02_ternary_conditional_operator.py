# Ejemplo de asignación simple
edad = 20
estado = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(f"Tienes {edad} años, por lo tanto eres: {estado}") # Salida: Mayor de edad

# Otro ejemplo con números
num = 10
par_o_impar = "Par" if num % 2 == 0 else "Impar"
print(f"El número {num} es: {par_o_impar}") # Salida: Par

# Usando el operador ternario en un print
saldo = 100
print("Transacción aprobada" if saldo >= 50 else "Transacción denegada")