# Object Oriented Programming (OOP)

La **Programación Orientada a Objetos** (_POO_) es un paradigma de programación que organiza el diseño del software en torno a objetos en lugar de funciones y lógica. Un objeto es una entidad que combina datos (atributos) y comportamiento (métodos).

Los cuatro pilares de la POO son:

1. Encapsulamiento
2. Abstracción
3. Herencia
4. Polimorfismo

## Clases y Objetos: Los Fundamentos

En POO, una clase es como un plano o plantilla para crear objetos. Define las propiedades (_atributos_) y los comportamientos (_métodos_) que tendrán los objetos creados a partir de ella. Un objeto (también conocido como instancia) es una realización concreta de una clase.

### Definición de Clases

Una clase se define utilizando la palabra clave `class`. Los nombres de las clases suelen seguir la convención **CamelCase** (la primera letra de cada palabra en mayúscula).

```python
# Definición de una clase simple
class NombreDeLaClase:
    pass # 'pass' es una declaración nula; no hace nada, pero es necesaria para que la sintaxis sea válida
```

### Creación de Objetos (Instanciación)

Crear un objeto a partir de una clase se llama **instanciación**. Lo haces llamando a la clase como si fuera una función.

```python
objeto = NombreDeLaClase(valor1, valor2, ...)
```

### Atributos: Datos de un Objeto

Los atributos son variables que pertenecen a un objeto y almacenan datos sobre él.

- **Atributos de Instancia:** Pertenecen a una instancia específica de la clase. Cada objeto tiene su propia copia de estos atributos. Se definen comúnmente en el método `__init__`.
- **Atributos de Clase:** Pertenecen a la clase misma y son compartidos por todas las instancias de esa clase.

```python
valor_del_atributo = objeto.atributo1
resultado_del_metodo = objeto.metodo(argumento1, argumento2, ...)
```

## Método `__init__` (Constructor)

Este es un método especial que se llama automáticamente cuando se crea una nueva instancia de la clase. Se utiliza para inicializar los atributos de la instancia. El primer parámetro de cualquier método de instancia es `self`, que se refiere a la instancia actual del objeto.

```python
class NombreDeLaClase:
    def __init__(self, parametro1, parametro2, ...):
        # Inicialización de atributos aquí
        self.atributo1 = parametro1
        self.atributo2 = parametro2
        ...
```

### Métodos: Comportamiento de un Objeto

Los métodos son funciones que pertenecen a una clase y definen el comportamiento de sus objetos. Siempre toman `self` como su primer argumento.

## Encapsulamiento

El **encapsulamiento** es el principio de agrupar los datos (_atributos_) y los métodos que operan sobre esos datos dentro de una sola unidad (_la clase_), y restringir el acceso directo a algunos de los componentes del objeto. Esto protege la integridad de los datos y simplifica el uso del objeto.

En Python, el encapsulamiento se logra mediante convenciones de nombrado, ya que no tiene modificadores de acceso estrictos como `private` o `public` de otros lenguajes como Java.

- **Público:** Atributos y métodos accesibles desde cualquier lugar. (Sin prefijo)

  ```python
  self.nombre
  ```

- **Protegido:** Atributos y métodos destinados a ser usados internamente por la clase o sus subclases. Se usa un prefijo de un solo guion bajo (`_`).

  ```python
  self._saldo # Python no lo impone, es una convención para los desarrolladores
  ```

- **Privado:** Atributos y métodos destinados a ser usados solo dentro de la clase que los define. Se usa un prefijo de doble guion bajo (`__`). Python "manglea" el nombre (lo renombra internamente) para evitar colisiones en subclases, haciendo que sea difícil pero no imposible acceder a ellos desde fuera.

  ```python
  self.__password
  ```

## Abstracción

La **abstracción** consiste en mostrar solo los detalles esenciales de un objeto y ocultar la complejidad interna. Permite al usuario interactuar con objetos a un alto nivel, sin preocuparse por cómo funcionan las cosas internamente.

En Python, la abstracción se logra naturalmente al definir interfaces claras (métodos públicos) y ocultar la implementación interna (usando encapsulamiento). Las clases abstractas y los métodos abstractos (del módulo `abc`) son herramientas explícitas para la abstracción, obligando a las subclases a implementar ciertos métodos.

```python
from abc import ABC, abstractmethod

class MiClaseAbstracta(ABC):
    @abstractmethod
    def mi_metodo_abstracto(self):
        pass

class MiSubclase(MiClaseAbstracta):
    def mi_metodo_abstracto(self):
        print("Implementación del método abstracto en la subclase")
```

## Herencia

La **herencia** permite que una clase (clase hija o subclase) herede atributos y métodos de otra clase (clase padre o superclase). Esto promueve la reutilización de código y establece una relación "es un tipo de" (_is-a-kind-of_) entre las clases.

```python
class Subclase(Superclase):
    pass
```

- `super().__init__()`: Se usa para llamar al constructor de la clase padre y asegurar que los atributos de la clase padre sean inicializados.

## Polimorfismo

El **polimorfismo** significa "_muchas formas_". En POO, se refiere a la capacidad de diferentes objetos para responder al mismo mensaje (llamada a método) de maneras diferentes, cada uno implementando ese mensaje de acuerdo con su propia naturaleza. Se logra a través de la herencia y la sobrescritura de métodos.

## Métodos Especiales (_Dunder Methods_)

Python utiliza una serie de métodos especiales, también conocidos como "dunder methods" (por sus dobles guiones bajos `__`), para implementar el comportamiento de operadores y funciones incorporadas. Personalizar estos métodos permite a tus objetos interactuar con Python de una manera más "pitónica".

Algunos importantes son:

- `__init__(self, ...)`: Constructor.
- `__str__(self)`: Representación en cadena legible para humanos (usada por `print()`).
- `__repr__(self)`: Representación en cadena para desarrolladores (usada en el intérprete).
- `__eq__(self, other)`: Compara dos objetos para igualdad (`==`).
- `__len__(self)`: Define el comportamiento de `len()`.
- `__getitem__(self, key)`: Define el comportamiento de `[]` para acceso por índice o clave.
- `__setitem__(self, key, value)`: Define el comportamiento de asignación `[] =`.
- `__delitem__(self, key)`: Define el comportamiento de `del obj[key]`.
- `__call__(self, *args, **kwargs)`: Permite que una instancia de un objeto sea llamada como una función.

## Propiedades (`@property`)

Las **propiedades** en Python te permiten definir métodos que se comportan como atributos. Esto es útil para:

- Controlar el acceso a los atributos (getters, setters, deleters).
- Validar datos antes de asignarlos a un atributo.
- Calcular el valor de un atributo "bajo demanda".

Se implementan usando el decorador `@property` para el getter, y `@nombre_atributo.setter`, `@nombre_atributo.deleter` para los métodos de establecer y eliminar, respectivamente.

## Métodos de Clase y Métodos Estáticos

Además de los métodos de instancia (que usan `self`), Python ofrece:

- **Métodos de Clase (`@classmethod`):** Operan sobre la clase misma, no sobre una instancia específica. Reciben la clase como primer argumento (por convención, `cls`). Son útiles para crear constructores alternativos o métodos que operan en atributos de clase.
- **Métodos Estáticos (`@staticmethod`)**: No operan sobre la instancia ni sobre la clase. No reciben `self` ni `cls`. Son funciones que lógicamente pertenecen a la clase, pero no necesitan acceder a sus datos internos. Son como funciones normales, pero se organizan dentro de una clase para mejorar la modularidad.

## Herencia Múltiple y `MRO`

Python permite la **herencia múltiple**, donde una clase puede heredar de varias clases base. Si hay métodos o atributos con el mismo nombre en diferentes clases padre, Python sigue un **Orden de Resolución de Métodos (MRO)** para determinar cuál se debe usar. El MRO se basa en un algoritmo llamado C3 linearization.

Puedes ver el MRO de una clase usando `Clase.mro()` o `help(Clase)`.

## Sobrecarga de Métodos

La **sobrecarga de métodos**, en términos generales, permite definir múltiples métodos con el mismo nombre pero con diferentes listas de parámetros (tipos y/o cantidad) dentro de una misma clase. Al llamar al método, el compilador (o intérprete) determina cuál de las versiones debe ejecutarse basándose en los argumentos proporcionados.

En Python, la sobrecarga de métodos, como característica inherente, **no existe como en otros lenguajes como Java o C++**. Sin embargo, se puede lograr un comportamiento similar mediante el uso de argumentos por defecto, argumentos variables (\*args, \*\*kwargs) y la comprobación de tipos dentro de un mismo método.
