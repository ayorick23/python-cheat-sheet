#!/bin/bash
# Script para establecer la versión local de Python con pyenv
# y luego crear y activar un entorno venv con esa versión.

echo "--- Estableciendo la versión local de Python a 3.9.18 para este directorio ---"
pyenv local 3.9.18

echo "--- Verificando la versión de Python activa localmente ---"
python -V # Esto debería mostrar Python 3.9.18

echo "--- Creando entorno virtual 'pyenv_project_env' con la versión de Python de pyenv ---"
python -m venv pyenv_project_env

echo "--- Activando el entorno virtual ---"
source pyenv_project_env/bin/activate

echo "--- Entorno virtual activo. Instalando un paquete de ejemplo (flask) ---"
pip install flask

echo "--- Paquetes instalados en 'pyenv_project_env':"
pip list

echo "--- Para desactivar, 'deactivate'. Para limpiar pyenv, 'pyenv local --unset'. ---"