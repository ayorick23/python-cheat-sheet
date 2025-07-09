import pprint

datos_complejos = {
    "nombre": "Equipo de Desarrollo",
    "miembros": [
        {"id": 1, "nombre": "Ana García", "rol": "Frontend"},
        {"id": 2, "nombre": "Bruno Díaz", "rol": "Backend"},
        {"id": 3, "nombre": "Carla Soto", "rol": "DevOps"}
    ],
    "proyectos": {
        "ProyectoA": {"estado": "En progreso", "tareas": 15},
        "ProyectoB": {"estado": "Pendiente", "tareas": 5},
        "ProyectoC": {"estado": "Completado", "tareas": 20}
    },
    "contacto": {
        "email": "devteam@ejemplo.com",
        "telefono": None,
        "direcciones": ["Calle Falsa 123", "Av. Siempre Viva 456"]
    }
}

print("--- Impresión normal (puede ser difícil de leer) ---")
print(datos_complejos)

print("\n--- Pretty Printing con pprint ---")
pprint.pprint(datos_complejos)

print("\n--- Pretty Printing con indentación personalizada ---")
pprint.pprint(datos_complejos, indent=2)

print("\n--- Pretty Printing con ancho limitado ---")
pprint.pprint(datos_complejos, width=40)