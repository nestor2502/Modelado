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
#peticiones
peticiones1 =[]
#Funcion que procesa todo el archivo
def procesarArchivo(ruta):
	peticiones =0
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
				n =0
				for i in lineas:
					linea = i.split(',')
					ciudad_origen = str(linea[0])
					ciudad_destino = str(linea[1])
					clima_origen = ""
					clima_destino = ""			
					se_encuentra_ciudad_origen = ciudad_origen in cache
					se_encuentra_ciudad_destino = ciudad_destino in cache
					
					#si la ciudad de origen no está en cache se busca
					if se_encuentra_ciudad_origen == False:
						cache[ciudad_origen]=None
						"""
						if __name__ == '__main__':
							thread = threading.Thread(target =genera_peticion , args=(ciudad_origen, linea[2],linea[3],))
							thread.start()

							"""

						genera_peticion(ciudad_origen, linea[2],linea[3])
						peticiones+=1
					if se_encuentra_ciudad_destino == False:
						cache[ciudad_destino]=None
						"""
						if __name__ == '__main__':
							thread = threading.Thread(target =genera_peticion , args=(ciudad_destino, linea[4],linea[5],))
							thread.start()
							"""	
						genera_peticion(ciudad_origen,linea[4],linea[5])	
						peticiones+=1
			peticiones1.append(peticiones)	
		else:
			print("No hay conexion a internet: ")
			print("   -Vuelve a intentarlo mas tarde")
			print("   -Revisa tu conexion a internet")
	except IOError:
		print("No se encuentra el archivo")

#Funcion que obtiene el clima de una ciudad
def genera_peticion(ciudad, coordenada1, coordenada2):
	
	#clima = obtenerClima(coordenada1, coordenada2)
	clima = ("1", "2", "3")
	cache[ciudad] = clima
	print(1)


#funcion que genera el reporte general
def reporte_peticion():

	j=0
	temp = cache.keys()
	for i in cache:
		print("Ciudad: "+str(temp[j])+"  Temperatura: "+str(cache[temp[j]]) )
		print("\n")
		j+=1

#se obtiene el clima de una ciudad
def obtenerClima(lat, lon):
	try:
		url = 'http://api.openweathermap.org/data/2.5/weather?'
		#parametros que se concatenaran al url
		args = {'lat':lat, 'lon':lon, 'APPID':'43f5a3f70cc7df767407eb61249926bc'}
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

#aqui se debe ingresar la ruta donde se encontrará el archivo .csv
procesarArchivo('/home/nestor2502/Modelado/Tarea01/texto/dataset.csv')
#se imprimen las ciudades y su temperatura
reporte_peticion()
#se imprime fecha y hora
print ("Fecha: "  + time.strftime("%x"))
print ("Hora:  " + time.strftime("%X"))
print("numero de peticiones: "+str(peticiones1))





