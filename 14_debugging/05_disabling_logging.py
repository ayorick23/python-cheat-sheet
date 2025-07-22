import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

logging.info("Este es un mensaje INFO visible.")
logging.warning("Este es un mensaje WARNING visible.")

print("\n--- Deshabilitando logging (mensajes de INFO y WARNING no se mostrarán) ---")
# Deshabilita todos los mensajes por debajo de CRITICAL (prácticamente todo)
logging.disable(logging.CRITICAL)

logging.info("Este mensaje INFO NO se mostrará.")
logging.warning("Este mensaje WARNING NO se mostrará.")
logging.error("Este mensaje ERROR NO se mostrará.") # Ni siquiera los errores

print("Logging está deshabilitado.")

print("\n--- Habilitando logging de nuevo ---")
logging.disable(logging.NOTSET) # Restablece el logging al nivel configurado (INFO)

logging.info("Este mensaje INFO es visible de nuevo.")
logging.debug("Este mensaje DEBUG NO es visible (porque el nivel base es INFO).")