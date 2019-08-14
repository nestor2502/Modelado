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
	#
	extension = os.path.splitext(ruta)
	if str(extension[1]) != ".csv":
		print("Formato de archivo incorrecto, solo se acepta el siguiente formato: .csv")
		return
	try:
		print("Obteniendo resultados....\n")
		if comprobarConexion() == True:
			with open(ruta, 'r') as archivo:
				lineas = archivo.read().splitlines()
				lineas.pop(0)
				for i in lineas:
					linea = i.split(',')
					ciudad_origen = str(linea[0])
					ciudad_destino = str(linea[1])
					coordenadasOrigen = (linea[2], linea[3])
					coordenadasDestino = (linea[4], linea[5])
					clima_origen = ""
					clima_destino = ""
					if ciudad_origen in cache:
						clima_origen = cache[ciudad_origen]
					else:
						clima_origen = obtenerClima(coordenadasOrigen[0], coordenadasOrigen[1])
						cache[ciudad_origen]= clima_origen
					if ciudad_destino in cache:
						clima_destino = cache[ciudad_destino]
					else:
						clima_destino = obtenerClima(coordenadasDestino[0], coordenadasDestino[1])
						cache[ciudad_destino]= clima_destino
				reporte_peticion()
				print ("Fecha: "  + time.strftime("%x"))
				print ("Hora:  " + time.strftime("%X"))
		else:
			print("No hay conexion a internet: ")
			print("   -Vuelve a intentarlo mas tarde")
			print("   -Revisa tu conexion a internet")
	except:
		print("Hubo un error")

def reporte_peticion():
	j=0
	temp = cache.keys()
	for i in cache:
		print("Ciudad: "+temp[j]+"  Temperatura: "+str(cache[temp[j]]) )
		print("\n")
		j+=1

def obtenerClima(lat, lon):
	try:
		if __name__ == '__main__':
			url = 'http://api.openweathermap.org/data/2.5/weather?'
			args = {'lat':lat, 'lon':lon, 'APPID':'eb29ea68cdfba20565899d9af8e2c437'}
			response = requests.get(url, params = args)
			if response.status_code == 200:
				content = response.content
				response_json = json.loads(response.text)
				main = response_json["main"]
				temperatura = "Temperatura:"+ str(main['temp'])
				presion = " Presion:"+str(main['pressure'])
				humedad = " Humedad:"+str(main['humidity'])
				datos_generales = (temperatura, presion, humedad)
		return datos_generales
	except:
		print("No podemos conectarnos con el servidor, intentalo mas tarde")
	
		

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

def comprobarConexion():
	return check_url('http://www.google.com')


procesarArchivo('/home/nestor2502/Modelado/Tarea01/dataset.csv')






