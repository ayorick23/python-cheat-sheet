# Control Flow

Los flujos de control dictan el orden en que se ejecutan las instrucciones en un programa. Permiten que tu código responda a diferentes condiciones y realice tareas repetitivas de manera eficiente.

## Sentencias Condicionales: `if`, `elif`, `else`

Las sentencias `if`, `elif` (abreviatura de "`else if`") y `else` se utilizan para ejecutar diferentes bloques de código basándose en condiciones booleanas.

```python
if condicion1:
    # Bloque de código si condicion1 es True
elif condicion2:
    # Bloque de código si condicion2 es True
elif condicion3:
    # Bloque de código si condicion3 es True
else:
    # Bloque de código si ninguna de las condiciones anteriores es True
```

- Python usa la indentación (espacios o tabulaciones) para definir los bloques de código. Esto es crucial y no opcional como en otros lenguajes.
- Se evalúa la primera condición. Si es `True`, se ejecuta su bloque de código y el resto de la estructura `elif`/`else` se salta.
- Si la primera condición es `False`, se evalúa la siguiente `elif`, y así sucesivamente.
- Si ninguna condición `if` o `elif` es `True`, se ejecuta el bloque `else` (si existe).

## Operador Condicional Ternario

El operador condicional ternario es una forma concisa de escribir una sentencia `if`-`else` en una sola línea, a menudo utilizada para asignaciones de variables basadas en una condición.

```python
valor_si_verdadero if condicion else valor_si_falso
```

## Estructura `match`-`case`

Python no tiene un switch-case tradicional como C++ o Java. Sin embargo, a partir de Python 3.10, se introdujo la sentencia `match`-`case` (conocida como _"Structural Pattern Matching"_) que ofrece una funcionalidad similar y mucho más potente.

```python
match valor_o_expresion:
    case patron1:
        # Bloque de código si el valor coincide con patron1
    case patron2:
        # Bloque de código si el valor coincide con patron2
    case patron3 | patron4: # Coincidencia OR
        # Bloque de código si el valor coincide con patron3 o patron4
    case patron_con_guard if condicion_adicional: # Coincidencia con 'guard'
        # Bloque de código si el valor coincide Y la condición adicional es True
    case [a, b, c]: # Coincidencia con estructuras de datos (listas, tuplas)
        # Accede a los elementos como a, b, c
    case {'clave': valor_deseado}: # Coincidencia con diccionarios
        # Accede al valor_deseado
    case _: # Patrón comodín (equivalente a 'default')
        # Bloque de código si no hay ninguna coincidencia anterior
```

- **Coincidencia de Patrones:** Puede coincidir con valores literales, variables, secuencias, diccionarios y objetos.
- **Captura de Valores:** Puedes "capturar" partes del valor coincidente en variables.
- **Operador `|` (OR):** Permite combinar múltiples patrones en un solo `case`.
- **Condiciones `if` (Guards):** Permite añadir una condición adicional que debe ser `True` para que el `case` coincida.
- **Default `_`:** Actúa como un `default` o `else` para capturar cualquier cosa que no haya coincidido con patrones anteriores.
- **Coincidencias con Clases Built-in:** Puedes usar `case` para emparejar tipos específicos o estructuras de datos como listas o diccionarios.
- **Longitud de un Iterable:** Puedes inferir o emparejar por la longitud implícitamente al emparejar la estructura.

## Bucle `while`

El bucle `while` ejecuta un bloque de código repetidamente mientras una condición sea verdadera.

```python
while condicion:
    # Bloque de código que se ejecuta repetidamente
    # (Asegúrate de que la condición eventualmente se vuelva False para evitar un bucle infinito)
```

### Declaraciones de control de bucle

- `break`: Termina completamente el bucle y la ejecución continúa con la sentencia siguiente al bucle.
- `continue`: Salta la iteración actual del bucle y pasa a la siguiente iteración.

## Bucle `do`-`while`

Python no tiene una sentencia `do`-`while` nativa como otros lenguajes. Un bucle `do`-`while` garantiza que el bloque de código se ejecute al menos una vez antes de que se verifique la condición.

En Python, puedes emular este comportamiento combinando un bucle `while True` con una sentencia `if` y `break`, o inicializando una variable de control para que la condición del `while` sea verdadera en la primera iteración.

```python
while True:
    # Bloque de código que se ejecutará al menos una vez
    # ...
    if not condicion: # O if condicion_para_salir:
        break
    # ... (código que se ejecuta si la condición es verdadera para continuar)
```

## Bucle `for`

El bucle `for` se utiliza para iterar sobre los elementos de un iterable (como listas, tuplas, cadenas, diccionarios, conjuntos) o para ejecutar un bloque de código un número específico de veces usando la función `range()`.

```python
for elemento in iterable:
    # Bloque de código para cada elemento
```

## Listas por Comprensión

Las listas por comprensión son una forma concisa de crear nuevas listas a partir de iterables existentes, aplicando una expresión a cada elemento y, opcionalmente, incluyendo una condición para filtrar elementos. Son una alternativa más legible y a menudo más eficiente que usar bucles `for` tradicionales para crear listas.

```python
nueva_lista = [expresion for elemento in iterable if condicion]
```

- `expresion`: El valor que se incluirá en la nueva lista por cada elemento. Puede ser cualquier operación o cálculo.
- `for elemento in iterable`: Un bucle `for` que itera sobre el `iterable` (_lista, tupla, rango, etc._).
- `if condicion`: Una condición opcional que filtra los elementos. Solo se procesarán aquellos elementos que cumplan la condición.
