"""json contraseña"""
import json
count=0
passwordsys=123456

with open('users_database.json','r') as json_file:
    pythonic_jason=json.load(json_file)


while count<3:
	password = int(input('Ingresa su contraseña: '))
	print(type(password))
	print(type(passwordsys))
	if password != passwordsys:
		print('Contraseña erronea intente de nuevo \n')
		count+=1
	else:
		cantidad=int(input('Ingrese la cantidad de datos a mostrar\n'))
		if cantidad==0:
			cantidad=10
		rangomin=int(input('Ingrese el rango minimo\n'))
		rangomax=int(input('Ingrese el rango maximo\n'))
		while cantidad !=0:
			cantidad-=1
			for i in range(len(pythonic_jason)):
				if int(pythonic_jason[i]["age"])>rangomin and int(pythonic_jason[i]["age"])<rangomax:
					print(pythonic_jason[i])
					

