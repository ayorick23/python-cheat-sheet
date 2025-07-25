#!/bin/bash
# Script para crear y activar un entorno virtual con venv en Linux/macOS

echo "--- Creando entorno virtual 'mi_venv_proyecto' ---"
python3 -m venv mi_venv_proyecto

echo "--- Activando entorno virtual 'mi_venv_proyecto' ---"
source mi_venv_proyecto/bin/activate

echo "--- Entorno virtual activo. Instalando un paquete de ejemplo (requests) ---"
pip install requests

echo "--- Paquetes instalados en 'mi_venv_proyecto':"
pip list

echo "--- Para desactivar el entorno, ejecuta 'deactivate' en tu terminal."
echo "--- Para re-activar, usa: source mi_venv_proyecto/bin/activate ---"
echo "--- Puedes ejecutar este script con: bash 1_create_and_activate_venv.sh ---"