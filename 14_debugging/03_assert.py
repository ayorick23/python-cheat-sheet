def dividir(a, b):
    # Aseguramos que b no es cero para evitar ZeroDivisionError
    assert b != 0, "No se puede dividir por cero."
    # Aseguramos que a y b son numéricos
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "Ambos argumentos deben ser números."
    return a / b

print("--- Usando aserciones ---")

try:
    # Caso válido
    print(f"10 / 2 = {dividir(10, 2)}")

    # Caso que falla por división por cero
    print(f"10 / 0 = {dividir(10, 0)}")
except AssertionError as e:
    print(f"Error de aserción: {e}")

try:
    # Caso que falla por tipo incorrecto
    print(f"'a' / 2 = {dividir('a', 2)}")
except AssertionError as e:
    print(f"Error de aserción: {e}")

# Ejemplo de aserción para verificar el estado interno del programa
class Pila:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)
        assert len(self._items) > 0, "La pila no debería estar vacía después de un push."

    def pop(self):
        assert len(self._items) > 0, "No se puede hacer pop de una pila vacía."
        return self._items.pop()

try:
    mi_pila = Pila()
    mi_pila.push(1)
    mi_pila.pop()
    mi_pila.pop() # Esto lanzará un AssertionError
except AssertionError as e:
    print(f"\nError de aserción en Pila: {e}")