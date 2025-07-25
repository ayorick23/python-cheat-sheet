@echo off
rem Script para instalar una versión específica de Python con pyenv-win

echo --- Instalando Python 3.9.13 con pyenv-win (versión estable común) ---
rem pyenv-win usa versiones ligeramente diferentes a las de pyenv normal
pyenv install 3.9.13

echo --- Verificando versiones de Python instaladas con pyenv-win ---
pyenv versions

echo --- Puedes ejecutar este script con: 2_install_python_with_pyenv.cmd ---
pause