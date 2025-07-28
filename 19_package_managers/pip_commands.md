# Principales Comandos `pip`

| Comando Principal | Subcomando/Opción Relevante | Descripción                                                                | Ejemplo de Uso                                            |
| ----------------- | --------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------- |
| `pip install`     | (ninguno)                   | Instala paquetes desde PyPI o fuentes locales/URLs.                        | `pip install requests`                                    |
|                   | `-r <file>`                 | Instala todos los paquetes listados en un archivo de requisitos.           | `pip install -r requirements.txt`                         |
|                   | `--upgrade`                 | Actualiza un paquete existente a la última versión.                        | `pip install --upgrade requests`                          |
|                   | `--no-deps`                 | Instala el paquete sin sus dependencias.                                   | `pip install --no-deps mypackage`                         |
|                   | `-e <path/url>`             | Instala un paquete en modo editable (para desarrollo).                     | `pip install -e .` (desde el directorio del proyecto)     |
|                   | `--target <dir>`            | Instala paquetes en un directorio específico.                              | `pip install --target=./mylib requests`                   |
| `pip uninstall`   | (ninguno)                   | Desinstala paquetes.                                                       | `pip uninstall requests`                                  |
|                   | `-y`                        | No pide confirmación para desinstalar.                                     | `pip uninstall -y requests`                               |
| `pip list`        | (ninguno)                   | Lista los paquetes instalados.                                             | `pip list`                                                |
|                   | `--outdated`                | Muestra los paquetes que tienen versiones más nuevas disponibles.          | `pip list --outdated`                                     |
|                   | `--format=freeze`           | Lista los paquetes en un formato adecuado para `requirements.txt`.         | `pip list --format=freeze > requirements.txt`             |
| `pip show`        | (ninguno)                   | Muestra información detallada sobre un paquete instalado.                  | `pip show requests`                                       |
| `pip freeze`      | (ninguno)                   | Genera una lista de los paquetes instalados en formato de requisitos.      | `pip freeze`                                              |
| `pip search`      | (comando retirado)          | (Nota: Este comando fue retirado en versiones recientes de pip)            | N/A                                                       |
| `pip check`       | (ninguno)                   | Verifica si las dependencias de los paquetes instalados están satisfechas. | `pip check`                                               |
| `pip config`      | `get <key>`                 | Muestra el valor de una opción de configuración.                           | `pip config get global.index-url`                         |
|                   | `set <key> <value>`         | Establece el valor de una opción de configuración.                         | `pip config set global.index-url https://pypi.org/simple` |
|                   | `unset <key>`               | Elimina una opción de configuración.                                       | `pip config unset global.index-url`                       |
|                   | `list`                      | Lista todas las configuraciones.                                           | `pip config list`                                         |
| `pip index`       | `versions <package>`        | Muestra las versiones disponibles de un paquete en PyPI.                   | `pip index versions requests`                             |
| `pip download`    | (ninguno)                   | Descarga paquetes sin instalarlos.                                         | `pip download requests`                                   |
| `pip cache`       | `dir`                       | Muestra el directorio de la caché de pip.                                  | `pip cache dir`                                           |
|                   | `purge`                     | Vacía la caché de pip.                                                     | `pip cache purge`                                         |
|                   | `remove <package>`          | Elimina un paquete de la caché.                                            | `pip cache remove requests`                               |
| `pip help`        | (ninguno)                   | Muestra la ayuda general de pip.                                           | `pip help`                                                |
|                   | `<comando>`                 | Muestra la ayuda para un comando específico (ej. `install`).               | `pip help install`                                        |
