precio_unitario = 15
cantidad = 3
total_sin_impuestos = precio_unitario * cantidad

# Sin el especificador =
print(f"El total sin impuestos es: {total_sin_impuestos}")

# Con el especificador = (más útil para depuración)
print(f"El total sin impuestos es: {total_sin_impuestos=}")
# Salida: El total sin impuestos es: total_sin_impuestos=45

# Puedes usarlo con cualquier expresión
impuesto = 0.15
total_con_impuesto = total_sin_impuestos * (1 + impuesto)
print(f"El total con impuesto es: {total_con_impuesto=:.2f}") # También puedes formatear la salida
# Salida: El total con impuesto es: total_con_impuesto=51.75