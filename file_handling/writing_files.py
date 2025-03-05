#Escribir en un archivo (sobrescribe el contenido existente)
with open("output.txt", "w") as file:
    file.write("Hello world!\n")
    file.write("Writing to a file in Python.\n")
    
#Agregar contenido a un archivo existente
with open("output.txt", "a") as file:
    file.write("Appending a new line.\n")