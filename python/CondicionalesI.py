
print("Programa de evaluacion de notas de alumno")

nota_alumno = input("\nIntroduce la nota del alumno\n")

def evaluacion(nota):
	valoracion = "aprobado"
	if nota<=5:
		valoracion = "suspenso"
	return valoracion

print(evaluacion(int(nota_alumno)))