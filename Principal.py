from Empleados import *
import os
import os.path
import pickle

contadorEmpleados = 0
empleados = []

if os.path.isfile("empleados.dat"):
	f = open("empleados.dat","rb")
	try:
		while True:
			contadorEmpleados = contadorEmpleados + 1
			empleados.append(pickle.load(f))
	except:
		f.close()

def guardarDatos(obj : list):
	f = open("empleados.dat","ab+")
	for empleado in obj:
		pickle.dump(empleado,f)

def mostrarMenu():
	mensajeBienvenida = '''
*********************************************************
*Bienvenido al sistema de control de Empleado           *
*Presione una tecla para acceder a distintas opciones   *
*1) Crear Empleado					*
*2) Visualizar Infromacion de Empleado                  *
*3) Cambiar Informacion de Empleado                     *
*4) Obtener sueldo de esta semana                       *
*Presione 0 para salir...                               *
*********************************************************'''
	print(mensajeBienvenida)

def calcularSueldo(obj : list):
	print("Selecciona numero de empleado para calcular su sueldo")
	for i in obj:
		print(i.numEmpleado)
	i = int(input("Selecciona una opcion: "))
	horasTrabajadas = int(input("Cuantas horas trabajo este empleado: "))
	obj[i  - 1].calcularSueldo(horasTrabajadas)
	input("Ingresa una tecla para continuar...")


def mostrarEmpleado(obj : list):
	print("Selecciona numero de empleado")
	for i in obj:
		print(i.numEmpleado)
	i = int(input("Selecciona una opcion: "))
	os.system("clear")
	obj[i - 1].mostrarInformacion()
	input("Ingresa una tecla para continuar...")


def modificarEmpleado(obj : list):
	print("Selecciona numero de empleado")
	for i in obj:
		print(i.numEmpleado)
	i = int(input("Selecciona una opcion: "))
	obj[i - 1].cambiarInformacion()

def crearEmpleado():
	 global contadorEmpleados
	 i =int(input("Que tipo de empleado deseas crear? \n1) Produccion \n2) Tecnico \n3)Administrativo \n:"))
	 if (i == 1):
		 nombre = input("Nombre para este empleado: ")
		 edad = input("Edad de este empleado: ")
		 proyecto = input("Proyecto asignado a este empleado: ")
		 contadorEmpleados = contadorEmpleados + 1
		 return EmpleadoProduccion(proyecto,nombre,edad,contadorEmpleados)

	 if (i == 2):
		 nombre = input("Nombre para este empleado: ")
		 edad = input("Edad de este empleado: ")
		 proyecto = input("Proyecto asignado a este empleado: ")
		 contadorEmpleados = contadorEmpleados + 1
		 return EmpleadoTecnico(proyecto,nombre,edad,++contadorEmpleados)
	 if (i == 3):
		 nombre = input("Nombre para este empleado: ")
		 edad = input("Edad de este empleado: ")
		 area = input("Area asignada a este empleado: ")
		 contadorEmpleados = contadorEmpleados + 1
		 return EmpleadoAdministrativo(area,nombre,edad,++contadorEmpleados)



opcion = -1

while(opcion == -1):
	mostrarMenu()
	opcion = int(input("Ingrese opcion: "))
	if(opcion == 1):
		os.system("clear")
		empleados.append(crearEmpleado())
		os.system("clear")
		print("\nEmpleado creado con exito")
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
		guardarDatos(empleados)
		break
