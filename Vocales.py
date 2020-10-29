"""Pedir el texto y sacar las vocales de cada uno"""

enunciado = input("Diga su enunciado: ").lower()
dicc = {}

for i in enunciado:
	if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
		print(i)
#Otra manera

enunciado = input("Diga su enunciado: ")
largo= len(enunciado)

while largo != 0:
	for i in enunciado:
		if i == 'a' 
		or i == 'e' 
		or i == 'i' 
		or i == 'o' 
		or i == 'u'
		or i == 'A' 
		or i == 'E' 
		or i == 'I' 
		or i == 'O' 
		or i == 'U':
			print(i)
			count= count+1
		else:
			count= count+1

"""Meter la cantidad de vocales en un diccionario"""

enunciado = input("Diga su enunciado: ").lower()
voc = {
		'aA':0, 
		'eE':0,
		'iI':0,
		'oO':0,
		'uU':0
	}
for i in enunciado:
	if i == 'a':
		voc['aA'] +=1
	elif i == 'e':
		voc['eE'] +=1
	elif i == 'i':
		voc['iI'] +=1
	elif i == 'o':
		voc['oO'] +=1
	elif i == 'u':
		voc['uU'] +=1

print(f'aA:',voc['aA'])
print(f'eE:',voc['eE'])
print(f'iI:',voc['iI'])
print(f'oO:',voc['oO'])
print(f'uU:',voc['uU'])

vocales = 'aeiou'
for i in enunciado:
	for x in vocales:
		if i == x and x == 'a':
			voc['aA'] +=1
		elif i == x and x == 'e':
			voc['eE'] +=1
		elif i == x and x == 'i':
			voc['iI'] +=1
		elif i == x and x == 'o':
			voc['oO'] +=1
		elif i == x and x == 'u':
			voc['uU'] +=1

print(f'aA:',voc['aA'])
print(f'eE:',voc['eE'])
print(f'iI:',voc['iI'])
print(f'oO:',voc['oO'])
print(f'uU:',voc['uU'])







