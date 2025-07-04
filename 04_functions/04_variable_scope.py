# Variable Global
contador_global = 0
mensaje_global = "Soy una variable global."

def funcion_con_variables():
    # Variable Local
    contador_local = 10
    mensaje_local = "Soy una variable local."

    print(f"Dentro de la función:")
    print(f"  Acceso a contador_local: {contador_local}")
    print(f"  Acceso a mensaje_local: {mensaje_local}")
    print(f"  Acceso a contador_global (solo lectura): {contador_global}")
    print(f"  Acceso a mensaje_global (solo lectura): {mensaje_global}")

# Llamada a la función
funcion_con_variables()

print("\nFuera de la función:")
# print(contador_local) # Esto causaría un NameError: name 'contador_local' is not defined
# print(mensaje_local)  # Esto causaría un NameError: name 'mensaje_local' is not defined
print(f"Acceso a contador_global: {contador_global}")
print(f"Acceso a mensaje_global: {mensaje_global}")

# Intentar modificar una global sin 'global' crea una nueva local
def intentar_modificar_global():
    contador_global = 5 # Esto crea una NUEVA variable local llamada 'contador_global'
    print(f"Dentro de intentar_modificar_global, contador_global (local): {contador_global}")

print("\n--- Intentando modificar global sin 'global' ---")
intentar_modificar_global()
print(f"Fuera de la función, contador_global (original): {contador_global}") # Sigue siendo 0

# Ejemplo con 'global'
visitas = 0 # Variable global

def registrar_visita():
    global visitas # Declaramos que vamos a modificar la variable global 'visitas'
    visitas += 1
    print(f"Número de visitas: {visitas}")

def obtener_total_visitas():
    # No necesitamos 'global' aquí porque solo la estamos leyendo
    print(f"El total de visitas registradas es: {visitas}")

print(f"Visitas iniciales: {visitas}") # Salida: 0

registrar_visita() # visitas ahora es 1
registrar_visita() # visitas ahora es 2
registrar_visita() # visitas ahora es 3

obtener_total_visitas() # Salida: El total de visitas registradas es: 3

# Otro ejemplo: modificar una cadena global
mensaje_estado = "Inactivo"

def activar_sistema():
    global mensaje_estado
    mensaje_estado = "Activo"
    print(f"Estado del sistema cambiado a: {mensaje_estado}")

print(f"\nEstado inicial del sistema: {mensaje_estado}") # Salida: Inactivo
activar_sistema()
print(f"Estado final del sistema: {mensaje_estado}")   # Salida: Activo