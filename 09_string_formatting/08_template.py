from string import Template

# 1. Definir la plantilla de texto
plantilla_email = Template("Hola $nombre,\n\nTe recordamos que tu balance es de $balance.\n\nGracias,\nEl Equipo.")

# 2. Definir un diccionario con los datos a sustituir
datos = {
    'nombre': 'Elena',
    'balance': '$500.00'
}

# 3. Sustituir las variables en la plantilla
email_formateado = plantilla_email.substitute(datos)

print("--- Email generado ---")
print(email_formateado)

# Caso de uso seguro: evitar inyección de código
# template.substitute() solo reemplaza variables, no ejecuta código como los f-strings.
# plantilla_peligrosa = Template("El resultado de la suma es ${2 + 2}.") # Esto no funcionaría