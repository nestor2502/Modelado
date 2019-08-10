import requests
import json

#se cambia el metodo get() por post()
"""
Con el metodo post nosotros crearemos algun recurso en el servidor

"""
_name_ = '_main_'
if _name_ =='_main_':
	url = 'http://httpbin.org/put'
	#payload es el nombre con el que comoceremos los datos
	payload = {'nombre':'eduardo', 'curso':'python', 'nivel':'intermedio'}
	#le digo al servidor que estoy enviando datos en tipo json
	headers = {'Content-Type':'application/json', 'acces-token':'10863897'}
	#en este caso los parametros se guardan en json
	#response= requests.post(url, json = payload)
	#en este caso se guardan en data pero se crea un diccionario y se guarda en json
	response= requests.put(url, data = json.dumps(payload), headers = headers)

	#json post se encarga de serializarlos
	#data nosotros nos encargamos de serializarlos
	print(response.url)

	if response.status_code == 200:
		#print(response.content)
		headers_response = response.headers #diccionario
		#print(headers_response)
		server = headers_response['Server']
		print(server)
		#pRINCIPALES METODOS DE HTTP
		"""
		GET para obtener algun recurso
		POST para crearlo
		PUT  para actualizarlo
		DELETE para eliminarlo
		"""

       

