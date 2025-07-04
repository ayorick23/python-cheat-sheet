# Introduction to Python

**Python** es un lenguaje de programación de alto nivel, interpretado, con semántica dinámica y multipropósito. Se caracteriza por su sintaxis clara y legible, lo que facilita el aprendizaje y la escritura de código conciso. Python es ampliamente utilizado en diversas áreas como desarrollo web, análisis de datos, inteligencia artificial y scripting.

## Características principales

- **Interpretado:** Python es un lenguaje interpretado, lo que significa que el código se ejecuta línea por línea por un intérprete en lugar de ser compilado a código máquina antes de su ejecución.
- **Tipado dinámico:** Python no requiere que se especifiquen los tipos de datos de las variables, permitiendo una mayor flexibilidad en el código.
- **Sintaxis clara:** La sintaxis de Python es similar al inglés, lo que lo hace más fácil de aprender y leer.
- **Multiproposito:** Python se puede utilizar para una amplia gama de tareas, desde scripts simples hasta aplicaciones complejas.
- **Código abierto:** Python es un lenguaje de código abierto, lo que significa que es gratuito y cualquier persona puede acceder al código fuente y modificarlo.

## Operadores Básicos

Los operadores son símbolos que le indican al intérprete que realice una operación específica, como aritmética, comparación, lógica, etc.

### Operadores Aritméticos

Un operador aritmético toma dos operandos como entrada, realiza un cálculo y devuelve el resultado.

**De mayor a menor precedencia:**

| Operador | Descripción                                        | Uso             |
| -------- | -------------------------------------------------- | --------------- |
| `**`     | Realiza la potencia de los operandos               | `2 ** 3 = 8`    |
| `%`      | Realiza un módulo entre los operandos              | `22 % 8 = 6`    |
| `//`     | Realiza la división con resultado de número entero | `22 // 8 = 2`   |
| `/`      | Realiza División entre los operandos               | `22 / 8 = 2.75` |
| `*`      | Realiza Multiplicación entre los operandos         | `3 * 3 = 9`     |
| `-`      | Realiza Substracción entre los operandos           | `5 - 2 = 3`     |
| `+`      | Realiza Adición entre los operandos                | `2 + 2 = 4`     |

### Operadores Relacionales

Un operador relacional se emplea para comparar y establecer la relación entre ellos. Devuelve un valor booleano (true o false) basado en la condición.

| Operador | Descripción                                                                                   | Uso                        |
| -------- | --------------------------------------------------------------------------------------------- | -------------------------- |
| `>`      | Devuelve `True` si el operador de la izquierda es mayor que el operador de la derecha         | `12 > 3` devuelve `True`   |
| `<`      | Devuelve `True` si el operador de la derecha es mayor que el operador de la izquierda         | `12 < 3` devuelve `False`  |
| `==`     | Devuelve `True` si ambos operandos son iguales                                                | `12 == 3` devuelve `False` |
| `>=`     | Devuelve `True` si el operador de la izquierda es mayor o igual que el operador de la derecha | `12 >= 3` devuelve `True`  |
| `<=`     | Devuelve `True` si el operador de la derecha es mayor o igual que el operador de la izquierda | `12 <= 3` devuelve `False` |
| `!=`     | Devuelve `True` si ambos operandos no son iguales                                             | `12 != 3` devuelve `True`  |

### Operadores Bit a Bit

Un operador bit a bit realiza operaciones en los operandos bit a bit.

| Operador | Descripción                                                                                                                                                              | Uso                                                       |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| &        | Realiza bit a bit la operación AND en los operandos                                                                                                                      | a & b = 2 (Binario: 10 & 11 = 10)                         |
| \|       | Realiza bit a bit la operación OR en los operandos                                                                                                                       | a \| b = 3 (Binario: 10 \| 11 = 11)                       |
| ^        | Realiza bit a bit la operación XOR en los operandos                                                                                                                      | a ^ b = 1 (Binario: 10 ^ 11 = 01)                         |
| ~        | Realiza bit a bit la operación NOT bit a bit. Invierte cada bit en el operando \| ~a = -3 (Binario: ~(00000010) = (11111101))                                            |
| >>       | Realiza un desplazamiento a la derecha bit a bit. Desplaza los bits del operador de la izquierda a la derecha tantos bits como indica el operador de la derecha          | a >> b = 0 (Binario: 00000010 >> 00000011 = 0)            |
| <<       | Realiza un desplazamiento a la izquierda bit a bit. Desplaza los bits del operando de la izquierda a la izquierda tantos bits como especifique el operador de la derecha | a \| << b = 16 (Binario: 00000010 << 00000011 = 00001000) |

### Operadores de Asignación

Se utiliza un operador de asignación para asignar valores a una variable. Esto generalmente se combina con otros operadores (como aritmética, bit a bit) donde la operación se realiza en los operandos y el resultado se asigna al operando izquierdo.

| Operador | Descripción                                     |
| -------- | ----------------------------------------------- |
| `=`      | `a = 5`. El valor 5 es asignado a la variable a |
| `+=`     | `a += 5` es equivalente a `a = a + 5`           |
| `-=`     | `a -= 5` es equivalente a `a = a - 5`           |
| `*=`     | `a *= 3` es equivalente a `a = a * 3`           |
| `/=`     | `a /= 3` es equivalente a `a = a / 3`           |
| `%=`     | `a %= 3` es equivalente a `a = a % 3`           |
| `**=`    | `a **= 3` es equivalente a `a = a ** 3`         |
| `//=`    | `a //= 3` es equivalente a `a = a // 3`         |
| `&=`     | `a &= 3` es equivalente a `a = a & 3`           |
| `\|=`    | `a \|= 3` es equivalente a `a = a \| 3`         |
| `^=`     | `a ^= 3` es equivalente a `a = a ^ 3`           |
| `>>=`    | `a >>= 3` es equivalente a `a = a >> 3`         |
| `<<=`    | `a <<= 3` es equivalente a `a = a << 3`         |

### Operadores Lógicos

Se utiliza un operador lógico para tomar una decisión basada en múltiples condiciones. Los operadores lógicos utilizados en Python son `and`, `or` y `not`.

| Operador | Descripción                                          | Uso       |
| -------- | ---------------------------------------------------- | --------- |
| `and`    | Devuelve `True` si ambos operandos son `True`        | `a and b` |
| `or`     | Devuelve `True` si alguno de los operandos es `True` | `a or b`  |
| `not`    | Devuelve `True` si alguno de los operandos `False`   | `not a`   |

### Operadores de Pertenencia

Un operador de pertenencia se emplea para identificar pertenencia en alguna secuencia (listas, strings, tuplas).

`in` y `not in` son operadores de pertenencia.

- `in` devuelve `True` si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.
- `not in` devuelve `True` si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve `False`.

### Operadores de Identidad

Un operador de identidad se emplea para comprobar si dos variables emplean la misma ubicación en memoria.

`is` y `is not` son operadores de identidad.

- `is` devuelve `True` si los operandos se refieren al mismo objeto. En caso contrario devuelve `False`.
- `is not` devuelve `True` si los operandos no se refieren al mismo objeto. En caso contrario devuelve `False`.

Ten en cuenta que dos valores, cuando son iguales, no implica necesariamente que sean idénticos.
