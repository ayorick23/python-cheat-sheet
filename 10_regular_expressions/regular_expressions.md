# Regular Expressions (_RegEx_)

Las **expresiones regulares** son herramientas para encontrar patrones en texto. Pueden usarse para tareas como validar formatos de entrada, extraer información específica o reemplazar texto.

## Importa Módulo

Para trabajar con expresiones regulares en Python, siempre debes importar el módulo `re`.

```python
import re
```

## Símbolos de Expresiones Regulares

| Símbolo                  | Coincidencia                                                                 |
| ------------------------ | ---------------------------------------------------------------------------- |
| `?`                      | Cero o una del grupo que le precede.                                         |
| `*`                      | Cero o más del grupo que le precede.                                         |
| `+`                      | Una o más del grupo que le precede.                                          |
| `{n}`                    | Exactamente `n` del grupo que le precede.                                    |
| `{n,}`                   | Una o más del grupo que le precede.                                          |
| `{,m}`                   | 0 a `m` del grupo que le precede.                                            |
| `{n,m}`                  | Al menos `n` y como máximo `m` del grupo que le precede.                     |
| `{n,m}?` or `*?` or `+?` | Realiza una coincidencia no codiciosa del grupo que le precede.              |
| `^spam`                  | Significa que la cadena debe comenzar con `spam`.                            |
| `spam$`                  | Significa que la cadena debe terminar con `spam`.                            |
| `.`                      | Cualquier carácter, excepto caracteres de nueva línea.                       |
| `\d`, `\w`, and `\s`     | Un dígito, una palabra o un carácter de espacio, respectivamente.            |
| `\D`, `\W`, and `\S`     | Cualquier cosa excepto un dígito, una palabra o un espacio, respectivamente. |
| `[abc]`                  | Cualquier carácter entre corchetes (como a, b, c).                           |
| `[^abc]`                 | Cualquier carácter que no esté entre corchetes.                              |

## Uso de `re.compile()`

Compilar una expresión regular con `re.compile()` la convierte en un objeto de expresión regular. Esto es útil si vas a usar la misma expresión regular varias veces en tu código, ya que mejora el rendimiento.

```python
import re
patron = re.compile(r'mi_patron')
```

La `r` antes de la cadena (`r'mi_patron'`) es importante. Indica una "raw string" (cadena cruda), lo que significa que las barras invertidas (`\`) no se tratan como secuencias de escape normales de Python, lo cual es crucial para RegEx donde `\` se usa a menudo para caracteres especiales.

## Coincidencia de Objetos (Match Object)

Cuando una expresión regular encuentra una coincidencia, los métodos como `re.search()` o `re.match()` devuelven un objeto de coincidencia (Match object). Este objeto contiene información sobre la coincidencia, incluyendo el texto coincidente, su posición, etc. Si no hay coincidencia, devuelven `None`.

- `re.search(patron, cadena)`: Busca la primera ocurrencia del patrón en la cadena y devuelve un objeto de coincidencia.
- `re.match(patron, cadena)`: Busca el patrón solo al principio de la cadena.

## Agrupación con Paréntesis `()` y Método `groups()`

Los paréntesis `()` en una expresión regular sirven para agrupar partes del patrón. Esto te permite extraer subcadenas específicas de una coincidencia. El método `group(n)` de un objeto de coincidencia devuelve el texto de un grupo específico, y `groups()` devuelve una tupla con todos los grupos.

- `group(0)` o `group()`: Devuelve toda la coincidencia.
- `group(1)`: Devuelve el contenido del primer grupo entre paréntesis.
- `group(n)`: Devuelve el contenido del n-ésimo grupo.
- `groups()`: Devuelve una tupla de todas las subcadenas coincidentes para todos los grupos

## Grupos con Pipe `|` (OR lógico)

El carácter `|` actúa como un operador "OR" lógico dentro de una expresión regular, permitiéndote coincidir con cualquiera de varios patrones.

```python
(patron1|patron2|patron3)
```

## Coincidencias con el Signo de Interrogación `?` (Cero o Una Vez)

El signo de interrogación `?` hace que el elemento que le precede sea opcional, es decir, coincidirá cero o una vez.

```python
elemento?
```

## Coincidencias con Estrella o Asterisco `*` (Cero o Más Veces)

El asterisco `*` indica que el elemento que le precede puede aparecer cero o más veces.

```python
elemento*
```

## Coincidencias con el Signo Más `+` (Una o Más Veces)

El signo más `+` indica que el elemento que le precede debe aparecer una o más veces.

```python
elemento+
```

## Coincidencias con Llaves `{}` (Rangos de Repetición)

Las llaves `{}` te permiten especificar el número exacto de repeticiones o un rango para el elemento precedente.

- `elemento{n}`: n veces exactamente.
- `elemento{n,}`: n o más veces.
- `elemento{n,m}`: entre n y m veces (inclusive).

## Emparejamiento Codicioso (Greedy) y No Codicioso (Non-Greedy)

Por defecto, los cuantificadores (`*`, `+`, `?`, `{}`) son codiciosos (greedy). Esto significa que intentan coincidir con la cadena más larga posible. Para hacerlos no codiciosos (non-greedy), añade un `?` después del cuantificador. Esto hace que coincidan con la cadena más corta posible.

```python
cuantificador? # (ej. .*?, +?, ??, {n,m}?)
```

## Método `re.findall()`

El método `re.findall()` devuelve una lista de todas las subcadenas no superpuestas que coinciden con el patrón en la cadena dada. Es una de las funciones más utilizadas para extraer datos de texto.

```python
re.findall(patron, cadena)
```

## Creación de Propias Clases de Caracteres `[]`

Puedes definir tus propias clases de caracteres usando corchetes `[]`. Esto coincide con cualquier carácter dentro de los corchetes.

```python
[caracteres]
```

- `[aeiou]`: Coincide con cualquier vocal en minúscula.
- `[0-9]`: Coincide con cualquier dígito (equivalente a `\d`).
- `[a-zA-Z]`: Coincide con cualquier letra (mayúscula o minúscula).
- `[^abc]`: Coincide con cualquier carácter excepto 'a', 'b' o 'c'. (El `^` al principio de `[]` niega el conjunto).

## Anclajes: Signo de Intercalación `^` y Signo de Dólar `$`

Estos caracteres no coinciden con caracteres, sino con posiciones en la cadena.

- `^` **(Inicio de la cadena):** Coincide con el inicio de la cadena.
- `$` **(Fin de la cadena):** Coincide con el fin de la cadena.

## Carácter Comodín `.` (Cualquier Carácter Excepto Nueva Línea)

El punto `.` (punto) es un comodín que coincide con cualquier carácter excepto un salto de línea (`\n`).

## Combinación `.*` (Cero o Más de Cualquier Carácter)

La combinación `.*` es muy común y significa "cero o más de cualquier carácter (excepto nueva línea)". Se usa a menudo para "saltar" un número arbitrario de caracteres.

```python
.*  # (codicioso por defecto)
.*? # (no codicioso)
```

## Coincidencias de Nuevas Líneas con el Punto (`re.DOTALL`)

Por defecto, el punto `.` no coincide con el carácter de nueva línea (`\n`). Si quieres que el punto también coincida con saltos de línea, usa el flag `re.DOTALL` (o `re.S`).

```python
re.compile(patron, re.DOTALL)
```

## Coincidencias sin Distinción entre Mayúsculas y Minúsculas (`re.IGNORECASE`)

Para hacer que tu búsqueda de patrones no distinga entre mayúsculas y minúsculas, usa el flag `re.IGNORECASE` (o `re.I`).

```python
re.compile(patron, re.IGNORECASE)
```

## Método `re.sub()` (Sustitución)

El método `re.sub()` se utiliza para reemplazar todas las ocurrencias de un patrón en una cadena con una cadena de reemplazo.

```python
re.sub(patron, reemplazo, cadena[, count])
```

- `patron`: La expresión regular a buscar.
- `reemplazo`: La cadena con la que se sustituirá la coincidencia. Puede incluir referencias a grupos (ej. `\1`).
- `cadena`: La cadena original donde buscar y reemplazar.
- `count`: (Opcional) El número máximo de reemplazos a realizar.

## Gestión de Expresiones Regulares Complejas (`re.VERBOSE`)

Para expresiones regulares muy largas o complejas, el flag `re.VERBOSE` (o `re.X`) permite añadir espacios en blanco y comentarios dentro del patrón, mejorando enormemente la legibilidad.

```python
patron_complejo = re.compile(r"""
    ^                  # Inicio de la cadena
    (\d{3})            # Grupo 1: Tres dígitos
    -?                 # Guion opcional
    (\d{3})            # Grupo 2: Tres dígitos
    -                  # Guion obligatorio
    (\d{4})            # Grupo 3: Cuatro dígitos
    $                  # Fin de la cadena
""", re.VERBOSE)
```
