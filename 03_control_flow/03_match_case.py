# Función para procesar comandos con match-case
def procesar_comando(comando):
    match comando:
        case "iniciar":
            print("Iniciando el sistema...")
        case "detener":
            print("Deteniendo el sistema.")
        case "reiniciar" | "reset": # Uso del OR para múltiples coincidencias
            print("Reiniciando el sistema...")
        case ("sumar", num1, num2): # Coincidencia con tuplas y captura de valores
            resultado = num1 + num2
            print(f"Suma de {num1} + {num2} = {resultado}")
        case ("dividir", num1, num2) if num2 != 0: # Coincidencia con 'guard'
            resultado = num1 / num2
            print(f"División de {num1} / {num2} = {resultado:.2f}")
        case ("dividir", _, 0): # Manejo de división por cero
            print("Error: No se puede dividir por cero.")
        case [item1, item2]: # Coincidencia con lista de longitud 2
            print(f"Recibida una lista con dos elementos: {item1} y {item2}")
        case {"accion": "mostrar", "item": item}: # Coincidencia con diccionario
            print(f"Mostrando el item: {item}")
        case _: # Patrón comodín (default)
            print(f"Comando desconocido: {comando}")

print("--- Ejemplos de match-case ---")
procesar_comando("iniciar")
procesar_comando("reset")
procesar_comando(("sumar", 10, 5))
procesar_comando(("dividir", 10, 2))
procesar_comando(("dividir", 10, 0))
procesar_comando(["primero", "segundo"])
procesar_comando({"accion": "mostrar", "item": "producto X"})
procesar_comando("otra cosa")


# Ejemplo de coincidencia con tipos built-in (conceptualmente)
# Aunque match-case no coincide directamente con "type",
# puedes usarlo con isinstance en un guard o patrones estructurales.
def procesar_dato(dato):
    match dato:
        case str(): # Coincide si el dato es una cadena
            print(f"El dato '{dato}' es una cadena.")
        case int(x) if x > 100: # Coincide si es un entero mayor a 100
            print(f"El dato {dato} es un entero grande.")
        case float(): # Coincide si el dato es un flotante
            print(f"El dato {dato} es un número flotante.")
        case list(): # Coincide si el dato es una lista
            print(f"El dato es una lista con {len(dato)} elementos.") # Longitud de iterable
        case _:
            print(f"El dato '{dato}' es de otro tipo.")

print("\n--- Ejemplos de coincidencia de tipos y longitud ---")
procesar_dato("Hola")
procesar_dato(50)
procesar_dato(150)
procesar_dato(3.14)
procesar_dato([1, 2, 3])
procesar_dato({"a":1})