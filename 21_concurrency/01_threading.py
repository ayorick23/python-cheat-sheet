import threading
import time
import requests

def tarea_cpu_intensiva(id_tarea):
    """Simula una tarea que consume mucha CPU."""
    print(f"[{threading.current_thread().name}] Tarea CPU intensiva {id_tarea} comenzada...")
    # Simula cálculo intenso
    _ = [i*i for i in range(1_000_000)]
    print(f"[{threading.current_thread().name}] Tarea CPU intensiva {id_tarea} finalizada.")

def tarea_io_intensiva(url, id_tarea):
    """Simula una tarea que espera por E/S (red)."""
    print(f"[{threading.current_thread().name}] Tarea I/O intensiva {id_tarea} comenzada (descargando {url})...")
    try:
        response = requests.get(url, timeout=5) # El GIL se libera durante la espera de la red
        print(f"[{threading.current_thread().name}] Tarea I/O intensiva {id_tarea} finalizada. Tamaño: {len(response.text)} bytes.")
    except requests.exceptions.RequestException as e:
        print(f"[{threading.current_thread().name}] Tarea I/O intensiva {id_tarea} fallida: {e}")

print("--- Demostración de Multi-Threading ---")

# --- Escenario 1: Tareas CPU-intensivas (donde el GIL impacta) ---
print("\n--- Ejecutando 2 Tareas CPU-Intensivas con Hilos ---")
start_time_cpu = time.perf_counter()
threads_cpu = []
for i in range(2):
    thread = threading.Thread(target=tarea_cpu_intensiva, args=(i+1,), name=f"CPU-Thread-{i+1}")
    threads_cpu.append(thread)
    thread.start()

for thread in threads_cpu:
    thread.join() # Esperar a que los hilos terminen
end_time_cpu = time.perf_counter()
print(f"Tiempo total para tareas CPU-intensivas con hilos: {end_time_cpu - start_time_cpu:.4f} segundos.")
# Notarás que el tiempo es casi el doble de lo que tomaría una sola tarea,
# confirmando el impacto del GIL en tareas CPU.

# --- Escenario 2: Tareas I/O-intensivas (donde el GIL ayuda) ---
print("\n--- Ejecutando 3 Tareas I/O-Intensivas con Hilos ---")
urls = [
    "https://www.google.com",
    "https://www.bing.com",
    "https://www.python.org"
]
start_time_io = time.perf_counter()
threads_io = []
for i, url in enumerate(urls):
    thread = threading.Thread(target=tarea_io_intensiva, args=(url, i+1,), name=f"IO-Thread-{i+1}")
    threads_io.append(thread)
    thread.start()

for thread in threads_io:
    thread.join() # Esperar a que los hilos terminen
end_time_io = time.perf_counter()
print(f"Tiempo total para tareas I/O-intensivas con hilos: {end_time_io - start_time_io:.4f} segundos.")
# Notarás que el tiempo es significativamente menor que la suma de los tiempos individuales,
# ya que los hilos pueden operar mientras otros esperan la E/S.