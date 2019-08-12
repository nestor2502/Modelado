def generaPares(limite):
	num = 1
	
	while num<limite:
		#yield nos devuelve un objeto iterable
		yield num*2
		num+=1;

devuelvePares = generaPares(10)

print(next(devuelvePares))
print(next(devuelvePares))
