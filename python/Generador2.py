#!/usr/bin/env python
# -*- coding: Windows-1252 -*-
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
# -*- coding: IBM850 -*-

#siusamos * antes del argumento le estamos diciendo que recibirá un numero indeterminado de argumentos
#los cuales recibira en forma de tupla
def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		for sub in elemento:
			yield sub
		


ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))