import requests
import json

def obtener_posts():
    """
    Realiza una solicitud GET a una API pública para obtener una lista de posts.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    print(f"Haciendo solicitud GET a: {url}")
    
    try:
        # La función get() retorna un objeto Response
        response = requests.get(url)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            print(f"Solicitud exitosa. Código de estado: {response.status_code}")
            
            # response.json() convierte la respuesta JSON a un objeto Python (lista de diccionarios)
            posts = response.json()
            
            # Imprimir los primeros 3 posts para no saturar la consola
            print(f"\nSe obtuvieron {len(posts)} posts. Mostrando los primeros 3:")
            for post in posts[:3]:
                print(f"  - ID: {post['id']}, Título: {post['title'][:30]}...")
            
            return posts
        else:
            print(f"Error en la solicitud. Código de estado: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

if __name__ == "__main__":
    posts_obtenidos = obtener_posts()