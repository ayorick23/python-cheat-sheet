import re

# Patrón para fechas en formato DD-MM-AAAA
patron_fecha = re.compile(r'(\d{2})-(\d{2})-(\d{4})')
texto_fecha = "Fecha de hoy: 15-07-2025 y fecha de vencimiento: 31-12-2026."

coincidencia = patron_fecha.search(texto_fecha)

if coincidencia:
    print(f"Coincidencia completa: {coincidencia.group(0)}") # o coincidencia.group()
    print(f"Día: {coincidencia.group(1)}")
    print(f"Mes: {coincidencia.group(2)}")
    print(f"Año: {coincidencia.group(3)}")
    print(f"Todos los grupos: {coincidencia.groups()}") # Salida: ('15', '07', '2025')
else:
    print("Fecha no encontrada.")