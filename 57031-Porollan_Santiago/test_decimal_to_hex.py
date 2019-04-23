import unittest
from interfaz_decimal_to_hex import interfaz_decimal_to_hex

class Test_decimal_to_hex(unittest.TestCase):
    def test_5(self):
        val = interfaz_decimal_to_hex(5)
        self.assertEqual(val,'5')
    def test_10(self):
        val = interfaz_decimal_to_hex(10)
        self.assertEqual(val,'A')
    def test_Hola(self):
        val = interfaz_decimal_to_hex('HOLA')
        self.assertEqual(val,'Disculpe, solo acepto numeros')
    def test_17(self):
        val = interfaz_decimal_to_hex(17)
        self.assertEqual(val,'11')
    def test_16(self):
        val = interfaz_decimal_to_hex(16)
        self.assertEqual(val,'10')
    def test_4095(self):
        val = interfaz_decimal_to_hex(4095)
        self.assertEqual(val,'FFF')
    def test_1234(self):
        val = interfaz_decimal_to_hex(1234)
        self.assertEqual(val,'4D2')
    def test_234(self):
        val = interfaz_decimal_to_hex(234)
        self.assertEqual(val,'EA')
    
if __name__ == '__main__':
    unittest.main()
    