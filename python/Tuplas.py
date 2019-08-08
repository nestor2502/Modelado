miTupla = ("A", "B", "C")
print("tupla inicial:")
print(miTupla)
print("\n")

#convertir tupla a lista
miLista = list(miTupla)

#acceder a un elemento en concreto
print("elemento en la posicion 2: ", miTupla[2])
print("\nse convierte tupla en lista: ")
print(miLista[:])

#convertir lista en tupla
miTupla2 = tuple(miLista)
print("\nse convierte lista en tupla: ")
print(miTupla2)

#saber si hay un elemento en una tupla
print("\nD encuentra en la tupla:")
print("D" in miTupla)

#saber el numero de elemnto de mi tupla
print("\nNumero veces que se encuentra un elemento(en este caso A) en mi tupla: ")
print(miTupla.count("A"))

#saber la longitud de la tupla
print("\nLongitud de la tupla: ")
print(len(miTupla))

#Tuplas unitarias (solo contienen un elemento)
miTupla3 = ("Juan",)

print("\n")

#desempaquetado de tuplas
miTupla4= ("Nestor", 25, 02, 2000)
nombre, dia, mes, agno = miTupla4
print(nombre)
print(dia)
print(mes)
print(agno)
