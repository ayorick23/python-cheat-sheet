# Ejemplo básico de if-else
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Ejemplo con if-elif-else para un sistema de calificación
nota = 85

if nota >= 90:
    print("Calificación: A")
elif nota >= 80:
    print("Calificación: B")
elif nota >= 70:
    print("Calificación: C")
elif nota >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")

# Múltiples condiciones con operadores lógicos (and, or, not)
temperatura = 25
llueve = False

if temperatura > 20 and not llueve:
    print("Buen día para salir al parque.")
elif temperatura > 20 and llueve:
    print("Hace calor, pero está lloviendo.")
else:
    print("Quizás no sea el mejor día para actividades al aire libre.")

# If anidado
saldo = 500
compra = 300
if saldo >= compra:
    print("Saldo suficiente para la compra.")
    if compra > 200:
        print("¡Gran compra!")
else:
    print("Saldo insuficiente.")