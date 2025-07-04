# Argumentos posicionales y por defecto
def calcular_descuento(precio, porcentaje=10):
    """Calcula el precio final después de un descuento."""
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return f"Precio original: ${precio}, Descuento: {porcentaje}%, Precio final: ${precio_final:.2f}"

print(calcular_descuento(100))        # Salida: Precio original: $100, Descuento: 10%, Precio final: $90.00
print(calcular_descuento(200, 15))    # Salida: Precio original: $200, Descuento: 15%, Precio final: $170.00
print(calcular_descuento(porcentaje=20, precio=50)) # Argumentos de palabra clave

# Argumentos de longitud variable (*args)
def mostrar_ingredientes(*ingredientes):
    """Muestra una lista de ingredientes."""
    print("Ingredientes de la receta:")
    for ing in ingredientes:
        print(f"- {ing}")

mostrar_ingredientes("Harina", "Huevos", "Leche")
# Salida:
# Ingredientes de la receta:
# - Harina
# - Huevos
# - Leche

mostrar_ingredientes("Tomate")

# Argumentos de longitud variable (**kwargs)
def configurar_juego(**opciones):
    """Configura un juego con opciones dadas."""
    print("Configuración del juego:")
    for clave, valor in opciones.items():
        print(f"{clave.replace('_', ' ').capitalize()}: {valor}")

configurar_juego(nivel="Difícil", sonido="Activado", idioma="Español")
# Salida:
# Configuración del juego:
# Nivel: Difícil
# Sonido: Activado
# Idioma: Español

configurar_juego(graficos="Ultra", resolucion="1920x1080")

# Combinando todos los tipos (orden: posicional, por defecto, *args, **kwargs)
def ejemplo_completo(obligatorio, por_defecto="defecto", *args, **kwargs):
    print(f"Obligatorio: {obligatorio}")
    print(f"Por defecto: {por_defecto}")
    print(f"Args (tupla): {args}")
    print(f"Kwargs (diccionario): {kwargs}")

print("\n--- Ejemplo completo de argumentos ---")
ejemplo_completo(10, "valor_nuevo", "arg1", "arg2", clave_a="valorA", clave_b="valorB")