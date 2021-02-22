"""Piramide"""

num = int(input('Diga un numero: '))

for fila in range (1,num+1):
	for colum in range(1,fila+1):
		print(fila, end="");
	print()
for fila in range (num,0,-1):
	for column in range (fila,0,-1):
		if fila != 5:
			print(fila,end="");
	if fila!=5:
			print()