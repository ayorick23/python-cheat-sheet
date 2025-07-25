@echo off
rem Script para instalar virtualenv globalmente (Windows CMD)

echo --- Instalando virtualenv globalmente ---
rem Es buena práctica instalar herramientas globales con pipx para aislamiento
rem Si no tienes pipx, puedes usar pip: pip install virtualenv
python -m pip install virtualenv

echo --- virtualenv instalado. ---
echo --- Puedes verificar la instalación con: virtualenv --version ---
pause