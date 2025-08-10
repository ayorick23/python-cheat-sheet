# A diferencia de unittest, no necesitas importar nada ni heredar de una clase.

# Función a probar (puede estar en otro archivo, ej. mi_modulo.py)
def restar_numeros(a, b):
    return a - b

# Las funciones de prueba deben comenzar con 'test_'
def test_restar_positivos():
    """Verifica la resta de números positivos."""
    assert restar_numeros(10, 5) == 5
    assert restar_numeros(5, 5) == 0

def test_restar_negativos():
    """Verifica la resta de números negativos."""
    assert restar_numeros(-10, -5) == -5

def test_restar_flotantes():
    """Verifica la resta de números flotantes."""
    assert restar_numeros(5.5, 2.5) == 3.0

# Pytest Fixtures (una forma elegante de manejar la configuración)
# Se definen en un archivo con el nombre "conftest.py"
# Si creas un archivo conftest.py en el mismo directorio con el siguiente contenido:

# # conftest.py
# import pytest
#
# @pytest.fixture
# def lista_inicial():
#     print("\nCreando lista inicial...")
#     return [1, 2, 3]

# Puedes usar el fixture como un argumento en tu función de prueba:
def test_lista_con_fixture(lista_inicial):
    """Verifica el fixture de la lista."""
    assert lista_inicial[0] == 1
    assert len(lista_inicial) == 3