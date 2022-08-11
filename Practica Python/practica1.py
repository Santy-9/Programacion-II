from math import exp
from re import S


def ej():
    for x in range (0,10,2):
        print(x)    

def ej1():
    for x in range (10,0,-1):
        print(x)

def hola(nombre):
 return "Hola " + nombre + "!"

def saludar():
    nombre = input ("Por favor ingrese su nombre: ")
    saludo = hola (nombre)
    print(saludo)

def edad():
    peso = float (input("cuantos pesas? "))
    print (edad)
    print (peso >= 18)

def calculoIMC():
    peso = float (input ("Ingrese su peso: "))
    altura = float( input ("Ingrese su altura: "))
    IMC = peso / altura ** 2
    print("El IMC es", IMC)

#ej6

def factorial(n):
    fact = 1
    for x in range(1,n+1):
        fact = fact * x
    print(fact)    

#ej7

def ej7(n):
    for x in range(1,11):
        print(x*n)
       


#ej8

def ej8(palabra, cant, sep):
    for x in range (1, cant):
        print(palabra, end = sep)    
    print(palabra, "\n")

def main():
    string = input("Ingrese una palabra: ")
    n = int(input("Ingrese cantidad de repeticiones: "))
    separador = input("Ingrese separador: ")
    ej8(string, n, separador)

