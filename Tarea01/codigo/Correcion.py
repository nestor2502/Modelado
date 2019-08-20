#!/usr/bin/env python
# -*- coding: Windows-1252 -*-
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
# -*- coding: IBM850 -*-

import requests
import json

cache = {}
clima = {}

def procesarArchivo(ruta):

	with open(ruta, 'r') as archivo:
		lineas = archivo.read().splitlines()
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

			else:
				clima_origen = obtenerClima(coordenadasOrigen[0], coordenadasOrigen[1])
				cache[ciudad_origen]= clima_origen
			if ciudad_destino in cache:
				clima_destino = cache[ciudad_destino]
			else:
				clima_destino = obtenerClima(coordenadasDestino[0], coordenadasDestino[1])
				cache[ciudad_destino]= clima_destino

			print(reporte_solicitud(ciudad_origen, ciudad_destino, clima_origen, clima_destino))



def reporte_solicitud(ciudad_origen, ciudad_destino, clima_origen, clima_destino):
	ciudad_origenF = str(ciudad_origen)
	ciudad_destinoF = str(ciudad_destino)
	clima_origenF = str(clima_origen)
	clima_destinoF = str(clima_destino)
	return("|| "+ciudad_origenF+" : "+clima_origenF+" - "+ciudad_destinoF+" : "+clima_destinoF+" ||")






def obtenerClima(lat, lon):
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




procesarArchivo('/home/nestor/Modelado/Tarea01/texto/dataset.csv')