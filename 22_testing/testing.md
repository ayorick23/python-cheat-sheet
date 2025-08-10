# Testing

El **testing** en Python es el proceso de verificar el comportamiento de tu código para asegurarte de que funciona como esperas. Cubriremos las herramientas estándar y las más populares de la comunidad.

## Conceptos Fundamentales de Testing

Antes de entrar en las herramientas, es vital entender estos conceptos:

- **Prueba Unitaria (Unit Test):** El tipo de prueba más pequeño y fundamental. Aísla una porción de código (generalmente una función o método) y verifica que se comporta correctamente de forma independiente.
- **Prueba de Integración (Integration Test):** Combina y prueba diferentes partes de tu código (ej. un módulo con una base de datos) para ver si funcionan juntas correctamente.
- **Prueba de Aceptación/Funcional (Acceptance Test):** Verifica que el sistema completo cumple con los requisitos del usuario. Se asemeja más a cómo un usuario final interactuaría con la aplicación.
- **Cobertura de Código (Code Coverage):** Mide la cantidad de código fuente que se ha ejecutado durante las pruebas. Un alto porcentaje de cobertura no garantiza la ausencia de bugs, pero indica que gran parte de tu código está siendo probado.
- **Test Runner:** Una herramienta que descubre y ejecuta tus pruebas, y reporta los resultados.
- **Fixture:** Un estado o configuración que se necesita para que una prueba se ejecute (ej. una conexión a una base de datos, un objeto inicializado).

## Doctest: Pruebas en la Documentación

**Doctest** es una herramienta integrada en Python que busca bloques de código de tipo `>>>` en las cadenas de documentación (`docstrings`) de tus funciones o clases. Es ideal para documentar el comportamiento esperado de tu código y asegurarse de que los ejemplos de la documentación no queden obsoletos.

- **Uso:** Principalmente para ejemplos sencillos y de auto-documentación.
- **Integración:** Viene con la instalación estándar de Python.

## Unittest (PyUnit): El Framework Estándar

**Unittest** es el framework de pruebas unitarias de Python que se basa en la sintaxis de JUnit de Java. Viene incluido en la biblioteca estándar y es muy robusto.

- **Uso:** Creación de pruebas unitarias estructuradas, con configuración y limpieza (`setUp`/`tearDown`).
- **Estructura:** Las pruebas se organizan en clases de prueba, que heredan de `unittest.TestCase`.

## Nose: El Test Runner Sencillo

**Nose** fue en su momento un popular `test runner` que buscaba simplificar el proceso de descubrimiento y ejecución de pruebas. Fue muy influyente, pero su desarrollo ha decaído en favor de herramientas más modernas como `pytest`. Aunque ya no se recomienda para nuevos proyectos, su impacto fue clave.

- **Uso:** Descubría pruebas automáticamente sin necesidad de `unittest.main()`.
- **Estado:** Considerado obsoleto. Su sucesor espiritual es `pytest`.

## Pytest: El Estándar Moderno de la Comunidad

**Pytest** es el test runner de facto de la comunidad de Python. Es conocido por su sintaxis simple, legible y potente. Requiere menos boilerplate que `unittest` y ofrece características avanzadas.

- **Instalación:** `pip install pytest`
- **Uso:** Descubre automáticamente las pruebas, ofrece `fixtures` más poderosas, y tiene una gran cantidad de plugins.

## Tox: El Entorno de Pruebas Aislado

**Tox** es una herramienta de automatización y orquestación de pruebas. Su objetivo principal es automatizar las pruebas y despliegues en múltiples entornos de Python (ej. Python 3.8, 3.9, 3.10), asegurando que tu proyecto funcione en todas las versiones de Python que soporta.

- **Instalación:** `pip install tox`
- **Uso:** Se configura con un archivo `tox.ini` en la raíz de tu proyecto.
- **Beneficios:** Aislamiento total de dependencias, automatización del ciclo de pruebas, y ejecución en múltiples entornos.

### Ejemplo de `tox.ini`

```ini,TOML
# tox.ini
[tox]
envlist = py38, py39, py310

[testenv]
deps =
    pytest
    # Otras dependencias de tu proyecto
commands =
    pytest
```

### Explicación

- `[tox]` y `envlist`: Le dice a Tox que cree y ejecute un entorno de pruebas para Python 3.8, 3.9 y 3.10.
- `[testenv]`: Configura un entorno de pruebas genérico.
- `deps`: Instala las dependencias necesarias (`pytest` en este caso).
- `commands`: Ejecuta el comando de pruebas (`pytest`).

Tox creará un entorno virtual aislado para cada versión de Python especificada y ejecutará `pytest` en cada uno, reportando los resultados al final.

## ¿Cuál Usar?

- `doctest`: Para pruebas sencillas embebidas en la documentación. Rápido y útil para ejemplos.
- `unittest`: Si necesitas un framework completo que sigue estándares y que ya está incluido en la librería estándar.
- `pytest`: La elección recomendada para la mayoría de los proyectos modernos. Su sintaxis simple, potente sistema de fixtures y amplio ecosistema de plugins lo hacen el favorito de la comunidad.
- `tox`: Para proyectos que necesitan probar su compatibilidad en múltiples versiones de Python, o para automatizar la configuración y ejecución de pruebas de manera aislada y reproducible.
