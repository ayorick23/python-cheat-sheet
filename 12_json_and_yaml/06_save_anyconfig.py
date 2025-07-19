import anyconfig
import os

# Datos Python para guardar
mis_datos = {
    "proyecto": "MiSuperApp",
    "version": "2.0",
    "componentes": [
        {"nombre": "frontend", "tecnologia": "React"},
        {"nombre": "backend", "tecnologia": "Python Flask"}
    ]
}

# --- Guardar como JSON ---
print("--- Guardando con anyconfig como JSON ---")
output_json_file = "output_config.json"
anyconfig.dump(mis_datos, output_json_file, ac_parser='json', indent=4)
print(f"Datos guardados en '{output_json_file}'.")
with open(output_json_file, "r") as f:
    print("\nContenido de JSON generado:")
    print(f.read())

# --- Guardar como YAML ---
print("\n--- Guardando con anyconfig como YAML ---")
output_yaml_file = "output_config.yaml"
anyconfig.dump(mis_datos, output_yaml_file, ac_parser='yaml', default_flow_style=False)
print(f"Datos guardados en '{output_yaml_file}'.")
with open(output_yaml_file, "r") as f:
    print("\nContenido de YAML generado:")
    print(f.read())

# Limpieza
os.remove(output_json_file)
os.remove(output_yaml_file)