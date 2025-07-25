@echo off
rem Script para crear y activar un entorno virtual con venv en Windows CMD

echo --- Creando entorno virtual 'mi_venv_proyecto' ---
python -m venv mi_venv_proyecto

echo --- Activando entorno virtual 'mi_venv_proyecto' ---
call mi_venv_proyecto\Scripts\activate.bat

echo --- Entorno virtual activo. Instalando un paquete de ejemplo (requests) ---
pip install requests

echo --- Paquetes instalados en 'mi_venv_proyecto':
pip list

echo --- Para desactivar el entorno, ejecuta 'deactivate' en tu terminal.
echo --- Para re-activar, usa: mi_venv_proyecto\Scripts\activate.bat ---
echo --- Puedes ejecutar este script con: 1_create_and_activate_venv.cmd ---
pause