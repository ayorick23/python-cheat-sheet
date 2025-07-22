import logging
import os

log_file_name = "mi_aplicacion.log"

# Configurar el logger para escribir en un archivo
# El archivo se creará o se añadirá a él si ya existe
logging.basicConfig(
    filename=log_file_name,
    filemode='w', # 'w' para sobrescribir cada vez que el script se ejecuta, usa 'a' para añadir
    level=logging.DEBUG, # Establece el nivel más bajo para capturar todo en el archivo
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Puedes obtener un logger específico por nombre (buenas prácticas)
logger = logging.getLogger(__name__) # __name__ se refiere al nombre del módulo actual

logger.debug("Mensaje de depuración detallado.")
logger.info("El programa ha iniciado correctamente.")

try:
    resultado = 10 / 0
except ZeroDivisionError:
    logger.error("¡Se intentó una división por cero!", exc_info=True) # exc_info=True añade el traceback al log
    # Puedes usar logger.exception() directamente en un except, que automáticamente añade exc_info
    # logger.exception("¡Se intentó una división por cero!") # Más conciso

logger.warning("Algunas operaciones pueden haber fallado.")
logger.critical("El sistema está a punto de apagarse.")

print(f"Los logs se han escrito en '{log_file_name}'.")

# Opcional: Mostrar el contenido del archivo de log para verificar
print(f"\n--- Contenido de '{log_file_name}' ---")
try:
    with open(log_file_name, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Archivo de log no encontrado.")

# Limpieza
os.remove(log_file_name)