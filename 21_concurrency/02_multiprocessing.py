import multiprocessing
import time
import os

def tarea_cpu_intensiva_proceso(id_tarea):
    """Simula una tarea que consume mucha CPU."""
    process_id = os.getpid()
    print(f"[Proceso {process_id}] Tarea CPU intensiva {id_tarea} comenzada...")
    # Simula cálculo intenso
    _ = [i*i for i in range(1_000_000)] # El mismo cálculo que en el ejemplo de threading
    print(f"[Proceso {process_id}] Tarea CPU intensiva {id_tarea} finalizada.")

# Ejemplo de comunicación entre procesos usando Queue
def productor(q):
    """Produce elementos y los pone en la cola."""
    for i in range(5):
        msg = f"Mensaje {i}"
        q.put(msg)
        print(f"[Productor] Puesto: {msg}")
        time.sleep(0.1)
    q.put(None) # Señal para el consumidor de que no hay más datos

def consumidor(q):
    """Consume elementos de la cola."""
    while True:
        msg = q.get()
        if msg is None: # Señal de terminación
            break
        print(f"[Consumidor] Recibido: {msg}")
        time.sleep(0.2)


print("--- Demostración de Multi-Processing ---")

# --- Escenario 1: Tareas CPU-intensivas (superando el GIL) ---
print("\n--- Ejecutando 2 Tareas CPU-Intensivas con Procesos ---")
start_time_cpu = time.perf_counter()
processes_cpu = []
for i in range(2):
    process = multiprocessing.Process(target=tarea_cpu_intensiva_proceso, args=(i+1,))
    processes_cpu.append(process)
    process.start()

for process in processes_cpu:
    process.join() # Esperar a que los procesos terminen
end_time_cpu = time.perf_counter()
print(f"Tiempo total para tareas CPU-intensivas con procesos: {end_time_cpu - start_time_cpu:.4f} segundos.")
# Notarás que el tiempo es casi la mitad de lo que tomaría una sola tarea,
# demostrando el paralelismo real en CPU gracias a los procesos.

# --- Escenario 2: Comunicación Inter-Procesos (IPC) con Queue ---
print("\n--- Demostración de IPC con Queue ---")
q = multiprocessing.Queue()
p_prod = multiprocessing.Process(target=productor, args=(q,))
p_cons = multiprocessing.Process(target=consumidor, args=(q,))

p_prod.start()
p_cons.start()

p_prod.join()
p_cons.join()
print("Comunicación IPC con Queue finalizada.")