# APIs

Una **API (_Application Programming Interface_)** es un conjunto de reglas y protocolos que permite que dos aplicaciones de software se comuniquen entre sí. En la web, la mayoría de las APIs se basan en el protocolo **HTTP/HTTPS** y utilizan formatos de datos como JSON o XML.

## Conceptos Fundamentales de APIs Web

- **Cliente y Servidor:** El cliente (ej. un navegador, tu script de Python) envía una solicitud (request) a la API. El servidor de la API procesa esa solicitud y envía una respuesta (response).
- **Métodos HTTP:** Los verbos HTTP definen el tipo de acción que el cliente desea realizar:

  - `GET`: Obtener un recurso (ej. leer un dato).
  - `POST`: Crear un nuevo recurso.
  - `PUT`: Actualizar un recurso existente (reemplazándolo por completo).
  - `PATCH`: Actualizar parcialmente un recurso.
  - `DELETE`: Eliminar un recurso.

- **Endpoints:** Son las URL específicas que representan los recursos de la API (ej. `/api/usuarios`, `/api/productos/123`).
- **Parámetros:** Datos que se envían con la solicitud. Pueden ser:

  - **Parámetros de URL:** Parte de la URL (ej. `/api/productos/123`).
  - **Parámetros de Consulta (Query):** Después del `?` en la URL (ej. `/api/usuarios?edad=30`).

- **Códigos de Estado HTTP:** La respuesta del servidor incluye un código de estado que indica el resultado de la solicitud (ej. `200 OK`, `404 Not Found`, `500 Internal Server Error`).
- **JSON (JavaScript Object Notation):** El formato de datos más común para las APIs web. Es ligero, fácil de leer y se mapea directamente a las estructuras de datos de Python (diccionarios y listas).

## Consumir APIs Externas con Python

Consumir una API significa hacer solicitudes a un servicio externo para obtener o enviar datos. La librería más popular y fácil de usar para esto en Python es `requests`.

- **Instalación:** `pip install requests`

## Crear APIs con Python

Para crear tus propias APIs en Python, necesitas un framework web. Los más populares y recomendados son:

- **Flask:** Un micro-framework web simple y ligero. Excelente para empezar o para APIs pequeñas y sencillas.
- **FastAPI:** Un framework web moderno, rápido y de alto rendimiento. Utiliza tipos de datos de Python (`typing`) para la validación automática de datos y la generación de documentación interactiva (Swagger UI).
- **Django REST Framework (DRF):** Un poderoso conjunto de herramientas para construir APIs RESTful sobre el framework web Django. Es ideal para proyectos grandes y complejos.

## Crear una API con Flask

Flask es muy popular por su simplicidad.

- **Instalación:** `pip install Flask`

## Crear una API con FastAPI

FastAPI se ha vuelto extremadamente popular por su velocidad y la simplicidad con la que genera documentación.

- **Instalación:** `pip install fastapi uvicorn` (`uvicorn` es un servidor ASGI para ejecutar la aplicación).

## ¿Cuándo Usar Cada Uno?

| Herramienta | Uso                                                                     | Pros                                                                  | Contras                                                    |
| ----------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------- |
| `requests`  | **Consumir APIs externas.** El estándar de facto.                       | Simple, intuitiva, rica en funcionalidades.                           | N/A (es un cliente, no un servidor).                       |
| Flask       | **Crear APIs pequeñas o medianas.** Rápido para empezar.                | Ligero, minimalista, gran comunidad, flexible.                        | No incluye muchas características por defecto.             |
| FastAPI     | **Crear APIs rápidas y modernas.** Para proyectos de cualquier tamaño.  | Muy rápido, validación automática de datos, documentación automática. | El paradigma `async` puede tener una curva de aprendizaje. |
| Django REST | **Crear APIs RESTful completas sobre un proyecto Django ya existente.** | Poderoso, incluye autenticación, serialización, ORM.                  | Requiere conocer Django, es más pesado.                    |
