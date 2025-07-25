#!/bin/bash
# Script para instalar virtualenv globalmente (Linux/macOS)

echo "--- Instalando virtualenv globalmente ---"
# Es buena práctica instalar herramientas globales con pipx para aislamiento
# Si no tienes pipx, puedes usar pip: pip install virtualenv
python3 -m pip install virtualenv

echo "--- virtualenv instalado. ---"
echo "--- Puedes verificar la instalación con: virtualenv --version ---"