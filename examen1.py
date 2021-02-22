"""Conteo de mayusculas y minusculas"""

archivo=open('examen.txt', mode='r') 
archivo.read()
i=0
mayusculas=0

while i<len(archivo):
	let=string[i]
	if letra.isupper()==True:
		mayusculas +=1

print("Total mayusculas: ",mayusculas) 