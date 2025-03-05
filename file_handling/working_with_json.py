import json

#Crear un diccionario y guardarlo en un archivo JSON
data = {"name": "Dereck", "age": 25, "city": "San Salvador"}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
    
#Leer un archivo JSON
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)