#!/usr/bin/env python
# -*- coding: Windows-1252 -*-
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
# -*- coding: IBM850 -*-
"""
Las anteriores lineas son para evitar problemas con la ñ y acentos,
se usa la primera linea y alguna de las otras(tambien todas pero hay
que evitar codigo no necesario)
"""
miDiccionario={"Alemania":"Berlin", "Francia":"Paris", "UK":"London", "Mexico": "Ciudad de Mexico"}
#utilizo la llave para obtener el valor
print(miDiccionario["Francia"])

#para imprimir todo el diccionario
print("\nSe imprime diccionario: ")
print(miDiccionario)

#Agregar elementos
print("\ndiccionario agregando un elemento: ")
miDiccionario["Italia"]= "lisboa"
print("\nSe imprime diccionario: ")
print(miDiccionario)

#Modificar el valor de una llave
miDiccionario["Italia"]= "Roma"
print("\nSe imprime diccionario: ")
print(miDiccionario)

#Eliminar un elemento
del miDiccionario["UK"]
print("\nSe elimina una llave del diccionario: ")
print(miDiccionario)

#mezclando tipos de datos
miDiccionario2 = {"Alemania": 1, 23: "Jordan", "Mosqueteros":3}
print("\nSe imprime diccionario 2: ")
print(miDiccionario2)

#Utilizando una tupla para asignar los valores
miLista = ["Spain","France","UK"]
miDiccionario3 = {miLista[0]:"Madrid", miLista[1]:"paris", miLista[2]:"Londres"}
print("\nSe imprime diccionario que usa tupla para asignar los valores")
print(miDiccionario3)

#Listas en diccionarios
miDiccionario4 = {23:"Jordan", "Nombre":"Michael", "Equipo": "Chicago", "Anillos": [1991, 1992, 1993, 1996, 1997,1998]}
print("\nImpresion de los valores: ")
print(miDiccionario4["Anillos"])

#Diccionarios dentro de diccionarios
#En este caso se tiene una lista como valor de una llave dentro de un diccionario dentro de un diccionario
miDiccionario4 = {23:"Jordan", "Nombre":"Michael", "Equipo": "Chicago", "Anillos":{"Temporadas":[1991, 1992, 1993, 1996, 1997,1998]}}
print("\nImpresion de los valores: ")
print(miDiccionario4["Anillos"])

#mas metodos
print("\nLlaves del diccionario 1")
print(miDiccionario.keys()) 

print("\nValores del diccionario 1")
print(miDiccionario.values())

print("\nLongitud del diccionario 1")
print(len(miDiccionario))  