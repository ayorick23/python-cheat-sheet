import csv

#Escribir un archivo CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Dereck", 25, "San Salvador"])
    writer.writerow(["Alejandra", 28, "Mejicanos"])
    
#Leer un archivo CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)