#!/bin/bash
# Script de GUÍA para instalar pyenv en Linux/macOS
# NOTA: La instalación de pyenv requiere pasos manuales para configurar el shell.

echo "--- Instalando pyenv (requiere Git) ---"
# Clona el repositorio de pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# Añade pyenv al PATH y habilita el autocompletado/shims (ESTO ES MANUALMENTE EN TU SHELL RC)
echo -e 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo -e 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'eval "$(pyenv init --no-rehash -)"' >> ~/.bashrc
echo -e 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# Para zsh, usar ~/.zshrc en lugar de ~/.bashrc
# Para aplicar los cambios, debes recargar tu shell: source ~/.bashrc o source ~/.zshrc
echo "--- pyenv instalado. Por favor, reinicia tu terminal o ejecuta 'source ~/.bashrc' (o .zshrc) ---"
echo "--- Después de reiniciar, puedes ejecutar: pyenv versions para verificar. ---"
echo "--- Si usas Windows, busca 'pyenv-win' para la instalación. ---"