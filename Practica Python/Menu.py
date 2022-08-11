import os
import re
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
  print ("6. Salir")

  opcion = int (input("Ingrese la opción elegida: ? "))
  return opcion

def imprimirSubMenu():
  '''None -> Integer
    Muestra un submenu de opciones y devuelve la opcion sugeruda por el usuario.
    Opciones:
    a. Sumar
    b. Restar
    c. Multiplicar
    d. Dividir
    e. Volver al principar
    '''
  os.system ("clear")
  print("a. Calcular suma")
  print("b. Calcular resta")
  print("c. Calcular multiplicacion")
  print("d. Calcular division")
  print("e. Volver al menu principal")  

  opcion =input("Ingrese la opción elegida: ? ")
  return opcion


def factorial(numero):
    ''' Diseño: 
            Numero: Natural
        Signatura:
            Nat -> Nat
        Proposito:
            Calcular en forma recursiva el factorial de un numero natural dado.
        Ejemplos:
            factorial(5) = 120
            factorial(0) = 1
            factorial(1) = 1
    '''
    if(numero == 0):
        return 1
    else:
        return (numero*factorial(numero-1))

def fibonacci(n): 
  ''' Diseño:
            Numero: Natural
        Signatura:
            Nat -> Nat
        Proposito:
            Calcular en forma recursiva el numero de fibonacci de un numero natural
            dado.
        Ejemplos:
            fibonacci(0) = 0
            fibonacci(1) = 1
            fibonacci(2) = 1
            fibonacci(8) = 21
    '''
  if (n == 0) or (n == 1):
      return n
  else:
      return fibonacci(n - 1) + fibonacci(n - 2)     

def promedioAritmetico (numero1, numero2):
  """Integer Integer-> Integer"""
  respuesta = (numero1 + numero2)/2
  return respuesta

def esPrimo (numero):
    """Integer -> Boolean"""
    resp = True
    for i in range(2, numero):
        if(numero % i == 0):
            resp = False
            break
        else:
            resp = True
    return resp

def suma(n1, n2):
  return n1 + n2

def resta(n1, n2):
  return n1 - n2

def realizarAcciones(opcion):
  """ Integer -> None
      Realiza una acción según la opción del menú elegida. Si la opcion no es valida entonces muestra en pantalla un mensaje de error. 
  """
  if (opcion ==  1):
    numero= int(input ("Ingrese nro a calcular? "))
    respuesta = factorial (numero)
    print ("El factorial del numero dado es: ", respuesta)
    time.sleep(5)
  elif (opcion == 2):
    numero= int(input ("Ingrese nro a calcular? "))
    respuesta = fibonacci (numero)
    print ("El fibonacci del numero dado es: ", respuesta)
    time.sleep(5)
  elif (opcion == 3):
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    respuesta = promedioAritmetico(numero1, numero2)
    print("El promedio de", numero1,"y", numero2,"es: ", respuesta)
    time.sleep(5)
  elif (opcion == 4):
    numero = int(input("Ingrese numero a calcular: "))
    respuesta = esPrimo(numero)
    if(respuesta == True):
      print(numero, "es primo")
    else:
      print(numero, "no es primo")
    time.sleep(5)
  elif(opcion == 5):
    respuesta = imprimirSubMenu()
  elif(opcion == "a"):
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    print(suma(numero1, numero2))
    time.sleep(5)
  elif(opcion == "b"):
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    print(resta(numero1, numero2))
    time.sleep(5)
  else:
    print ("La opción seleccionada no es valida.")
    time.sleep(5)

def main():
  respuesta = imprimirMenu()
  while (respuesta != 6):
    if(respuesta == 5):
      respuesta = imprimirSubMenu()
      while(respuesta != "e"):
        realizarAcciones(respuesta)
        respuesta= imprimirSubMenu()
      respuesta = imprimirMenu()
    realizarAcciones(respuesta)
    respuesta= imprimirMenu()
  print("Gracias por usar este Menú")


main()