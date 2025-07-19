# ejemplo_yaml_carga.py
import yaml
import os

# --- Simular un archivo YAML con un documento ---
yaml_data_single = """
servidor:
  host: localhost
  puerto: 8080
base_de_datos:
  tipo: postgres
  usuario: admin
"""
with open("config_single.yaml", "w") as f:
    f.write(yaml_data_single)

# --- Simular un archivo YAML con múltiples documentos ---
yaml_data_multi = """
# Primer documento
- nombre: Item 1
  valor: 100
---
# Segundo documento
- nombre: Item 2
  valor: 200
- nombre: Item 3
  valor: 300
"""
with open("documentos_multiples.yaml", "w") as f:
    f.write(yaml_data_multi)

# --- Usando yaml.safe_load() ---
print("--- Leyendo documento único (yaml.safe_load) ---")
try:
    with open("config_single.yaml", "r") as f:
        config = yaml.safe_load(f)
        print(f"Tipo de datos cargados: {type(config)}")
        print(f"Host del servidor: {config['servidor']['host']}")
except FileNotFoundError:
    print("El archivo 'config_single.yaml' no se encontró.")
except yaml.YAMLError as e:
    print(f"Error al decodificar YAML desde el archivo: {e}")

# --- Usando yaml.safe_load_all() ---
print("\n--- Leyendo múltiples documentos (yaml.safe_load_all) ---")
try:
    with open("documentos_multiples.yaml", "r") as f:
        documentos = list(yaml.safe_load_all(f)) # Convertir generador a lista para ver todos
        print(f"Número de documentos: {len(documentos)}")
        print(f"Primer documento: {documentos[0]}")
        print(f"Segundo documento: {documentos[1][0]['nombre']}")
except FileNotFoundError:
    print("El archivo 'documentos_multiples.yaml' no se encontró.")
except yaml.YAMLError as e:
    print(f"Error al decodificar YAML desde el archivo: {e}")

# Limpieza
os.remove("config_single.yaml")
os.remove("documentos_multiples.yaml")