# String Formatting

El formato de cadenas permite insertar variables y valores en una plantilla de texto de manera controlada.

## Operador `%`

Este es el método de formato más antiguo de Python, similar a la función `printf` de **C**. Aunque todavía se encuentra en código heredado, no se recomienda para código nuevo debido a su falta de legibilidad y versatilidad.

```python
'Cadena de texto con un %especificador' % (variable_o_valor)
```

Los especificadores comunes incluyen:

- `%s`: para cadenas (strings)
- `%d`: para enteros (decimales)
- `%f`: para flotantes
- `%.2f`: para flotantes con 2 decimales
- `%r`: representación de la cadena (útil para depuración)

## Método `str.format()`

Introducido en Python 2.6, este método fue una mejora significativa sobre el operador `%`. Utiliza llaves `{}` como marcadores de posición, lo que hace que la sintaxis sea más clara. Puedes referenciar variables por su posición o por su nombre.

```python
'Cadena de texto con {} y {}.'.format(valor1, valor2)
'Cadena de texto con {clave1} y {clave2}.'.format(clave1=valor1, clave2=valor2)
```

## F-Strings (_Formatted String Literals_)

Introducidas en Python 3.6, las f-**strings** son la forma más recomendada, moderna y eficiente de formatear cadenas. Son literales de cadena con una `f` o `F` al principio, y te permiten incrustar expresiones de Python directamente dentro de las llaves `{}`.

```python
f"Cadena de texto con {variable} y {expresion_python}."
```

## Características Avanzadas de F-Strings

Las f-strings no solo son convenientes, sino que también ofrecen potentes herramientas de formato.

### 1. El Especificador `=` para Depuración

Este especificador es increíblemente útil para la depuración. Dentro de una f-string, `variable=` muestra el nombre de la variable, el signo `=` y su valor.

### 2. Agregar Espacios o Caracteres (Relleno)

Puedes controlar el ancho y la alineación de la salida.

```python
{valor:ancho_total}
# o
{valor:caracter_relleno<ancho_total}
```

- `<`: Alineación a la izquierda (por defecto para cadenas)
- `>`: Alineación a la derecha (por defecto para números)
- `^`: Alineación al centro

### 3. Formatear Dígitos como Separador de Miles

Usa la coma `,` o el guion bajo `_` para formatear números y mejorar su legibilidad.

### 4. Redondeo, Mostrar Porcentaje y Formato Numérico

- **Redondeo (`.nf`)**: Formatea un número flotante con `n` decimales.
- **Porcentaje (`%`)**: Multiplica el número por 100 y le añade el signo de porcentaje.

#### Tabla de Formato de Números

| Número       | Formato   | Salida      | Descripción                                                  |
| ------------ | --------- | ----------- | ------------------------------------------------------------ |
| `3.1415926`  | `{:.2f}`  | `3.14`      | Formato float 2 decimales                                    |
| `3.1415926`  | `{:+.2f}` | `+3.14`     | Formato float 2 decimales con signo                          |
| `-1`         | `{:+.2f}` | `-1.00`     | Formato float 2 decimales con signo                          |
| `2.71828`    | `{:.0f}`  | `3`         | Formato float sin decimales                                  |
| `4`          | `{:0>2d}` | `04`        | Número de almohadilla con ceros (relleno izquierdo, ancho 2) |
| `4`          | `{:x<4d}` | `4xxx`      | Número de almohadilla con x's (relleno derecho, ancho 4)     |
| `10`         | `{:x<4d}` | `10xx`      | Número de almohadilla con x (relleno derecho, ancho 4)       |
| `1000000`    | `{:,}`    | `1,000,000` | Formato de número con separador de miles                     |
| `0.35`       | `{:.2%}`  | `35.00%`    | Formato de porcentaje                                        |
| `1000000000` | `{:.2e}`  | `1.00e+09`  | Notación de exponentes                                       |
| `11`         | `{:11d}`  | `11`        | Alineado a la derecha (predeterminado, ancho 10)             |
| `11`         | `{:<11d}` | `11`        | Alineado a la izquierda (ancho 10)                           |
| `11`         | `{:^11d}` | `11`        | Alineado al centro (ancho 10)                                |

### 5. Cadenas de Plantillas (string.Template)

El módulo `string.Template` proporciona una forma sencilla y segura de formatear cadenas, especialmente útil cuando el texto de la plantilla proviene de una fuente externa (como un usuario) y necesitas evitar la ejecución de código malicioso.

```python
from string import Template

plantilla = Template('Texto con marcadores como $variable.')
plantilla.substitute(variable=valor)
```

- Los marcadores de posición comienzan con `$`.
