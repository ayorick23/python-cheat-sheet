#Funcion lambda que sumar dos numeros
sumar = lambda x, y: x + y
print(sumar(2, 3))  # 5

#Funcion lambda con map
nums = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, nums))
print(cuadrados)  # [1, 4, 9, 16, 25]

#Funcion lambda con filter
pares = list(filter(lambda x: x % 2 == 0, nums))
print(pares)  # [2, 4]

#Funcion lambda con sorted
persons = [("Dereck", 25), ("Ale", 28), ("Cris", 15)]
ordenados = sorted(persons, key=lambda x: x[1])
print(ordenados)  # [('Cris', 15), ('Dereck', 25), ('Ale', 28)]