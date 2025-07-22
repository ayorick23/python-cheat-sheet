def calcular_descuento(precio, porcentaje_descuento):
    if not isinstance(precio, (int, float)) or not isinstance(porcentaje_descuento, (int, float)):
        raise TypeError("Precio y porcentaje de descuento deben ser números.")
    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
    
    descuento = precio * (porcentaje_descuento / 100)
    precio_final = precio - descuento
    return precio_final

print("--- Usando raise para validar entradas ---")
try:
    # Caso válido
    precio_con_descuento = calcular_descuento(100, 20)
    print(f"Precio con descuento: ${precio_con_descuento:.2f}")

    # Caso con TypeError
    calcular_descuento("cien", 10)
except TypeError as e:
    print(f"Error de tipo: {e}")

try:
    # Caso con ValueError
    calcular_descuento(50, 120)
except ValueError as e:
    print(f"Error de valor: {e}")

print("\n--- Relanzar una excepción (re-raising) ---")
def procesar_pedido(cantidad):
    try:
        if cantidad <= 0:
            raise ValueError("La cantidad del pedido debe ser positiva.")
        # Simular alguna lógica de procesamiento
        print(f"Procesando pedido de {cantidad} unidades.")
    except ValueError as e:
        print(f"Capturado en procesar_pedido: {e}")
        # Puedes añadir lógica de registro aquí y luego relanzar
        raise # Relanza la excepción original

try:
    procesar_pedido(-5)
except ValueError as e:
    print(f"Capturado en nivel superior: {e}")