import unittest
from conceptos import Conceptos

class Testconceptos(unittest.TestCase):

    def test_agreagar(self):
        #Si existe algun elemento
        lista = Conceptos()
        lista.agregar("LLave de prueba 3","concepto 3")
        existe = lista.buscarT("LLave de prueba 3")
        self.assertTrue((existe,False))

    def test_buscar(self):
        lista = Conceptos()
        lista.agregar("LLave de prueba 2","concepto 2")
        existe = lista.buscarT("LLave de prueba 2")
        self.assertEqual(existe,False)


    def test_a_existe_lista(self):
        lista = Conceptos()
        lista.agregar("22 de prueba","concepto 22")
        existe = lista.buscarT("22 de prueba")
        self.assertEqual(existe,False)   


    def test_d_existe_lista(self):
        lista = Conceptos()
        lista.agregar("LLave de prueba 1","concepto 1") 
        existe = lista.buscarT("LLave de prueba 1")
        self.assertEqual(existe,False)   


    def test_e_titulo_lista(self):
        lista = Conceptos() 
        lista.eliminar("prueba de eliminacion")
        existe = lista.buscarT("prueba de eliminacion ")
        self.assertEqual(existe,False)   


    def test_editar_(self):
        lista =  Conceptos()
        lista.editar("LLave de prueba 1")
        existe = lista.editar("LLave de prueba 1")
        self.assertEqual(existe,False)


    def test_imprimir_prueba(self):
        lista = Conceptos()
        lista.imprimir()
        existe = lista.imprimir() == lista
        self.assertEqual(existe,False)







if __name__ == '__main__':
    unittest.main()                         