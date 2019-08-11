print("Verificacion de acceso")

edad_usuario = int(input("\nIntroduce tu edad\n"))

if edad_usuario<18:
	print("no puedes pasar")
elif edad_usuario>100 and edad_usuario<200:
	print("edad incorrecta")
elif edad_usuario>200:
	print("edad incorrecta men")
else:
	print("puedes pasar")


print("\nEl programa ha finjalizado")