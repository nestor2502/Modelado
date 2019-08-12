
class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first+'.'+last+'@company.com'

	def fullName(self):
		return '{} {}'.format(self.first,self.last)


emp_1 = Employee('Corey', 'schafer', 5000)
emp_2 = Employee('vazquez', 'nestor', 6000)

#print(emp_1.email)
#print(emp_1.fullName())

print(Employee.fullName(emp_2))

