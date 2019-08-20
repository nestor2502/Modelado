import unittest
import Principal
import threading

class TestPrincipal(unittest.TestCase):
	
	#prueba de que se genera una peticion correctamente
	def test_obtenerClima(self):
		self.assertIsNotNone(Principal.obtenerClima(19.3371,-99.566))
	
	#prueba que verifica la existencia del archivo
	def test_verificarArchivo(self):
		self.assertRaises(Exception,Principal.procesarArchivo('/home/nestor2502/Modelado/Tarea01/dataset.csv'))
	
	#Prueba que verifica la conexion a internet	
	def test_conection(self):
		self.assertEqual(True, Principal.comprobarConexion())

	#prueba que realiza el proceso general de peticiones
	def test_procesoGeneral(self):
		Principal.procesarArchivo('/home/nestor2502/Modelado/Tarea01/texto/dataset.csv')
		t1 = threading.Thread(target=Principal.procesar_peticiones)
		t1.start()
		t1.join()
	
if __name__ == '__main__':
	unittest.main()