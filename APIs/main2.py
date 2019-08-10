import requests
import json

_name_ = '_main_'
if _name_ =='_main_':
	url = 'http://httpbin.org/get'
	args = {'nombre':'eduardo', 'curso':'python', 'nivel':'intermedio'}
	#get() se encarga de tomar los argumentos y colocarlos en la url
	response= requests.get(url, params = args)
	print(response.url)

	if response.status_code == 200:
		"""
		#si queremos guardar el contenido
		content = response.content
		#print(content)
		#si queremos origin, (obtener el Json que nos regrese el servidor)
		response_json = response.json() #es un diccionario
		origin = response_json['origin']
		print(origin)
		"""
		#otra forma de obtener el json
		response_json = json.loads(response.text)
		origin = response_json["origin"]
		print(origin)


