import anyconfig
import os
import json # Necesario para crear el archivo json
import yaml # Necesario para crear el archivo yaml

# --- Crear archivos de configuración de ejemplo ---
json_config_data = {"app_name": "MyWebApp", "version": "1.0", "settings": {"debug": True}}
with open("config.json", "w") as f:
    json.dump(json_config_data, f, indent=2)

yaml_config_data = {"database": {"type": "mysql", "port": 3306}, "logging": {"level": "INFO"}}
with open("config.yaml", "w") as f:
    yaml.dump(yaml_config_data, f, default_flow_style=False)

# --- Cargar configuración JSON ---
print("--- Cargando config.json con anyconfig ---")
try:
    config_json = anyconfig.load("config.json")
    print(f"App Name: {config_json['app_name']}")
    print(f"Debug Mode: {config_json['settings']['debug']}")
except anyconfig.AnyConfigException as e:
    print(f"Error al cargar config.json: {e}")

# --- Cargar configuración YAML ---
print("\n--- Cargando config.yaml con anyconfig ---")
try:
    config_yaml = anyconfig.load("config.yaml")
    print(f"Database Type: {config_yaml['database']['type']}")
    print(f"Logging Level: {config_yaml['logging']['level']}")
except anyconfig.AnyConfigException as e:
    print(f"Error al cargar config.yaml: {e}")

# --- Cargar múltiples archivos y fusionarlos (ejemplo avanzado) ---
# anyconfig puede fusionar configuraciones de múltiples fuentes.
# El orden importa para la sobrescritura de valores.
print("\n--- Fusionando configuraciones con anyconfig ---")
merged_config = anyconfig.load(["config.json", "config.yaml"])
# Los valores de config.yaml sobrescribirán si hay claves duplicadas en config.json
print(f"Configuración fusionada: {merged_config}")
print(f"¿'app_name' en fusionado? {'app_name' in merged_config}") # True
print(f"¿'database' en fusionado? {'database' in merged_config}") # True

# Limpieza
os.remove("config.json")
os.remove("config.yaml")