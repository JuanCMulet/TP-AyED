import re
emailRegex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}([.]\w{2})*$"
nombreRegex = "^(\w)+( SRL| SA)"
direcRegex = "^\d{1,4}( \w+){1,3}.( \w+){1,3},( \w+){1,3}$"
teleRegex = "^\d{2,3}-\d{7,8}"

pswd = "pass"

totalEmpresas = []

class Empresa: 
	def __init__(self, codEmp):
		self.codEmp = codEmp
		self.nombre = checkNombre()
		self.dirección = checkDirec()
		self.mail = checkEmail()
		self.teléfono = checkTele()
		self.codCiudad = checkCodCiudad()


def checkTele():
	a = input("\nIngrese el teléfono de la empresa:\n[Código de área + Número telefónico]\n")
	while ( re.search(teleRegex, a) == None ) :
		a = input("\nTeléfono incorrecto, el formato es:\n[Código de área + Número telefónico]\nEjemplo: 341-3804426\n")
	return a


def checkDirec():
	a = str(input("\nIngrese la dirección de la empresa:\n[Altura Calle. Ciudad, Provincia]\n"))
	while ( re.search(direcRegex, a) == None ) :
		a = str(input("\nDirección incorrecta, el formato es:\n[Altura Calle. Ciudad, Provincia]\nEjemplo: 2183 Rioja. Rosario, Santa Fe\n"))


def checkNombre():
	a = str(input("\nIngrese el nombre de la empresa: "))
	while ( re.search(nombreRegex, a) == None ) :
		a = str(input("\nEl nombre ingresado no es válido, intente nuevamente:\n"))
	return a


def checkEmail():
	a = str(input("\nIngrese el mail de la empresa:\n"))
	while ( re.search(emailRegex, a) == None ) :
		a = str(input("\nEl email no es válido, intente nuevamente:\n"))
	return a

	
def checkCodCiudad():
	a = ""
	while (True):
		a = str(input("\nIngrese el código de la ciudad:\n'ROS' para Rosario\n'CBA' para Córdoba\n'BA' para Buenos Aires\n"))
		if ( a == 'ROS' or a == 'CBA' or a == 'BA' ):
			return a


def contarEmpresas():
	ros = 0
	cba = 0
	ba = 0
	for x in totalEmpresas:
		if ( x.codCiudad == 'ROS' ):
			ros += 1
		elif ( x.codCiudad == 'CBA' ):
			cba += 1
		elif ( x.codCiudad == 'BA' ):
			ba += 1
	maxCiudad = max(ros, cba, ba)
	if ( ros == maxCiudad and cba == maxCiudad and ba == maxCiudad ):
		print("Las 3 ciudades cuentan con",maxCiudad,"empresas cada una")
	elif ( ros == maxCiudad and cba == maxCiudad and ba != maxCiudad):
		print("Rosario y Córdoba cuentan con la mayor cantidad de empresas con",maxCiudad,"cada una")
	elif ( ros == maxCiudad and cba != maxCiudad and ba == maxCiudad ):
		print("Rosario y Buenos Aires cuentan con la mayor cantidad de empresas con",maxCiudad,"cada una")
	elif ( ros != maxCiudad and cba == maxCiudad and ba == maxCiudad ):
		print("Córdoba y Buenos Aires cuentan con la mayor cantidad de empresas con",maxCiudad,"cada una")
	elif ( ros == maxCiudad ):
		print("Rosario es la ciudad con mayor cantidad de empresas con",maxCiudad,"empresas")
	elif ( cba == maxCiudad ):
		print("Córdoba es la ciudad con mayor cantidad de empresas con",maxCiudad,"empresas")
	elif ( ba == maxCiudad ):
		print("Buenos Aires es la ciudad con mayor cantidad de empresas con",maxCiudad,"empresas")


def cargaEmpresa(n):
	for x in range(n):
		totalEmpresas.append(Empresa(x))
	contarEmpresas()

def volverCarga(n):
	back = input("\nSi desea continuar escriba 'SI', para volver ingrese 'NO':\n")
	if ( back == 'SI' ):
		cargaEmpresa(n)
	elif ( back == 'NO' ):
		cantACargar()
	else:
		volverCarga(n)

def cantACargar():
	carga = input("\nBienvenido!\nIngrese la cantidad de empresas a cargar: ")
	while ( re.search("\d+", carga) == None ):
		carga = input("\nIngrese la cantidad de empresas a cargar: ")
	carga = int(carga)
	volverCarga(carga)


def pswdInput():
	return str(input("\nIngrese la contraseña:\n"))


def pswdCheck(intentos = 1):
	_pswd = pswdInput()
	if ( _pswd == pswd ):
		print("\nContraseña correcta, acceso permitido...\n")
		cantACargar()
	elif ( _pswd != pswd and intentos < 3 ):
		print("Clave incorrecta, le quedan ",(3-intentos)," intentos")
		pswdCheck(intentos + 1)
	elif ( _pswd != pswd and intentos >= 3 ):
		print("La clave es incorrecta, intente más tarde nuevamente")
		ingreso()


def ingreso():
	user = str(input("\n    ### Inicio de sesión ###\n'cliente' - Ingreso para clientes\n'empresa' - Carga de empresas\n"))

	while (True):
		if ( user == 'cliente' ):
			print("\nPrograma en proceso\n")
			break
		elif ( user == 'empresa' ):
			pswdCheck()
			break
		else:
			user = str(input("\n    ### Inicio de sesión ###\n'cliente' - Ingreso para clientes\n'empresa' - Carga de empresas\n"))

ingreso()