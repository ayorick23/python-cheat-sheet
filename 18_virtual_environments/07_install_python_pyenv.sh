#!/bin/bash
# Script para instalar una versión específica de Python con pyenv

echo "--- Instalando Python 3.9.18 con pyenv ---"
pyenv install 3.9.18

echo "--- Verificando versiones de Python instaladas con pyenv ---"
pyenv versions

echo "--- Puedes ejecutar este script con: bash 2_install_python_with_pyenv.sh ---"