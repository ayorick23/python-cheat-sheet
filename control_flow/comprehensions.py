#Lista por comprension
squares = [x**2 for x in range(10)]
print(squares)

#Diccionario por comprension
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)

#Conjunto por comprension
unique_chars = {char for char in "hello world" if char != ' '}
print(unique_chars)