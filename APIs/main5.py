import requests

__name__ = '__main__'
if __name__ == '__main__':
	url = 'https://ep01.epimg.net/elpais/imagenes/2018/12/14/album/1544777592_679099_1544990800_noticia_normal_recorte1.jpg'
	"""
	al colocar stream = True es realizar la peticion dejando la conexion abierta
	"""
	response = requests.get(url, stream = True) #Realiza la peticion sin descargar el contenido
	with open('image.jpg', 'wb') as file:
		#iter_content toma todo el contenido del servidor y la descarga lentamente
		for chunk in response.iter_content(): 
			file.write(chunk)
  

	response.close() #cerramos la conexion



