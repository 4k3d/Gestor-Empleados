class Empleado():

	def __init__(self, nombre : str, edad : int, numEmpleado : int):
		self.nombre = nombre
		self.edad = edad
		self.numEmpleado = numEmpleado

	def mostrarInformacion(self):
		print("Empleado Numero: ", self.numEmpleado, "\n""Nombre: ",self.nombre,"\n""Edad: ",self.edad)

	def cambiarInformacion(self):
		nombre = input("Ingresar nombre  (Enter para mantener el mismo): ")
		if(nombre != ""):
			 self.nombre = nombre
		edad = input("Ingresar edad  (Enter para mantener el mismo): ")
		if(edad != ""):
			 self.edad = int(edad)

	def calcularSueldo(self):
		pass

class EmpleadoTecnico(Empleado):

	def __init__(self, proyecto : str,nombre : str,edad : int,numEmpleado : int):
		Empleado.__init__(self,nombre,edad,numEmpleado)
		self.proyecto = proyecto
		self.__precioHora = 30

	def calcularSueldo(self,horasTrabajadas : int):
		sueldo = horasTrabajadas * self.__precioHora
		print("Tu sueldo de esta semana es : ",sueldo)

	def mostrarInformacion(self):
		print("Empleado Numero: ", self.numEmpleado, "\nProyecto: ",self.proyecto,"\n""Nombre: ",self.nombre,"\n""Edad: ",self.edad)

	def cambiarInformacion(self):
		nombre = input("Ingresar nombre  (Enter para mantener el mismo): ")
		if(nombre != ""):
			 self.nombre = nombre
		edad = input("Ingresar edad  (Enter para mantener el mismo): ")
		if(edad != ""):
			 self.edad = int(edad)
		proyecto = input("Ingresar proyecto  (Enter para mantener el mismo): ")
		if(proyecto != ""):
			 self.proyecto = proyecto


class EmpleadoProduccion(Empleado):

	def __init__(self,proyecto : str,nombre : str,edad : int,numEmpleado : int):
		Empleado.__init__(self,nombre,edad,numEmpleado)
		self.proyecto = proyecto
		self.__precioHora = 25

	def calcularSueldo(self,horasTrabajadas : int):
		sueldo = horasTrabajadas * self.__precioHora
		print("Tu sueldo de esta semana es : ",sueldo)

	def mostrarInformacion(self):
		print("Empleado Numero: ", self.numEmpleado, "\nProyecto: ",self.proyecto,"\n""Nombre: ",self.nombre,"\n""Edad: ",self.edad)

	def cambiarInformacion(self):
		nombre = input("Ingresar nombre  (Enter para mantener el mismo): ")
		if(nombre != ""):
			 self.nombre = nombre
		edad = input("Ingresar edad  (Enter para mantener el mismo): ")
		if(edad != ""):
			 self.edad = int(edad)
		proyecto = input("Ingresar proyecto  (Enter para mantener el mismo): ")
		if(proyecto != ""):
			 self.proyecto = proyecto


class EmpleadoAdministrativo(Empleado):

	def __init__(self,area : str,nombre : str,edad : int,numEmpleado : int):
		Empleado.__init__(self,nombre,edad,numEmpleado)
		self.area = area
		self.__precioHora = 35

	def calcularSueldo(self,horasTrabajadas : int):
		sueldo = horasTrabajadas * self.__precioHora
		print("Tu sueldo de esta semana es : ",sueldo)

	def mostrarInformacion(self):
		print("Empleado Numero: ", self.numEmpleado, "\nArea: ",self.area,"\n""Nombre: ",self.nombre,"\n""Edad: ",self.edad)

	def cambiarInformacion(self):
		nombre = input("Ingresar nombre  (Enter para mantener el mismo): ")
		if(nombre != ""):
			 self.nombre = nombre
		edad = input("Ingresar edad  (Enter para mantener el mismo): ")
		if(edad != ""):
			 self.edad = int(edad)
		area = input("Ingresar area  (Enter para mantener el mismo): ")
		if(area != ""):
			 self.area = area
