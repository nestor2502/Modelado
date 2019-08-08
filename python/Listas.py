miLista = ["maria", "pepe",65, "antonio"]
# esto es para agregar al funal de la lista
miLista.append("nestor")
# se agrega en una posicion definida para poder saber su ubicacion
miLista.insert(2,"juan")  

print("Obteniendo datos desde un elemento ")
print(miLista[2:])

print("\nobteniendo el indice de un elemento:")
print(miLista.index("pepe"))

print("\nNos dice si un elemento se encuentra en la lista:")
print("pepesss" in miLista)

print("\n\nElimina el ultimo elemento de la lista")
print("antes de borrar", miLista[:])
miLista.pop()
print("despues de borrar: ",miLista[:])


#sumar listas
miLista2 = ["sandra", "perla"]

miLista3 = miLista + miLista2
print("\n se suma lista 1 con lista 2")
print(miLista3[:])