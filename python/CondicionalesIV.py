#!/usr/bin/env python
# -*- coding: utf-8 -*-


print("Programa de becas año 2017\n")
distancia_escuela = int(input("\nIntroduce la distancia a la escuela en km:  "))

numero_hermanos = int(input("\nIntroduce el numero de hermanos:  "))

salario_familiar = int(input("\nIntroduce salario anual bruto:  "))

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")




