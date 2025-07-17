import re

mensaje = "Hola 123 mundo 456. Email: usuario@dominio.com."

# Reemplazar dígitos con '*'
mensaje_anonimizado = re.sub(r'\d', '*', mensaje)
print(f"Dígitos reemplazados: {mensaje_anonimizado}")
# Salida: Hola *** mundo ***. Email: usuario@dominio.com.

# Reemplazar una palabra específica
mensaje_sin_email = re.sub(r'Email:.*?\.', '', mensaje) # .*\. para coger hasta el punto
print(f"Email removido: {mensaje_sin_email}")
# Salida: Hola 123 mundo 456.

# Reemplazar con referencias a grupos
texto_nombres = "Nombre: Juan Pérez, Nombre: María García"
# Intercambiar orden de nombre y apellido
texto_invertido = re.sub(r'Nombre: (\w+) (\w+)', r'Nombre: \2, \1', texto_nombres)
print(f"Nombres invertidos: {texto_invertido}")
# Salida: Nombre: Pérez, Juan, Nombre: García, María