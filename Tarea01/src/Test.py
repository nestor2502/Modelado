import unittest
import Correccion
import threading

class TestCorreccion(unittest.TestCase):
	
	#prueba de que se genera una peticion correctamente
	def test_obtenerClima(self):
		self.assertIsNotNone(Correccion.obtenerClima(19.3371,-99.566))
	
	#prueba que verifica la existencia del archivo
	def test_verificarArchivo(self):
		self.assertRaises(Exception,Correccion.procesarArchivo('/home/nestor/Modelado/Tarea01/dataset.csv'))
	
	#Prueba que verifica la conexion a internet	
	def test_conection(self):
		self.assertEqual(True, Correccion.comprobarConexion())
"""
	#prueba que realiza el proceso general de peticiones
	def test_procesoGeneral(self):
		Correccion.procesarArchivo('/home/nestor2502/Modelado/Tarea01/codigo/data-set(test).csv')
"""
	
if __name__ == '__main__':
	unittest.main()