import logging

# Configuración básica del logging
# Establece el nivel mínimo de mensajes que se mostrarán.
# Aquí, solo se mostrarán mensajes de INFO, WARNING, ERROR y CRITICAL.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def mi_funcion_con_logs(valor):
    logging.debug(f"DEBUG: Se llamó a mi_funcion_con_logs con valor: {valor}")
    if valor < 0:
        logging.warning("WARNING: Valor negativo detectado. Esto podría causar problemas.")
    if valor == 0:
        logging.error("ERROR: Valor cero. ¡Operación crítica fallida!")
        raise ValueError("El valor no puede ser cero.")
    logging.info(f"INFO: Procesamiento exitoso para el valor: {valor}")
    logging.critical("CRITICAL: Fin de la ejecución de la función.")

print("--- Demostración de niveles de Logging ---")
try:
    mi_funcion_con_logs(10)
    print("\n--- Ejecutando con valor negativo ---")
    mi_funcion_con_logs(-5)
    print("\n--- Ejecutando con valor cero (causará error) ---")
    mi_funcion_con_logs(0)
except ValueError as e:
    print(f"Excepción capturada fuera de la función: {e}")

# Si cambias logging.basicConfig(level=logging.DEBUG, ...) verías también los mensajes DEBUG