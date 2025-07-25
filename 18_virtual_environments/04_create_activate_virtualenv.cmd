@echo off
rem Script para crear y activar un entorno virtual con virtualenv en Windows CMD

echo --- Creando entorno virtual 'mi_virtualenv_proyecto' con virtualenv ---
virtualenv mi_virtualenv_proyecto

echo --- Activando entorno virtual 'mi_virtualenv_proyecto' ---
call mi_virtualenv_proyecto\Scripts\activate.bat

echo --- Entorno virtual activo. Instalando un paquete de ejemplo (requests) ---
pip install requests

echo --- Paquetes instalados en 'mi_virtualenv_proyecto':
pip list

echo --- Para desactivar el entorno, ejecuta 'deactivate' en tu terminal.
echo --- Para re-activar, usa: mi_virtualenv_proyecto\Scripts\activate.bat ---
pause