contador = 0

miEmail = raw_input("Intreoduce tu correo: ")

for i in miEmail:
	if i == "@"  or i == ".":
		contador= contador +1
if contador >= 2:
	print("correo correcto")
else:
	print("correo incorrecto")


#uso de range
for i in range(5):
	print(i)

