def add(x, y):
	"""add function"""
	return x+y

def subtract(x,y):
	return  x-y

def multiply(x,y):
	return x*y

def divide(x, y):
	if y == 0:
		raise ValueError("can not divide by zero")

	return x/y
