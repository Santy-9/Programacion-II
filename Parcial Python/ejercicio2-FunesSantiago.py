#Funes Santiago
#41489259

#Diseno de datos
#Empleado (nombre, antiguedad, salario bruto, descuentos, bonificaciones)
#Empleado : (String, Number, Number, Number, Number)
#donde :
#	-nombre : Nombre del empleado
#	-antiguedad : Antiguedad del empleado inicializado en 0 salvo que se indique lo contrario
#	-salario bruto : Salario del empleado inicializado en $55.000 salvo que se indique lo contrario
#	-descuentos : descuentos del empleado inicializado en 0. El numero indica porcentaje
#	-bonificaciones : bonificaciones del empleado inicializado en 0 . EL numero indica porcentaje

def DatoAntiguedad(n):
	''' DatoAntiguedad : Int -> Bollean
		Recibe la antiguedad y determina si es valida
		DatoSalario(4) = True
		DatoSalario(-1) = False
	'''
	if(n >= 0):
		resp = True
	else:
		resp = False
	return resp
	
def DatoSalario(n):
	''' DatoSalario : Int -> Bollean
		Recibe el salario y determina si es valido
		DatoSalario(56000) = True
		DatoSalario(35000) = False
	'''
	if(n < 55000):
		resp = False
	else:
		resp = True
	return resp

def empleado_valido(t):
	''' empleado_valido : Empleado -> Empleado
		Recibe datos del empleado, verifica si es valido y construye un Empleado.
	''' 
	tamano = len(t)
	if(tamano == 1):
		respuesta = (t[0], 0, 55000, 0, 0)
	elif(tamano == 2 and DatoAntiguedad(t[1])):
		respuesta = (t[0], t[1], 55000, 0, 0)
	elif(tamano == 3 and DatoAntiguedad(t[1]) and DatoSalario(t[2])):
		respuesta = (t[0], t[1], t[2], 0, 0)
	elif(tamano == 5):
		respuesta = (t[0], t[1], t[2], t[3], t[4])
	else:
		respuesta = "Error"
	return respuesta
	
	
def mostrar_empleado(Empleado):
	''' mostrar_empleado : Empleado -> String
		Recibe una tupla Empleado y la muestra en pantalla
	'''
	print("Nombre: ",Empleado[0], "\n")
	print("Antiguedad: ",Empleado[1], "\n")
	print("Salario Bruto: ",Empleado[2], "\n")
	print("Descuentos: ",Empleado[3], "\n")
	print("bonificaciones: ",Empleado[4])
	
#print(mostrar_empleado(("Hola", 3, 70000, 0, 0)))

def Descuento(Salario):
	''' Descuento : Integer -> Integer
		Recibe un Empleado y calcula el descuento
	'''
	return Salario - 0.08 * Salario
	

def calcula_sueldo(Empleado):
	''' calcula_sueldo : Empleado -> Empleado
		Recibe un Empleado y aplica los descuentos/bonificaciones correspondientes
		calcula_sueldo(("Julian",12, 65000,0 ,0)) = 65780
		calcula_sueldo(("Maria",4, 55000,0 ,0)) = 53130
	'''
	descuento = Descuento(Empleado[2])
	if(Empleado[1] >= 11):
		respuesta = 0.1 * descuento + descuento
		respuesta2 = (8, 10)
	elif(Empleado[1] > 4 and Empleado[1] <= 10):
		respuesta = 0.07 * descuento + descuento
		respuesta2 = (8, 7)
	elif(Empleado[1] > 3 and Empleado[1] <= 5):
		respuesta = 0.05 * descuento + descuento
		respuesta2 = (8, 5)
	elif(Empleado[1] >= 1 and Empleado[1] <= 3):
		respuesta = 0.03 * descuento + descuento
		respuesta2 = (8, 3)
	else:
		respuesta = descuento
		respuesta2 = (8, 0)
		
	new_empleado = empleado_valido((Empleado[0], Empleado[1], Empleado[2], respuesta2[0], respuesta2[1]))
	mostrar_empleado(new_empleado)
	return("Sueldo neto :", respuesta)
	
def test_calcula_sueldo():
	assert(calcula_sueldo(("Julian",12, 65000,0 ,0))) == 65780
	assert(calcula_sueldo(("Maria",4, 55000,0 ,0))) == 53130
	
	
	
	
	

