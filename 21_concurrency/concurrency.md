# Concurrency

La **concurrencia** se refiere a la capacidad de un sistema para manejar múltiples tareas en progreso "al mismo tiempo". Esto no significa necesariamente que las tareas se ejecuten simultáneamente (en paralelo puro), sino que la ejecución de una tarea puede superponerse con la ejecución de otra. El objetivo es maximizar la utilización de los recursos y mejorar la capacidad de respuesta.

En Python, el principal obstáculo para el paralelismo puro (ejecución simultánea) en CPU es el **GIL (_Global Interpreter Lock_)**.

## El GIL (_Global Interpreter Lock_)

El GIL es un mecanismo de Python que asegura que solo un hilo a la vez pueda ejecutar bytecode de Python en el intérprete CPython. Esto significa que, incluso en una máquina con múltiples núcleos de CPU, un programa Python multi-hilo no puede aprovechar esos núcleos para tareas intensivas de CPU de forma paralela.

**¿Por qué existe el GIL?** Principalmente para simplificar la gestión de memoria y evitar condiciones de carrera en la manipulación de objetos Python por parte de múltiples hilos, lo que haría el intérprete mucho más complejo y propenso a errores.

### Implicaciones del GIL

- **Tareas intensivas en CPU:** Para operaciones que requieren mucho cálculo (ej. procesamiento de datos, algoritmos complejos), el multi-threading no ofrecerá mejoras de rendimiento reales en CPython, ya que el GIL limitará la ejecución a un solo núcleo.
- **Tareas intensivas en E/S (Input/Output):** Para operaciones que esperan la finalización de E/S (ej. lectura/escritura de archivos, solicitudes de red, interacción con bases de datos), el GIL libera el bloqueo mientras el hilo está esperando la operación de E/S. Esto significa que otros hilos pueden ejecutarse, mejorando significativamente la capacidad de respuesta y el rendimiento en estos escenarios.
-
