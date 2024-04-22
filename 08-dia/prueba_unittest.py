import unittest
import manejo_unittest


class ProbarCambiaTexto(unittest.TestCase):
    # Para crear test cada method debe empezar con "test"
    def test_uppers(self):
        palabra = 'Hello There'
        resultado = manejo_unittest.all_upper(palabra)
        self.assertEqual(resultado, 'HELLO THERE')


if __name__ == '__main__':
    unittest.main()
