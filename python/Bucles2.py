import math

print("Programa de calculo de raiz cuadrada\n")
numero = int(input("introduce un numero: "))
intentos = 0

while numero<0:
	print("\nno se puede hallar la raiz  de un numero negativo")
	if intentos==2:
		print("\nhas consumido demasiados intentos")
		break;
	numero = int(input("\nintroduce un numero: "))
	if numero <0:
		intentos = intentos+1

if intentos<2:
	solucion = math.sqrt(numero)
	print("\nLa raiz cuadrada de "+str(numero)+" es: "+str(solucion))

