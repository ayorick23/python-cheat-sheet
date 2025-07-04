# all()
lista_verdaderos = [True, True, 1, "hola"]
lista_falsos = [True, False, 1]
lista_vacia = []
lista_con_cero = [1, 2, 0, 4]

print(f"all({lista_verdaderos}): {all(lista_verdaderos)}") # Salida: True (todos son verdaderos)
print(f"all({lista_falsos}): {all(lista_falsos)}")     # Salida: False (False está presente)
print(f"all({lista_vacia}): {all(lista_vacia)}")       # Salida: True (iterable vacío)
print(f"all({lista_con_cero}): {all(lista_con_cero)}")   # Salida: False (0 es falso)

# any()
print("\n---")
print(f"any({lista_verdaderos}): {any(lista_verdaderos)}") # Salida: True (hay al menos un verdadero)
print(f"any({lista_falsos}): {any(lista_falsos)}")       # Salida: True (hay al menos un verdadero)
print(f"any({lista_vacia}): {any(lista_vacia)}")         # Salida: False (iterable vacío)
print(f"any({lista_con_cero}): {any(lista_con_cero)}")     # Salida: True (1, 2, 4 son verdaderos)
print(f"any([0, '', False]): {any([0, '', False])}")   # Salida: False (todos son falsos)