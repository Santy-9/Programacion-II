import os
import time

def imprimirMenu():
  """None->Integer
    Muestra un menú de opciones y devuelve la 
    opción ingresada por el usuario.
    Opciones:
    1. Factorial 
    2. Fibonacci
    3. Promedio Aritmetico
    4. Primo
    5. Operaciones basicas
    6. Salir

  """
  os.system ("clear") 
  print ("1. Calcula el Factorial ")
  print ("2. Calcula el Fibonacci ")
  print ("3. Calcula el Promedio Aritmético")
  print ("4. Determina si es un número primo")
  print ("5. Operaciones basicas")
  print ("6. Opcion de salida")

  opcion = int (input("Ingrese la opción elegida: ? "))
  return opcion

def factorial(n):
	print("Se debe genera el código para calcular el factorial de: ", n)
	respuesta = 0
	fact = 1
	for i in range(1, n+1):
		fact *= i
		respuesta = fact
	return

def fibonacci(numero):
	print("Se debe genera el código para calcular el fibonacci de: ", numero)
	respuesta = 0
	n1= 0
	n2= 1
	for k in range(numero):
		n3 = n2+n1
		n1 = n2
		n2 = n3
		respuesta = n1
	return respuesta

def promedioAritmetico (numero1, numero2):
  """Integer Integer-> Integer"""
  print("Se debe genera el código para calcular el promedio de: ", numero1, " con ", numero2 )
  respuesta = 0
  calculo = (numero1+numero2)/2
  respuesta = calculo
  return respuesta

#DA REL RESULTADO, PERO ESTA MAL HECHO
#def esPrimo (numero):
 # """Integer -> Boolean"""
  #print("Se debe genera el código para calcular si es primo o no el: ", numero, " dado ")
  #for n in range(2,numero):
	  #if numero%n==0:
		  #return False
  #respuesta = True
  #return respuesta

#esPrimo BIEN HECHO
def esPrimo(numero):
	flag = True
	n = 2
	while ((flag) and (n <= numero-1)):
		if (numero%n == 0):
			flag == False
		n+=1
		respuesta = flag
	return respuesta

def resta(numero1,numero2):
	respuesta = 0
	respuesta = numero1-numero2
	return respuesta
	
def suma(numero1,numero2):
	respuesta = 0
	respuesta = numero1+numero2
	return respuesta

def mult(numero1,numero2):
	respuesta = 0
	respuesta = numero1*numero2
	return 0

def div(numero1,numero2):
	respuesta = 0
	if numero2 == 0:
		print("Error")
	else:
		respuesta = numero1/numero2
	return respuesta

def imprimirSubMenu():
	os.system ("clear")
	print ("a. Calcula la suma ")
	print ("b. Calcula la resta ")
	print ("c. Calcula la multiplicacion")
	print ("d. Calcula la division")
	print ("e. Opción de Salida")
	opcion = input("Ingrese la opción elegida: ? ")
	return opcion

def realizarAcciones2(opcion):
	if (opcion == 'a'):
		numero1 = int(input("Ingrese nro a calcular? "))
		numero2 = int(input("Ingrese otro nro a calcular ?"))
		respuesta = suma(numero1,numero2)
		print("El resultado de la suma es: ",respuesta)
		time.sleep(5)
	elif (opcion == 'b'):
		numero1 = int(input("Ingrese nro a calcular? "))
		numero2 = int(input("Ingrese otro nro a calcular ?"))
		respuesta = resta(numero1,numero2)
		print("El resultado de la resta es: ",respuesta)
		time.sleep(5)
	elif (opcion == 'c'):
		numero1 = int(input("Ingrese nro a calcular? "))
		numero2 = int(input("Ingrese otro nro a calcular ?"))
		respuesta = mult(numero1,numero2)
		print("El resultado de la multiplicacion es: ",respuesta)
		time.sleep(5)
	elif (opcion == 'd'):
		numero1 = int(input("Ingrese nro a calcular? "))
		numero2 = int(input("Ingrese otro nro a calcular ?"))
		respuesta = div(numero1,numero2)
		print("El resultado de la division es: ",respuesta)
		time.sleep(5)
	else:
		print("La opcion no es valida, volviendo al menu")
		time.sleep(3)
		realizarAcciones()

def realizarAcciones(opcion):
	if (opcion ==  1):
		numero = int(input ("Ingrese nro a calcular? "))
		respuesta = factorial(numero)
		print ("El factorial del numero dado es: ", respuesta)
		time.sleep(5)
	elif (opcion == 2):
		numero = int(input ("Ingrese nro a calcular? "))
		respuesta = fibonacci(numero)
		print ("El fibonacci del numero dado es: ", respuesta)
		time.sleep(5)
	elif (opcion == 3):
		numero1 = int(input("Ingrese nro a calcular? "))
		numero2 = int(input("Ingrese otro nro a calcular ?"))
		respuesta = promedioAritmetico(numero1,numero2)
		print("El promedio aritmetico de los numeros es: ",respuesta)
		time.sleep(5)
	elif (opcion == 4):
		numero = int(input("Ingrese un nro a calcular? "))
		respuesta = esPrimo(numero)
		print("El numero es primo? True para si, False para no. ?", respuesta)
		time.sleep(5)
	elif (opcion == 5):
		respuesta = imprimirSubMenu()
		while (respuesta != 'e'):
			realizarAcciones2(respuesta)
			respuesta = imprimirSubMenu()
	else:
		print ("La opción seleccionada no es valida.")
		time.sleep(3)

def main():
  respuesta = imprimirMenu()
  while (respuesta != 6):
    realizarAcciones(respuesta)
    respuesta= imprimirMenu()
  print("Gracias por usar este Menú")


main()
 
 
