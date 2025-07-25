@echo off
rem Script para establecer la versión local de Python con pyenv-win
rem y luego crear y activar un entorno venv con esa versión.

echo --- Estableciendo la versión local de Python a 3.9.13 para este directorio ---
pyenv local 3.9.13

echo --- Verificando la versión de Python activa localmente ---
python -V

echo --- Creando entorno virtual 'pyenv_project_env' con la versión de Python de pyenv-win ---
python -m venv pyenv_project_env

echo --- Activando el entorno virtual ---
call pyenv_project_env\Scripts\activate.bat

echo --- Entorno virtual activo. Instalando un paquete de ejemplo (flask) ---
pip install flask

echo --- Paquetes instalados en 'pyenv_project_env':
pip list

echo --- Para desactivar, 'deactivate'. Para limpiar pyenv, 'pyenv local --unset'. ---
pause