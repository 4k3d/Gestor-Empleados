from Empleados import *
from Metodos import *
import os
import os.path
import pickle

opcion = -1

while(opcion == -1):
	mostrarMenu()
	opcion = int(input("Ingrese opcion: "))
	if(opcion == 1):
		os.system("clear")
		empleado = crearEmpleado()
		empleados.append(empleado)
		os.system("clear")
		print("\nEmpleado creado con exito")
		input("Presiona una tecla para continuar...")
		os.system("clear")
		opcion = -1
	elif(opcion == 2):
		os.system("clear")
		mostrarEmpleado(empleados)
		os.system("clear")
		opcion = -1
	elif(opcion == 3):
		os.system("clear")
		modificarEmpleado(empleados)
		os.system("clear")
		opcion = -1
	if(opcion == 4):
		os.system("clear")
		calcularSueldo(empleados)
		os.system("clear")
		opcion = -1
	if(opcion == 0):
		guardarDatos()
		break
