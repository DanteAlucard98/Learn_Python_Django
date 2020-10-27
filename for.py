"""Clase de FOR"""

names = ['Abraham', 'Cesar','Daniel','Daniela','Diego','Edgar']

for name in names:
	print(f'Student: {name}')
	if name == 'Daniela':
		break
else:
	print('No more names')


string = 'Mauricio'

for caracter in string:
	if caracter != 'i':
		print(caracter)
	else:
		print('Out of the for')


numbers = []

for number in range(0,21,2):
	numbers.append(number)
print(numbers)
