#Uso de finally
try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print("El archivo no existe")
finally:
    print("Finalizando la operación")