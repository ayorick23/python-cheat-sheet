s1 = "HOLA"
s2 = "hola"
s3 = "Hola Mundo"
s4 = "123 ABC"
s5 = "123"

print(f"'{s1}'.isupper(): {s1.isupper()}")       # Salida: True
print(f"'{s2}'.isupper(): {s2.isupper()}")       # Salida: False
print(f"'{s3}'.isupper(): {s3.isupper()}")       # Salida: False
print(f"'{s4}'.isupper(): {s4.isupper()}")       # Salida: True (los números se ignoran)
print(f"'{s5}'.isupper(): {s5.isupper()}")       # Salida: False (no hay caracteres alfabéticos)

print(f"\n'{s1}'.islower(): {s1.islower()}")     # Salida: False
print(f"'{s2}'.islower(): {s2.islower()}")       # Salida: True
print(f"'{s3}'.islower(): {s3.islower()}")       # Salida: False
print(f"'{s4}'.islower(): {s4.islower()}")       # Salida: False
print(f"'{s5}'.islower(): {s5.islower()}")       # Salida: False