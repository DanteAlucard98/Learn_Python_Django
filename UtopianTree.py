"""Utopian Tree"""

trees = int(input('¿Cuántos arboles quieres para el test?: '))

for i in range (trees):

	cycles = int(input('¿Cuántos ciclos se requiere?: '))
	altura=1
	for p in range(cycles):
		if p%2 ==0 :
			altura=altura*2
		else:
			altura=altura+1

print(f'La altura del arbol es de: ',{i+1},'Con los ciclos',{altura})

