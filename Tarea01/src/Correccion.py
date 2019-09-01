#!/usr/bin/env python
# -*- coding: Windows-1252 -*-
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
# -*- coding: IBM850 -*-

#VERSION 2.0
#realiza la peticion
import requests
#Poder obtener el archivo json
import json
#obtener la hora exacta
import time
#obtener el formato del archivo
import os.path
#comprobar si existe un url
import httplib
import urlparse
#manejar hilos
import threading

#diccionario donde se almacenaran los nombres de las ciudades y sus coordenadas
ciudades = {}
#diccionario donde se almacenan las ciudades y su temperatura
cache = {}
#peticiones-x
peticiones1 =[]
#Funcion que procesa todo el archivo
def procesarArchivo(ruta):
	peticiones =0
	renglones =0
	#Obtenemos el formato del archivo que se leerá
	extension = os.path.splitext(ruta)
	#si el formato no es .csv se termina el programa
	if str(extension[1]) != ".csv":
		print("Formato de archivo incorrecto, solo se acepta el siguiente formato: .csv")
		return
	#si el formato es .csv se procede
	try:
		#se comprueba que haya una conexion estable
		if comprobarConexion() == True:
			#se lee el archivo
			with open(ruta, 'r') as archivo:
				#se divide en lineas
				lineas = archivo.read().splitlines()
				#se elimina la primera linea que es la que incluye los titulos
				lineas.pop(0)
				for i in lineas:
					linea = i.split(',')
					ciudad_origen = linea[0]
					ciudad_destino = linea[1]
					coordenadasOrigen = (linea[2], linea[3])
					coordenadasDestino = (linea[4], linea[5])
					clima_origen = ""
					clima_destino = ""
					if ciudad_origen in cache:
						clima_origen = cache[ciudad_origen]
						renglones+=1

					else:
						clima_origen = obtenerClima(coordenadasOrigen[0], coordenadasOrigen[1])
						cache[ciudad_origen]= clima_origen
						peticiones+=1
						renglones+=1
					if ciudad_destino in cache:
						clima_destino = cache[ciudad_destino]
						renglones+=1
					else:
						clima_destino = obtenerClima(coordenadasDestino[0], coordenadasDestino[1])
						cache[ciudad_destino]= clima_destino
						peticiones+=1
						renglones+=1
					#se imprime linea a linea la informacion requerida
					if __name__ == '__main__':
						
						print(reporte_solicitud(ciudad_origen, ciudad_destino, clima_origen, clima_destino))
				if __name__ == '__main__':
	
					peticiones1.append(peticiones)
					print("Numero de vuelos registrados: "+str(renglones/2))
		else:
			print("No hay conexion a internet: ")
			print("   -Vuelve a intentarlo mas tarde")
			print("   -Revisa tu conexion a internet")
	except IOError:
		print("No se encuentra el archivo")

#funcion que devuelve el clima general de la ciudad de origen y destino
def reporte_solicitud(ciudad_origen, ciudad_destino, clima_origen, clima_destino):
	ciudad_origenF = str(ciudad_origen)
	ciudad_destinoF = str(ciudad_destino)
	clima_origenF = str(clima_origen)
	clima_destinoF = str(clima_destino)
	return("\n|| "+ciudad_origenF+" : "+clima_origenF+" - "+ciudad_destinoF+" : "+clima_destinoF+" ||\n")

#se obtiene el clima de una ciudad
def obtenerClima(lat, lon):
	try:
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

# función que se encarga de verificar que exista un url 
def check_url(url):
    # variable que se encarga de traer las respuestas y comprobar si existe un URL 
    codigo = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]
    return get_server_status_code(url) in codigo

#funcion que comprueba la conexion retornando un booleano
def comprobarConexion():
	return check_url('http://www.google.com')

if __name__ == '__main__':
	procesarArchivo('/home/nestor2502/Modelado/Tarea01/texto/dataset.csv')
	print("Numero de ciudades: "+str(peticiones1))
	print ("Fecha: "  + time.strftime("%x"))
	print ("Hora:  " + time.strftime("%X"))