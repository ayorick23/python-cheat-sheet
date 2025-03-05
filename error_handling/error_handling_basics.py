#Manejo de excepciones con try-except
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
    
#Capturar multiples excepciones
try:
    num = int("abc")
except ValueError:
    print("Error: No se puede convertir a entero")
except Exception as e:
    print(f"Otro error: {e}")