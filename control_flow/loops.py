#Bucle for
for i in range(5):
    print(f"Iteracion {i}")

#Bucle while
count = 0
while count < 5:
    print(f"Contador: {count}")
    count += 1

#Uso de break
i = 0
while i < 10:
    if i == 5:
        break #Sale del bucle cuando i es igual a 5
    print(i)
    i += 1

#Uso de continue
i = 0
while i < 10:
    if i == 5:
        continue #Omite la iteracion cuando i es igual a 5
    print(i)
    i += 1