salario_presidente = int(input("Introduce el salario del presidente: "))
print("Salario presidente: "+str(salario_presidente)+"\n")

salario_director = int(input("Introduce el salario del director: "))
print("Salario director: "+str(salario_director)+"\n")

salario_jefe_area = int(input("Introduce el salario del jefe de area: "))
print("Salario jefe de area: "+str(salario_jefe_area)+"\n")

salario_administrativo = int(input("Introduce el salario del administrativo: "))
print("Salario administrativo: "+str(salario_administrativo)+"\n")

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funcion correctamente")
else:
	print("algo anda mal.jpg")

