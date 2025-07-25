#!/bin/bash
# Script para crear y activar un entorno virtual con virtualenv en Linux/macOS

echo "--- Creando entorno virtual 'mi_virtualenv_proyecto' con virtualenv ---"
virtualenv mi_virtualenv_proyecto

echo "--- Activando entorno virtual 'mi_virtualenv_proyecto' ---"
source mi_virtualenv_proyecto/bin/activate

echo "--- Entorno virtual activo. Instalando un paquete de ejemplo (requests) ---"
pip install requests

echo "--- Paquetes instalados en 'mi_virtualenv_proyecto':"
pip list

echo "--- Para desactivar el entorno, ejecuta 'deactivate' en tu terminal."
echo "--- Para re-activar, usa: source mi_virtualenv_proyecto/bin/activate ---"