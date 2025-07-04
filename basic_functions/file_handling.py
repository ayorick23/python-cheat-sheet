def writeFile(filename, content):
    #Escribe contenido en un archivo
    with open(filename, "w") as file:
        file.write(content)
        
def readFile(filename):
    #Lee el contenido de un archivo
    with open(filename, "r") as file:
        return file.read()
    
if __name__ == "__main__":
    writeFile("example.txt", "Hola Mundo!")
    print(readFile("example.txt"))