from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulación de una base de datos en memoria
libros = [
    {'id': 1, 'titulo': 'El señor de los anillos', 'autor': 'J.R.R. Tolkien'},
    {'id': 2, 'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez'}
]

# Endpoint para obtener todos los libros
@app.route('/libros', methods=['GET'])
def obtener_libros():
    """Retorna una lista de todos los libros."""
    print("GET en /libros")
    return jsonify({'libros': libros})

# Endpoint para obtener un libro por su ID
@app.route('/libros/<int:id>', methods=['GET'])
def obtener_libro_por_id(id):
    """Retorna un libro específico por su ID."""
    print(f"GET en /libros/{id}")
    libro_encontrado = next((libro for libro in libros if libro['id'] == id), None)
    if libro_encontrado:
        return jsonify(libro_encontrado)
    return jsonify({'mensaje': 'Libro no encontrado'}), 404

# Endpoint para crear un nuevo libro
@app.route('/libros', methods=['POST'])
def crear_libro():
    """Crea un nuevo libro."""
    print("POST en /libros")
    nuevo_libro = {
        'id': len(libros) + 1,
        'titulo': request.json['titulo'],
        'autor': request.json['autor']
    }
    libros.append(nuevo_libro)
    return jsonify(nuevo_libro), 201

if __name__ == '__main__':
    app.run(debug=True)
    
# Para ejecutar la API de Flask:

# 1. Asegúrate de que Flask esté instalado.
# 2. Ejecuta el script: python 03_api_flask.py.
# 3. La API estará disponible en http://127.0.0.1:5000/.

# Cómo interactuar con la API de Flask:

# - GET /libros
# Abre tu navegador y ve a http://127.0.0.1:5000/libros para ver la lista completa.
# - GET /libros/1
# Ve a http://127.0.0.1:5000/libros/1 para ver el libro con ID 1.
# - POST /libros
# Necesitas una herramienta como cURL o Postman.
# Ejecuta en tu terminal:
# ```bash
# curl -X POST -H "Content-Type: application/json" -d '{"titulo": "1984", "autor": "George Orwell"}' http://127.0.0.1:5000/libros
# ```