from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Definición de un modelo de datos con Pydantic
class Libro(BaseModel):
    id: int
    titulo: str
    autor: str
    
# Simulación de una base de datos en memoria
libros_db = [
    Libro(id=1, titulo='El señor de los anillos', autor='J.R.R. Tolkien'),
    Libro(id=2, titulo='Cien años de soledad', autor='Gabriel García Márquez')
]

# Endpoint para obtener todos los libros
@app.get('/libros', response_model=List[Libro])
async def obtener_libros():
    """Retorna una lista de todos los libros."""
    return libros_db

# Endpoint para obtener un libro por su ID
@app.get('/libros/{id}', response_model=Libro)
async def obtener_libro_por_id(id: int):
    """Retorna un libro específico por su ID."""
    libro_encontrado = next((libro for libro in libros_db if libro.id == id), None)
    if libro_encontrado:
        return libro_encontrado
    raise HTTPException(status_code=404, detail="Libro no encontrado")

# Endpoint para crear un nuevo libro
@app.post('/libros', response_model=Libro, status_code=201)
async def crear_libro(libro: Libro):
    """Crea un nuevo libro."""
    libros_db.append(libro)
    return libro

# Para ejecutar la API de FastAPI:

# 1. Asegúrate de que fastapi y uvicorn estén instalados.
# 2. Ejecuta el script desde la terminal:
# ```bash
# uvicorn 04_api_fastapi:app --reload
# ```
# 3. La API estará disponible en http://127.0.0.1:8000/.
# 4. Para ver la documentación interactiva (¡una de las mejores características!):
#   - Abre tu navegador y ve a http://127.0.0.1:8000/docs. Podrás probar los endpoints
#     directamente desde allí.