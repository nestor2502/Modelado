#!/usr/bin/env python
# -*- coding: Windows-1252 -*-

def divide():
	try:
		op1 = (float(input("Introduce el primer numero:  ")))
		op2 = (float(input("Introduce el segundo numero:  ")))
		print("La division es: "+str(op1/op2))
	except ValueError:
		print("El valor introducido es erroneo 1")
	except NameError:
		print("El valor introducido es erroneo 2")
	except ZeroDivisionError:
		print("No se puede dividir entre cero")
	#Lo que esté dentro del finally se ejecuta siempre aunque ocurra un error
	finally:
		print("Calculo finalizado")

divide()