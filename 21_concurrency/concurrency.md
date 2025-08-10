# Concurrency

La **concurrencia** se refiere a la capacidad de un sistema para manejar múltiples tareas en progreso "al mismo tiempo". Esto no significa necesariamente que las tareas se ejecuten simultáneamente (en paralelo puro), sino que la ejecución de una tarea puede superponerse con la ejecución de otra. El objetivo es maximizar la utilización de los recursos y mejorar la capacidad de respuesta.

En Python, el principal obstáculo para el paralelismo puro (ejecución simultánea) en CPU es el **GIL (_Global Interpreter Lock_)**.

## El GIL (_Global Interpreter Lock_)

El GIL es un mecanismo de Python que asegura que solo un hilo a la vez pueda ejecutar bytecode de Python en el intérprete **CPython**. Esto significa que, incluso en una máquina con múltiples núcleos de CPU, un programa Python multi-hilo no puede aprovechar esos núcleos para tareas intensivas de CPU de forma paralela.

**¿Por qué existe el GIL?** Principalmente para simplificar la gestión de memoria y evitar condiciones de carrera en la manipulación de objetos Python por parte de múltiples hilos, lo que haría el intérprete mucho más complejo y propenso a errores.

### Implicaciones del GIL

- **Tareas intensivas en CPU:** Para operaciones que requieren mucho cálculo (ej. procesamiento de datos, algoritmos complejos), el multi-threading no ofrecerá mejoras de rendimiento reales en CPython, ya que el GIL limitará la ejecución a un solo núcleo.
- **Tareas intensivas en E/S (Input/Output):** Para operaciones que esperan la finalización de E/S (ej. lectura/escritura de archivos, solicitudes de red, interacción con bases de datos), el GIL libera el bloqueo mientras el hilo está esperando la operación de E/S. Esto significa que otros hilos pueden ejecutarse, mejorando significativamente la capacidad de respuesta y el rendimiento en estos escenarios.

Dado el GIL, Python ofrece diferentes enfoques para la concurrencia:

### Multi-Threading (Hilos)

El **multi-threading** permite que un programa ejecute múltiples partes de código "simultáneamente" dentro del mismo proceso. Comparten el mismo espacio de memoria, lo que facilita la comunicación entre ellos, pero también requiere una gestión cuidadosa para evitar condiciones de carrera y deadlocks.

- **Uso:** Ideal para tareas intensivas en E/S, donde los hilos pueden liberar el GIL y permitir que otros hilos trabajen mientras uno espera una operación lenta.
- **Módulo:** `threading`

### Multi-Processing (Procesos)

El **multi-processing** permite ejecutar tareas en paralelo real, aprovechando múltiples núcleos de CPU. Cada proceso tiene su propio intérprete de Python y su propio espacio de memoria, lo que significa que el GIL no afecta al paralelismo entre procesos.

- **Uso:** Ideal para tareas intensivas en CPU que pueden dividirse en partes independientes.
- **Comunicación:** La comunicación entre procesos es más compleja (requiere IPC - InterProcess Communication) que entre hilos, ya que no comparten memoria directamente.
- **Sobrecarga:** Mayor sobrecarga de inicio y uso de memoria que los hilos.
- **Módulo:** `multiprocessing`

### Asyncio (Programación Asíncrona)

**Asyncio** es el marco de trabajo de Python para escribir código concurrente utilizando la sintaxis `async/await`. Es un enfoque de concurrencia **basada en una sola hebra (_single-threaded concurrency_)**, lo que significa que no hay paralelismo real, pero sí se logra la capacidad de respuesta ejecutando operaciones de forma cooperativa.

- **Uso:** Excelente para tareas intensivas en E/S (red, disco, base de datos) que requieren esperar la finalización de operaciones externas. Mientras una tarea `await` (espera) por E/S, el bucle de eventos de `asyncio` puede cambiar a otra tarea que esté lista para ejecutarse.
- **Funcionamiento:** Utiliza un bucle de eventos para programar la ejecución de "coroutines" (funciones `async`). Cuando una coroutine encuentra una operación de E/S (`await`), "cede" el control al bucle de eventos, permitiendo que otra coroutine se ejecute.
- **No evade el GIL:** Como opera en un solo hilo, no resuelve el problema de las tareas CPU-intensivas.
- **Módulo:** `asyncio`

## Comparativa: Hilos vs. Procesos vs. Asyncio

| Característica         | Hilos (threading)                                     | Procesos (multiprocessing)               | Asyncio (async/await)                                                  |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------- | ---------------------------------------------------------------------- |
| **Paralelismo Real**   | No (debido al GIL en CPython)                         | Sí (cada proceso tiene su propio GIL)    | No (concurrencia en un solo hilo)                                      |
| **Mejor para**         | Tareas I/O-intensivas (red, disco, etc.)              | Tareas CPU-intensivas (cálculos)         | Tareas I/O-intensivas (altamente concurrentes)                         |
| **Espacio de Memoria** | Compartido (mismo proceso)                            | Separado (copia de memoria)              | Compartido (mismo hilo/bucle de eventos)                               |
| **Comunicación**       | Fácil (variables compartidas), pero requiere bloqueos | Más compleja (colas, pipes, managers)    | Fácil (al ser single-threaded, no hay condiciones de carrera de hilos) |
| **Sobrecarga**         | Baja                                                  | Alta (creación de procesos es costosa)   | Baja (solo cambio de contexto de coroutines)                           |
| **Depuración**         | Más compleja (condiciones de carrera, deadlocks)      | Compleja (IPC, deadlocks entre procesos) | Relativamente sencilla (sin condiciones de carrera de hilos)           |
| **Sintaxis**           | Tradicional (funciones y clases)                      | Tradicional (funciones y clases)         | `async`/`await` (requiere un cambio de paradigma)                      |
| **Recursos**           | Ligeros                                               | Pesados                                  | Ligeros                                                                |

### Cuándo usar cada enfoque

- **Multi-Threading (threading):**

  - Tu aplicación pasa mucho tiempo esperando operaciones de E/S (descargas de archivos, web scraping, interacción con bases de datos).
  - Necesitas compartir datos fácilmente entre "subtareas".
  - No necesitas paralelismo puro en CPU.

- **Multi-Processing (multiprocessing):**

  - Tu aplicación realiza cálculos intensivos en CPU que pueden dividirse y ejecutarse en paralelo (ej. procesamiento de imágenes, análisis de datos masivos).
  - La cantidad de datos a compartir entre tareas es manejable o las tareas son en su mayoría independientes.
  - Necesitas aprovechar todos los núcleos de tu procesador.

- **Asyncio (`async`/`await`):**
  - Estás construyendo aplicaciones altamente concurrentes basadas en E/S (servidores web, clientes de red, APIs).
  - Quieres máxima eficiencia en la gestión de miles de conexiones simultáneas.
  - Estás dispuesto a adoptar el paradigma async/await.
  - Es ideal cuando la latencia de las operaciones de E/S es el cuello de botella, no el cálculo.

## Combinando Concurrencia

Es común combinar estos enfoques en aplicaciones complejas:

- Un proceso principal puede iniciar varios procesos hijos para tareas intensivas en CPU.
- Cada proceso hijo, a su vez, puede usar hilos para manejar múltiples operaciones de E/S de forma concurrente.
- Dentro de un hilo o proceso, se puede usar `asyncio` para gestionar una gran cantidad de operaciones de E/S asíncronas de manera eficiente.
