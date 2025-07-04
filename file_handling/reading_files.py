#Abrir un archivo en modo lectura
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    
#Leer linea por linea
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())