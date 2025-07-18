# JSON and YAML

**JSON (_JavaScript Object Notation_)** y **YAML (_YAML Ain't Markup Language_)** son formatos legibles por humanos para serializar objetos de datos. Ambos son ampliamente utilizados para la configuración de aplicaciones, la transmisión de datos a través de redes y el almacenamiento de estructuras de datos simples.

## Archivos JSON

**JSON** es un formato ligero para el intercambio de datos. Es fácil de leer y escribir para los humanos y fácil de parsear y generar para las máquinas. Se basa en una estructura de pares clave-valor (como los diccionarios de Python) y listas (como las listas de Python).

Python tiene un módulo incorporado llamado json para trabajar con datos JSON.

### Cargar Datos

- `json.load(file_object)`: Lee un objeto JSON desde un objeto de archivo (ya abierto) y lo deserializa en un objeto Python (típicamente un diccionario o lista).
- `json.loads(json_string)`: Lee una cadena JSON (string) y la deserializa en un objeto Python.

### Guardar Datos

- `json.dump(python_object, file_object, indent=None)`: Serializa un objeto Python y lo escribe en un objeto de archivo (ya abierto). El parámetro `indent` te permite formatear la salida con indentación para hacerla más legible.
- `json.dumps(python_object, indent=None)`: Serializa un objeto Python a una cadena JSON.

## Archivos YAML

**YAML** es otro formato popular para la serialización de datos, a menudo preferido para archivos de configuración por su legibilidad mejorada (se basa en la indentación). Python no incluye un módulo YAML en su librería estándar, por lo que necesitarás instalar la librería PyYAML.

```bash
pip install PyYAML
```

### Cargar Datos

- `yaml.safe_load(stream)`: Carga un solo documento YAML desde un stream (objeto de archivo o cadena). `safe_load` se prefiere sobre `load` por razones de seguridad, ya que previene la ejecución de código arbitrario.
- `yaml.safe_load_all(stream)`: Carga múltiples documentos YAML desde un stream (separados por `---`). Devuelve un generador.

### Guardar Datos

- `yaml.dump(python_object, stream, default_flow_style=False)`: Serializa un objeto Python a un stream (objeto de archivo o cadena). `default_flow_style=False` hace que la salida sea más legible con indentación.
- `yaml.safe_dump()`: Es la versión preferida por seguridad.

## `anyconfig`

El módulo `anyconfig` es una librería muy útil que proporciona una API unificada para cargar, volcar (dump) y validar archivos de configuración en varios formatos (JSON, YAML, INI, XML, TOML, etc.). Esto es extremadamente útil cuando tu aplicación necesita soportar múltiples formatos de configuración o cuando quieres abstraerte de los detalles de cada formato.

**Instalación:**

```bash
pip install anyconfig
# Si necesitas soporte para YAML, TOML, etc., también instala sus dependencias
pip install "anyconfig[yaml,toml]"
```

### Cargar Configuración

`anyconfig.load()` puede detectar el formato del archivo automáticamente basándose en la extensión o puedes especificarlo.

```python
import anyconfig
config = anyconfig.load('ruta/a/archivo_config.ext')
config = anyconfig.load('ruta/a/archivo_config.ext', ac_parser='json') # Forzar parser
```

### Guardar Configuración

`anyconfig.dump()` permite serializar objetos Python a diferentes formatos de archivo.

```python
import anyconfig
datos = {"clave": "valor"}
anyconfig.dump(datos, 'ruta/a/archivo_salida.ext')
anyconfig.dump(datos, 'ruta/a/archivo_salida.ext', ac_parser='json', indent=4)
```
