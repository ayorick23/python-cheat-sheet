import unittest

# Función a probar
def sumar_numeros(a, b):
    return a + b

class TestSumar(unittest.TestCase):
    
    # Este método se ejecuta antes de cada prueba.
    def setUp(self):
        print("\nEjecutando setUp...")
        self.a = 5
        self.b = 3
    
    # Este método se ejecuta después de cada prueba.
    def tearDown(self):
        print("Ejecutando tearDown...")
        del self.a
        del self.b

    # Los métodos de prueba deben empezar con 'test_'
    def test_sumar_positivos(self):
        """Verifica la suma de números positivos."""
        print("  Ejecutando test_sumar_positivos")
        resultado = sumar_numeros(self.a, self.b)
        self.assertEqual(resultado, 8) # Afirmación para verificar que el resultado es 8
        self.assertNotEqual(resultado, 7)
    
    def test_sumar_negativos(self):
        """Verifica la suma de números negativos."""
        print("  Ejecutando test_sumar_negativos")
        resultado = sumar_numeros(-10, -5)
        self.assertEqual(resultado, -15)

    def test_sumar_flotantes(self):
        """Verifica la suma de números flotantes."""
        print("  Ejecutando test_sumar_flotantes")
        resultado = sumar_numeros(2.5, 3.5)
        self.assertAlmostEqual(resultado, 6.0) # Uso de assertAlmostEqual para flotantes

if __name__ == '__main__':
    unittest.main()