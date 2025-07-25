# Package Managers

Los **administradores de paquetes** son herramientas que te permiten instalar, actualizar y gestionar las librerías (o "paquetes") de Python que tus proyectos necesitan. El administrador de paquetes estándar para Python es `pip`.

Cuando activas un entorno virtual, el `pip` que utilizas es el `pip` de ese entorno virtual, no el `pip` global de tu sistema. Esto garantiza que los paquetes se instalen solo dentro de tu "caja de arena" del proyecto.

## Instalar Paquetes con `pip`

La forma más básica de instalar un paquete es usando `pip install`.

```bash
pip install nombre_del_paquete
```

## Actualizar Paquetes con `pip`

Puedes actualizar un paquete a su última versión.

```bash
pip install --upgrade nombre_del_paquete
```

## Desinstalar Paquetes

Para eliminar un paquete de tu entorno.

```bash
pip uninstall nombre_del_paquete
```

## Gestionando Dependencias con `requirements.txt`

Para replicar un entorno, no querrás recordar todas las librerías que instalaste manualmente. Aquí es donde entra en juego el archivo `requirements.txt`.

### Generar `requirements.txt`

Esto guarda una lista de todos los paquetes y sus versiones exactas instaladas en tu entorno actual.

```bash
pip freeze > requirements.txt
```

### Instalar desde `requirements.txt`

En un nuevo entorno (o en la máquina de otro desarrollador), puedes instalar todas las dependencias listadas en el archivo.

```bash
pip install -r requirements.txt
```

## `PyPI` (The Python Package Index)

`PyPI` es el repositorio oficial de paquetes de Python de terceros. Es como un gran almacén donde los desarrolladores de Python publican sus librerías para que otros las usen.

- **Funcionamiento:** `pip` se conecta por defecto a `PyPI` para descargar los paquetes que solicitas. Cuando ejecutas `pip install requests`, `pip` va a `PyPI`, busca el paquete `requests`, descarga la versión más adecuada y la instala.

- **Uso Recomendado:** Siempre que necesites un paquete de terceros público, lo buscarás en `PyPI` (implícitamente a través de `pip`).

## `pipenv` (Unificador de Entornos y Paquetes)

`pipenv` busca simplificar el flujo de trabajo de desarrollo de Python unificando la gestión de entornos virtuales y paquetes. Es una alternativa a usar `venv` + `pip` por separado.

- **Funcionamiento:**

  - Crea y gestiona automáticamente entornos virtuales.
  - Proporciona comandos para instalar, desinstalar, ejecutar scripts, etc.
  - Utiliza `Pipfile` y `Pipfile.lock` en lugar de `requirements.txt`.

    - `Pipfile`: Lista las dependencias directas del proyecto (más legible).
    - `Pipfile.lock`: Fija las versiones exactas de todas las dependencias (directas e indirectas) para asegurar la reproducibilidad.

## `Poetry`

`Poetry` es una herramienta de gestión de dependencias y paquetes de Python que se enfoca en la reproductibilidad del proyecto y la publicación de paquetes. Es considerada por muchos como el "_estándar de oro_" moderno.

- **Funcionamiento:**
  - Gestiona entornos virtuales internamente (o puede usarlos existentes).
  - Usa el archivo `pyproject.toml` (un estándar de PEP) para definir metadatos del proyecto y dependencias.
  - Tiene un resolvedor de dependencias muy robusto que garantiza que todas las dependencias sean compatibles entre sí.
  - Proporciona comandos para ejecutar pruebas, construir paquetes, publicar en PyPI, etc.

## `uv`

`uv` es un instalador y resolvedor de paquetes de Python extremadamente rápido escrito en **Rust**. Es un reemplazo de `pip` y `pip-tools` (una herramienta para generar `requirements.txt` a partir de un `requirements.in`).

- **Funcionamiento:** Es un ejecutable único que realiza las operaciones de instalación y resolución de dependencias de `pip` y `pip-tools` a velocidades significativamente mayores. Se integra con `venv` para la creación y gestión de entornos básicos.

## `Conda` (Ecosistema Completo para Datos y Otros Lenguajes)

`Conda` no es solo un administrador de paquetes de Python, es un administrador de paquetes y entornos independiente del lenguaje. Es especialmente popular en la comunidad de **ciencia de datos e inteligencia artificial**.

- **Funcionamiento:**
  - Instala paquetes que no son solo de Python (ej. librerías C/C++, R, Java, etc.).
  - Crea y gestiona entornos que pueden contener diferentes versiones de Python y librerías, sin depender de `pip` o `PyPI` si no es necesario (tiene su propio repositorio de paquetes, Anaconda o Conda-Forge).
  - Puede resolver dependencias a través de lenguajes y paquetes de sistema.
