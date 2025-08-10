import requests
import json

def crear_post(titulo, cuerpo, usuario_id):
    """
    Realiza una solicitud POST a una API para crear un nuevo post.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Datos que se enviarán en el cuerpo de la solicitud
    nuevo_post = {
        'title': titulo,
        'body': cuerpo,
        'userId': usuario_id
    }
    
    print(f"Haciendo solicitud POST a: {url} con datos: {nuevo_post}")

    try:
        # La función post() envía los datos en formato JSON automáticamente
        response = requests.post(url, json=nuevo_post)
        
        if response.status_code == 201: # 201 Created es el código para creación exitosa
            print(f"Post creado exitosamente. Código de estado: {response.status_code}")
            
            # La respuesta generalmente incluye el objeto creado con su nuevo ID
            post_creado = response.json()
            print(f"Respuesta del servidor: {post_creado}")
            print(f"Nuevo post creado con ID: {post_creado['id']}")
            return post_creado
        else:
            print(f"Error al crear el post. Código de estado: {response.status_code}")
            print(f"Respuesta del servidor: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

if __name__ == "__main__":
    crear_post("Mi primer post", "Este es el cuerpo de mi primer post.", 1)