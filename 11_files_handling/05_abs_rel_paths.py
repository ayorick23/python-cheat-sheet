import os
from pathlib import Path

# Directorio de trabajo actual
cwd = os.getcwd()
print(f"Directorio de trabajo actual: {cwd}")

# Ruta relativa
ruta_relativa = "mi_carpeta/archivo.txt"

# Convertir a absoluta con os.path.abspath
ruta_absoluta_os = os.path.abspath(ruta_relativa)
print(f"Ruta relativa '{ruta_relativa}' a absoluta (os): {ruta_absoluta_os}")

# Convertir a absoluta con pathlib.Path.resolve()
ruta_relativa_pathlib = Path("mi_carpeta_pb/archivo_pb.txt")
# Creamos la carpeta para que resolve() no dé error si no existe el padre
ruta_relativa_pathlib.parent.mkdir(parents=True, exist_ok=True)
ruta_absoluta_pathlib = ruta_relativa_pathlib.resolve()
print(f"Ruta relativa '{ruta_relativa_pathlib}' a absoluta (pathlib): {ruta_absoluta_pathlib}")

# Calcular ruta relativa
ruta_destino = os.path.join(cwd, "directorio_destino", "sub", "archivo_final.txt")
os.makedirs(os.path.dirname(ruta_destino), exist_ok=True) # Asegurarse que el directorio existe

ruta_relativa_calc_os = os.path.relpath(ruta_destino, start=cwd)
print(f"Ruta relativa de '{ruta_destino}' desde '{cwd}': {ruta_relativa_calc_os}")

# Calcular ruta relativa con pathlib
ruta_destino_pb = Path(cwd) / "directorio_destino_pb" / "sub_pb" / "archivo_final_pb.txt"
ruta_destino_pb.parent.mkdir(parents=True, exist_ok=True)

ruta_relativa_calc_pathlib = ruta_destino_pb.relative_to(Path.cwd())
print(f"Ruta relativa de '{ruta_destino_pb}' desde '{Path.cwd()}' (pathlib): {ruta_relativa_calc_pathlib}")