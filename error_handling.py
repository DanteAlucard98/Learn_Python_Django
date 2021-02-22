"""error_handling"""

"""def division(int1,int2):
	try:
		return int1/int2
	except :
		raise Exception('No podemos dividir entre cero')

print(division(0,0))
"""
"""
import sys

def linux_function():
	assert('linux' in sys.platform),"This code only run on Linux"
	print('Doing something')

try:
	linux_function()
except AssertionError as error:
	print(error)
	print("Linux function was not executed")
"""
"""
assert
if 'linux' in sys.platform:
	pass
else:
	raise Exception("OS Error: This code only runs on Linux")
"""
import sys

def linux_validation():
	assert('win32' in sys.platform),"This code only run on Linux"
	print('Doing something')

try:
	linux_validation()
except AssertionError as error:
	print(error)
else:
	try:
		with open('file.log')as file:
			read_data = file.read()
	except FileNotFoundError as file_error:
		print(file_error) 
finally:
	print('This is the finally clause')
