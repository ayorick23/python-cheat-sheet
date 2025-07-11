poblacion_mundial = 8200000000
presupuesto = 12345678.90

print(f"La población mundial es de {poblacion_mundial:,} personas.")
# Salida: La población mundial es de 8,200,000,000 personas.

print(f"El presupuesto de la compañía es ${presupuesto:,.2f}.")
# Salida: El presupuesto de la compañía es $12,345,678.90.

# También puedes usar _ como separador, especialmente útil en el código
print(f"Presupuesto: {presupuesto:_}")
# Salida: Presupuesto: 12_345_678.9