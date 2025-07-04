# int() - Conversión a entero
cadena_num = "123"
flotante_num = 45.67
print(f"'{cadena_num}' convertido a int: {int(cadena_num)}, tipo: {type(int(cadena_num))}") # Salida: 123, <class 'int'>
print(f"{flotante_num} convertido a int: {int(flotante_num)}, tipo: {type(int(flotante_num))}") # Salida: 45, <class 'int'> (trunca decimales)

# int() con base (para cadenas que representan números en diferentes bases)
binario_str = "1011" # 11 en decimal
print(f"'{binario_str}' (base 2) convertido a int: {int(binario_str, 2)}") # Salida: 11

# float() - Conversión a flotante
entero_num = 100
cadena_flotante = "98.76"
print(f"{entero_num} convertido a float: {float(entero_num)}, tipo: {type(float(entero_num))}") # Salida: 100.0, <class 'float'>
print(f"'{cadena_flotante}' convertido a float: {float(cadena_flotante)}, tipo: {type(float(cadena_flotante))}") # Salida: 98.76, <class 'float'>

# str() - Conversión a cadena
numero = 12345
lista_nums = [10, 20]
print(f"{numero} convertido a str: '{str(numero)}', tipo: {type(str(numero))}") # Salida: '12345', <class 'str'>
print(f"{lista_nums} convertido a str: '{str(lista_nums)}', tipo: {type(str(lista_nums))}") # Salida: '[10, 20]', <class 'str'>

# bool() - Conversión a booleano
# Casi todos los valores son True, excepto: 0, 0.0, "", [], (), {}, None
print(f"bool(0): {bool(0)}")           # Salida: False
print(f"bool(1): {bool(1)}")           # Salida: True
print(f"bool(''): {bool('')}")         # Salida: False
print(f"bool('Hola'): {bool('Hola')}") # Salida: True
print(f"bool([]): {bool([])}")         # Salida: False
print(f"bool([1, 2]): {bool([1, 2])}") # Salida: True
print(f"bool(None): {bool(None)}")     # Salida: False