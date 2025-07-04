#Crear una excepcion personalizada
class CustomError(Exception):
    pass

try:
    raise CustomError("Esto es un error personalizado")
except CustomError as e:
    print(f"Capturada una excepcion personalizada: {e}")