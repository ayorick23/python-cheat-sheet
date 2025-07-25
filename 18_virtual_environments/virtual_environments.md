# Virtual Environments

Un **entorno virtual** es un directorio auto-contenido que contiene una instalación de Python y un conjunto de paquetes que son aislados del resto del sistema. Piensa en ello como una "caja de arena" o un espacio de trabajo privado para cada uno de tus proyectos.

## ¿Por qué son importantes?

- **Aislamiento de Dependencias:** Evitan conflictos entre las versiones de librerías requeridas por diferentes proyectos. Por ejemplo, el Proyecto A podría necesitar `requests` v2.20 y el Proyecto B `requests` v2.28. Sin entornos virtuales, tendrías un conflicto global.
- **Limpieza:** Mantienen las librerías de cada proyecto separadas de la instalación global de Python, evitando el "bloat" y facilitando la gestión.
- **Replicabilidad:** Facilitan compartir tus proyectos. Puedes exportar la lista exacta de dependencias de un entorno virtual, lo que permite a otros desarrolladores (o a ti mismo en otro momento) recrear el mismo entorno fácilmente.

## Herramientas Comunes para Entornos Virtuales

Python viene con módulos incorporados para crear entornos virtuales, siendo los más comunes:

## `venv`

Es la herramienta de facto para crear entornos virtuales en Python 3.3 y posteriores. Viene integrada con Python.

- **Funcionamiento:** Crea un directorio (`.venv` por convención) que contiene una copia mínima del intérprete de Python, un `pip` propio de ese entorno y directorios para instalar paquetes.

**Uso Recomendado:**

- **Proyectos individuales o pequeños:** Cuando no necesitas una gestión de dependencias excesivamente compleja.
- **Simpleza y portabilidad:** Ya que viene con Python, está disponible en cualquier lugar y es fácil de usar.
- **Educación/Introducción:** Es el punto de partida para aprender sobre entornos virtuales.

### Crear un Entorno Virtual con `venv`

La creación de un entorno virtual es un proceso sencillo que se realiza con la siguiente sintaxis:

```bash
python -m venv nombre_del_entorno
```

- `python`: Llama al intérprete de Python de tu sistema.
- `-m venv`: Le dice a Python que ejecute el módulo venv.
- `nombre_del_entorno`: Es el nombre del directorio donde se creará el entorno virtual. Convencionalmente, se usa venv, .venv, o env.

### Activar el Entorno Virtual (`venv`)

Una vez creado, debes "activar" el entorno virtual para que tu terminal use la instalación de Python y los paquetes de ese entorno, en lugar de los globales del sistema.

**Sintaxis (dependiendo de tu sistema operativo):**

- Windows (CMD):

  ```bash
  .venv\Scripts\activate.bat
  ```

- Windows (PowerShell):

  ```bash
  .venv\Scripts\Activate.ps1
  ```

- macOS / Linux:

  ```bash
  source .venv/bin/activate
  ```

### Desactivar el Entorno Virtual (`venv`)

Cuando hayas terminado de trabajar en un proyecto, o si necesitas cambiar a otro, puedes desactivar el entorno virtual con el comando `deactivate`.

```bash
deactivate
```

El nombre del entorno desaparecerá de la línea de comandos, indicando que ya no estás en el entorno virtual.

## `virtualenv`

Es una herramienta más antigua que `venv` y fue la solución estándar antes de Python 3.3. Todavía se usa, especialmente para versiones de Python más antiguas o en situaciones donde `venv` no cumple ciertos requisitos.

- **Funcionamiento:** Similar a `venv`, pero ofrece más opciones de configuración, como la posibilidad de usar intérpretes de Python remotos o personalizar más la estructura del entorno. Puede crear entornos para versiones de Python donde `venv` no está disponible.

**Uso Recomendado:**

- Proyectos con **versiones de Python antiguas (<3.3)**.
- **Casos de uso avanzados:** Donde se requiere un control más fino sobre la creación del entorno.

### Crear un Entorno Virtual con `virtualenv`

#### Instalar `virtualenv`

Si aún no tienes `virtualenv`, instálalo globalmente con `pip install virtualenv`.

```bash
pip install virtualenv
```

Navega a la carpeta de tu proyecto en la terminal y crea un entorno virtual con un nombre específico, por ejemplo, "venv":

```bash
virtualenv venv
```

Esto creará una carpeta llamada `venv` (o el nombre que hayas elegido) que contendrá el entorno aislado.

### Activar el Entorno Virtual (`virtualenv`)

- Windows:

  ```bash
  venv\Scripts\activate
  ```

- macOS / Linux:

  ```bash
  source venv/bin/activate
  ```

### Desactivar el Entorno Virtual (`virtualenv`)

```bash
deactivate
```

## `pyenv`

pyenv es un administrador de versiones de Python, no un creador de entornos virtuales en sí mismo (aunque se integra con ellos). Te permite instalar múltiples versiones de Python (ej. 3.8.1, 3.9.7, 3.10.4) en tu máquina y cambiar entre ellas fácilmente a nivel global, de usuario o de proyecto.

- **Funcionamiento:** No crea entornos virtuales directamente. En su lugar, modifica la variable de entorno PATH para dirigir la llamada a python a la versión deseada. Luego, puedes usar venv o pipenv con esa versión específica de Python que pyenv está "apuntando".

**Uso Recomendado:**

- **Testing:** Para probar tus aplicaciones en diferentes versiones de Python.
- Desarrolladores que trabajan con **múltiples proyectos, cada uno requiriendo una versión diferente de Python.**

### Crear un Entorno Virtual con `pyenv`

#### Instalar de `pyenv` y `pyenv-virtualenv`

- Si aún no tienes `pyenv` instalado, puedes encontrar instrucciones de instalación en su [repositorio oficial de GitHub](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation).
- Para instalar `pyenv-virtualenv`, generalmente se usa un instalador o se clona desde su repositorio y se configura el entorno.

Una vez que pyenv y pyenv-virtualenv estén instalados, puedes crear un entorno virtual con el siguiente comando:

```bash
pyenv virtualenv <version> <nombre_del_entorno>
```

- `<version>`: La versión de Python que deseas utilizar (ej. 3.9.1).
- `<nombre_del_entorno>`: El nombre que le darás a tu entorno virtual (ej. `my_project_env`).

### Activar el Entorno Virtual (`pyenv`)

```bash
pyenv activate <nombre_del_entorno>
```

### Desactivar el Entorno Virtual (`pyenv`)

```bash
pyenv deactivate
```

## Diferencia con Docker

Aquí es donde a menudo hay confusión. Los entornos virtuales de Python y Docker abordan problemas relacionados pero fundamentalmente diferentes.

### Entornos Virtuales (Python-centric)

- **Propósito:** Aislar las dependencias y la versión del intérprete de Python de un proyecto de otros proyectos en la misma máquina host.
- **Alcance:** A nivel de código Python y sus librerías.
- **Aislamiento:** Principalmente a nivel de paquetes de Python y la versión del intérprete. No virtualiza el sistema operativo o el hardware.
- **Portabilidad:** Buena para llevar el código a otra máquina con la misma base de sistema operativo (ej. Linux a Linux, o macOS a macOS), asumiendo que las dependencias del sistema operativo (si las hay) están presentes. Depende del sistema operativo subyacente.
- **Uso Típico:** Desarrollo local, garantizar que dos proyectos en tu laptop no se pisen las dependencias.

### Docker (Contenedorización)

- **Propósito:** Empaquetar una aplicación y todas sus dependencias (código, librerías del sistema, configuraciones, runtime, etc.) en una unidad autónoma y portable llamada contenedor.
- **Alcance:** A nivel de sistema operativo (ligero) y aplicación completa.
- **Aislamiento:** Proporciona un aislamiento a nivel de sistema operativo. Cada contenedor se ejecuta en un entorno aislado, con sus propios procesos, red, sistema de archivos. El contenedor tiene todo lo necesario para ejecutarse, independientemente del host.
- **Portabilidad:** Excelente. Un contenedor Docker se ejecutará de la misma manera en cualquier máquina que tenga Docker instalado, independientemente del sistema operativo host (Linux, Windows, macOS). "_Build once, run anywhere._"
- **Uso Típico:** Despliegue de aplicaciones, microservicios, entornos de desarrollo consistentes para equipos, CI/CD.
