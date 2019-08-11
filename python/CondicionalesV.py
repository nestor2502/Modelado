#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Asignaturas optativas año 2019\n")
print("Asiganturas optativas: \n-Informatica grafica \n-Pruebas de software \n-Usabilidad y accesabilidad")
asignatura = raw_input("Escribe la asignatura escogida:  ")

if asignatura in("informatica grafica", "pruebas de software", "usabilidad y accesabilidad"):
	print("\nAsignatura elegida: "+ asignatura)

else:
	print("\nLa asignatura escogida no esta contemplada")

