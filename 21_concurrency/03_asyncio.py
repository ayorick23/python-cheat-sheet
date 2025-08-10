import asyncio
import time
import aiohttp # Necesitarás instalar esta librería: pip install aiohttp

async def tarea_lenta_io(url, id_tarea):
    """Simula una tarea asíncrona que espera por E/S (red)."""
    print(f"[Asyncio] Tarea I/O asíncrona {id_tarea} comenzada (descargando {url})...")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as response:
                text = await response.text() # await cede el control
                print(f"[Asyncio] Tarea I/O asíncrona {id_tarea} finalizada. Tamaño: {len(text)} bytes.")
    except aiohttp.ClientError as e:
        print(f"[Asyncio] Tarea I/O asíncrona {id_tarea} fallida: {e}")

async def main_asyncio():
    """Función principal para coordinar las tareas asíncronas."""
    print("--- Demostración de Asyncio ---")
    
    urls = [
        "https://www.google.com",
        "https://www.bing.com",
        "https://www.python.org",
        "https://www.example.com",
        "https://www.github.com"
    ]

    start_time_async = time.perf_counter()
    
    # Crear una lista de coroutines (tareas)
    tasks = []
    for i, url in enumerate(urls):
        tasks.append(tarea_lenta_io(url, i+1))
    
    # Ejecutar todas las tareas concurrentemente y esperar a que terminen
    await asyncio.gather(*tasks)
    
    end_time_async = time.perf_counter()
    print(f"Tiempo total para tareas I/O asíncronas con Asyncio: {end_time_async - start_time_async:.4f} segundos.")

# Para ejecutar la función asíncrona principal
if __name__ == "__main__":
    asyncio.run(main_asyncio())