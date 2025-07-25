@echo off
rem Script para desactivar un entorno virtual (solo funciona si ya está activo en la terminal actual)

echo --- Desactivando entorno virtual ---
call deactivate

echo --- Entorno virtual desactivado. ---
echo --- Puedes ejecutar este script con: 2_deactivate_venv.cmd (si el entorno está activo) ---
pause