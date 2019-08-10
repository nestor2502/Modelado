import requests
"""
Con el metodo get nosotros obtenermos un recurso del servidor 
"""
_name_ = '_main_'
if _name_ =='_main_':
	url = 'https://www.google.com.mx/'
	response= requests.get(url)

	if response.status_code == 200:
		#me imprime el contenido del objeto response
		print(response.content) 
		#si queremos guardar el contenido
		content = response.content
		"""
		se genera un nuevo archivo con open
		(nombre del archivo, tipo de escritura(escritura binaria))
		"""
		file = open("google.html", 'wb')
		file.write(content)
		file.close()


