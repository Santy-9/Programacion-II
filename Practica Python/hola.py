from platform import python_version
from re import T
from tkinter import N

def imprimir_cuadrados():
 print("Se calculará la suma de los cuadrados entre dos números ingresados")
  
 n1 = int (input ("Ingrese un número entero: "))
 n2 = int (input ("Ingrese otro número entero: "))
 suma=0
 for x in range (n1, n2):
     suma = suma + x*x

 print ("La suma de los cuadrados entre ", n1, "y ", n2, "es: ", suma)
 print ("Es todo por ahora!")

#imprimir_cuadrados()

def Name ():
    a = input("Como es su Name: ")
    print ("Hola ", a)

#Name()

def prod():
    a = int (input("ingrese el primer numero "))
    b = int (input("ingrese el segundo numero "))
    print("el producto de ambos es", a*b)
    
#prod()

#suma = 0
#for x in range (10,0,-1):
 #   print(x)
 #   suma = suma + x
#print ("la suma es: ", suma)

#suma = 0
#for x in range (0,10,2):
#    print(x)
#    suma = suma + x
#print ("la suma es: ", suma)  




def far_cel():

    ''' Representamos temperaturas mediante números float.
    temperatura: float
    far_cel: float -> float
    El parámetro representa una temperatura en Fahrenheit y
    retorna su equivalente en Celsius.
    Ejemplos:
    far_cel(32) = 0
    far_cel(212) = 100
    far_cel( -40) = -40
    far_cel(90) = 32.22  ''' 
    temp_f = 0
    temp_c = 0
    temp_k = 0
    temp_r = 0
    temp = float(input("Ingrese temperatura: "))
    unid = input("Ingrese unidad: ")
    if(unid == "C"):
        temp_f = temp * 1.8 + 32
        temp_k = temp + 273.15
        temp_r = (temp + 273.15) * 1.8
    elif(unid == "F"):
        temp_c = (temp - 32) / 1.8
        temp_k = (temp + 459.67) / 1.8
        temp_r = temp + 459.67
    elif (unid == "K"):
        temp_c = temp - 273.15
        temp_f = 9 * temp - 459.67
    else: 
        temp_c = (temp / 1.8)- 273.15

    print(unid,"a F:", temp_f, "a C:", temp_c,"a K:", temp_k, "a R", temp_r  )

def far_cel1(temp_f):
 '''Representamos temperaturas mediante números float
  temperatura: float
  far_cel: float -> float
  El parámetro representa una temperatura en Fahrenheit y
  retorna su equivalente en Celsius.
  Ejemplos:
  far_cel(32) = 0
  far_cel(212) = 100
  far_cel(-40) = -40
  far_cel(90) = 32.22 '''
 temp_c = (temp_f -32)* 5/9
 return round(temp_c,2)

def test_far_cel1():
    assert far_cel1(32) == 0
    assert far_cel1(212) == 100
    assert far_cel1(-40) == -40
    assert far_cel1(90) == 32.22

# def main():
 #   ''' main: None -> None
 #   Toma los datos de temperatura a convertir y muestra en pantalla el 
 #   resultado de la conversion.
 #   '''
#   print(far_cel())

'''Pytest
python -m pytest hola.py
-nombre debe estar procedido portest_<identificador>():
como tienen q ser nuestras funciones para ser testeables?
 Devolver
return -> devuelve la funcion en su invocaccion
!=
print -> salida estandar, pantalla
 Tomar
tomar dato|recibir dato por parametro
!=
tomar dato por teclado -> entrada estandar -> teclado

 Estructura de programa
def fun1(  ):
    ...
    return r1
def fun2(  ):
    ...
    return r2

def main():
    #toma los datos de la E/S -> input
    #invocar a las funciones necesarias para resolver el problema
    #mostrar el resultado E/S -> print

pwd
cd
ls
cat
nano

conjetura de collats
combinaciones posibles de contraseña con 3 caracteres


'''

'''
Definir ordenar q reciba 3 numeros y los muestra en orden

Escribir un programa que intercambie el valor de dos variables

Miercoles 27/04 parcial
'''

def intercambio():
    x = int(input("Ingrese un numero: "))
    y = int(input("Ingrese un numero: "))
    z = x
    x = y
    y = z
    print(x)
    print(y)

cad="Hola Mundo"

#for c in cad:
#print(c, end="")


#ej : hacer que sumen las a
#es_a: String -> Boolean
def es_a(caracter):
    return (caracter == "a") or (caracter == "á") or (caracter == "A") or (caracter == "Á")

def cambiar_a(palabra):
    ''' palabra : string
        cambiar_a : String -> String
        traduce cada letra "a" por * en toda la cadena
        Ejempos:
        cambiar_a("banana") = "b*n*n*"
        cambiar_a("sol") = "sol"
        cambiar_a("") = ""
        cambiar_a("ambición") = "*mbicion"
        cambiar_a("ananá") = "*n*n*"
        cambiar_a("Ada") = "*d*"
        cambiar_a("ANANÁ") = "*N*N*"
    '''
    respuesta = ""
    for c in palabra:
        if(es_a(c)):
            respuesta += "*"
        else:
            respuesta += c
    return respuesta

def main():
    palabra = input("Ingrese palabra: ")
    traduccion = cambiar_a(palabra)
    print("La cadena",palabra ,"transformada es",traduccion) 

def test_cambiar_a():
    assert cambiar_a("banana") == "b*n*n*"
    assert cambiar_a("sol") == "sol"
    assert cambiar_a("") == ""
    assert cambiar_a("ambición") == "*mbición"
    assert cambiar_a("ananá") == "*n*n*"
    assert cambiar_a("Ada") == "*d*"
    assert cambiar_a("ANANÁ") == "*N*N*"

def clasificacion(num):
    ''' Numero : Integer
        Clasificaion : Integer -> String
        Categorizar en positivo y negativo y cero a un numero dado
        Ejemplos :
            clasificacion(10) = "Positivo"
            clasificacion(0) = "Cero"
            clasificacion(-5) = "Negativo"
    '''
    if(num > 0):
        respuesta = "Positivo"
    elif (num == 0):
        respuesta = "Cero"
    else:
        respuesta = "Negativo"
    return respuesta

def test_clasificacion():
    assert clasificacion(10) == "Positivo"
    assert clasificacion(-5) == "Negativo"
    assert clasificacion(0) == "Cero"

def main():
    cant = int(input("Ingrese cant. de numero: "))
    for i in range(0, cant):
        num = int(input("Ingrese numero: "))
        print(clasificacion(num))

def main2():
    centinela = input("Ingrese numero o * para terminar: ")
    while(centinela != "*"):
        num = int(centinela)
        print(clasificacion(num))
        centinela = input("Ingrese numero o * para terminar: ")

def main3():
    while(True):
        centinela = input("Ingrese un numero o * para salir")
        if (centinela == "*"):
            break
        numero = int(centinela)
        print(clasificacion(numero))



# centinela , iteractivo
def ej7(n, c):
    '''
        n : Integer
        c : Integer
        Calsificacion : Integer -> Float 
        Recibe un conjunto de notas y calcula el promedio.
        EJemplos : 
    '''
    if (c == 0):
        return "Error, Division por 0"
    else:
        promedio = n / c
        return promedio
   

def main():
    total = 0
    cont = 0
    cent = input("ingrese la nota o * para terminar: ")
    while(cent != "*"):
        nota = int(cent)
        total += nota
        cont += 1
        cent = input("ingrese la nota o * para terminar: ")
    print(ej7(total, cont))


def cont():
    for x in range(10):
        print("x vale ",x)
        if(x % 2 == 0):
            continue
        print(x, "es impar")

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

def esPrimo1 (numero):
    """Integer -> Boolean"""
    resp = True
    for i in range(2, numero):
        if(numero % i == 0):
            return False
        else:
            return True

def esPrimo2 (numero):
    """Integer -> Boolean"""
    resp = True
    for i in range(2, numero):
        if(numero % i == 0):
            return False
    respuesta = True
    return respuesta


def esPrimo3(numero):
    flag = True
    n = 2
    while(flag == True and n <= numero-1):
        if(numero % n == 0):
            flag = False
        n += 1
    return flag

def esPrimo4(numero):
    i = 2
    contador = 0
    while(contador == 0 and i <= numero - 1):
        if(numero % i == 0):
            contador += 1
        i += 1
    if (contador != 0):
        respuesta = False
    return respuesta

def main(n):
    if(esPrimo1(n) == True):
      print(n, "es primo")
    else:
      print(n, "no es primo")









