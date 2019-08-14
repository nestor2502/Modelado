#!/usr/bin/env python
# -*- coding: Windows-1252 -*-
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
# -*- coding: IBM850 -*-
import requests
import json
import time
import os.path
import httplib
import urlparse

#diccionario donde se almacenan las ciudades y su temperatura
cache = {}

#Funcion que procesa todo el archivo
def procesarArchivo(ruta):
	#Obtenemos el formato del archivo que se leerá
	extension = os.path.splitext(ruta)
	#si el formato no es .csv se termina el programa
	if str(extension[1]) != ".csv":
		print("Formato de archivo incorrecto, solo se acepta el siguiente formato: .csv")
		return
	#si el formato es .csv se procede
	try:
		print("Obteniendo resultados....\n")
		#se comprueba que haya una conexion estable
		if comprobarConexion() == True:
			#se lee el archivo
			with open(ruta, 'r') as archivo:
				#se divide en lineas
				lineas = archivo.read().splitlines()
				#se elimina la primera linea que es la que incluye los titulos
				lineas.pop(0)
				#se recorre linea a linea
				for i in lineas:
					linea = i.split(',')
					ciudad_origen = str(linea[0])
					ciudad_destino = str(linea[1])
					coordenadasOrigen = (linea[2], linea[3])
					coordenadasDestino = (linea[4], linea[5])
					clima_origen = ""
					clima_destino = ""
					#si la ciudad de origen está en cache se busca
					if ciudad_origen in cache:
						clima_origen = cache[ciudad_origen]
					#si no, entonces se agrega
					else:
						clima_origen = obtenerClima(coordenadasOrigen[0], coordenadasOrigen[1])
						cache[ciudad_origen]= clima_origen
					if ciudad_destino in cache:
						clima_destino = cache[ciudad_destino]
					else:
						clima_destino = obtenerClima(coordenadasDestino[0], coordenadasDestino[1])
						cache[ciudad_destino]= clima_destino
				#se obtiene toda la informacion
				reporte_peticion()
				print ("Fecha: "  + time.strftime("%x"))
				print ("Hora:  " + time.strftime("%X"))
		else:
			print("No hay conexion a internet: ")
			print("   -Vuelve a intentarlo mas tarde")
			print("   -Revisa tu conexion a internet")
	except:
		print("Hubo un error")

#funcion que genera el reporte general
def reporte_peticion():
	j=0
	temp = cache.keys()
	for i in cache:
		print("Ciudad: "+temp[j]+"  Temperatura: "+str(cache[temp[j]]) )
		print("\n")
		j+=1

#se obtiene el clima de una ciudad
def obtenerClima(lat, lon):
	try:
		if __name__ == '__main__':
			url = 'http://api.openweathermap.org/data/2.5/weather?'
			#parametros que se concatenaran al url
			args = {'lat':lat, 'lon':lon, 'APPID':'eb29ea68cdfba20565899d9af8e2c437'}
			#se realiza la peticion
			response = requests.get(url, params = args)
			if response.status_code == 200:
				#se obtiene un archivo content
				content = response.content
				#se obtiene un archivo json
				response_json = json.loads(response.text)
				#obtenemos un diccionario con la informacion
				main = response_json["main"]
				#se obtiene la temperatura de main
				temperatura = "Temperatura:"+ str(main['temp'])
				#se obtiene la presion de main
				presion = " Presion:"+str(main['pressure'])
				#se obtiene la humedad de main
				humedad = " Humedad:"+str(main['humidity'])
				#se genera una tupla con la informacion obtenida
				datos_generales = (temperatura, presion, humedad)
		return datos_generales
	except:
		print("No podemos conectarnos con el servidor, intentalo mas tarde")
	
		
#funcion que devuelve el estado de la conexion
def get_server_status_code(url):
    # descarga sólo el encabezado de una URL y devolver el código de estado del servidor.
    host, path = urlparse.urlparse(url)[1:3]
    try:
        conexion = httplib.HTTPConnection(host)
        conexion.request('HEAD', path)
        return conexion.getresponse().status
    except StandardError:
        return None

# función que se encarga de checkear que exista la url a guardar
def check_url(url):
    # Comprobar si existe un URL sin necesidad de descargar todo el archivo. Sólo comprobar el encabezado URL.
    # variable que se encarga de traer las respuestas
    codigo = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]
    return get_server_status_code(url) in codigo

#funcion que comprueba la conexion retornando un booleano
def comprobarConexion():
	return check_url('http://www.google.com')


procesarArchivo('/home/nestor2502/Modelado/Tarea01/dataset.csv')






