import math

def Num():
    resp = int(input("Ingrese numero: "))
    if (resp > 0):
        print("Numero positivo")
    elif (resp < 0):
        print("Numero negativo")
    else:
        print("Es cero")


def ej6a(n):
    if(n % 2 == 0):
        print("Par")
    else:
        print("Impar")

def ej6b(n, f):
    if(n % f == 0):
        print(n, "es multiplo de", f )
    else:
        print(n, "no es multiplo de", f )

def ej7(n):
    if(n >= 0):
        print(n)
    else:
        print(-n)

#cuadratica = (-b +- raiz(b ** 2 - 4 * a * c) )/ 2 * a

def ej8(a, b, c):
    delta = b**2 - 4*a*c
    if(delta > 0 and a != 0):
        raiz =  math.sqrt(delta)
        x1 = ((-b + raiz) / 2 * a)
        x2 = ((-b - raiz) / 2 * a)
        print("La primera raiz es: x1 = ",x1 ,"y la segunda raiz es: x1 = ",x2 )
    else:
        print("No se puede realizar la raiz cuadradada")

def main():
    a = float(input("Ingrese primer termino: "))
    b = float(input("Ingrese segundo termino: "))
    c = float(input("Ingrese termino independiente: "))
    ej8(a, b, c)

def ej9a(año):
    if(año % 4 == 0 and not(año % 100 == 0) or año % 400 == 0):
        print(año, "es bisiesto")
    else:
        print(año, "no es bisiesto")

def ej9b(mes):
    if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
        print("31 dias")
    elif(mes==4 or mes==6 or mes==9 or mes==11):
        print("30 dias")
    else:
        print("28 dias")

def ej9c(mes):
    if(mes == 1):
        return "Enero"
    elif(mes == 2):
        return("Febrero")
    elif(mes == 3):
        return "Marzo"
    elif(mes == 4):
        return("Abril")
    elif(mes == 5):
        return("Mayo")
    elif(mes == 6):
        return("Junio")
    elif(mes == 7):
        return("Julio")
    elif(mes == 8):
        return("Agosto")
    elif(mes == 9):
        return("Septiembre")
    elif(mes == 10):
        return("Octubre")
    elif(mes == 11):
        return("Noviembre")
    elif(mes == 12):
        return("Diciembre")
    else:
        return(mes, "No representa un mes")

def ej9d(d, m, a):
    print(d, "de", ej9c(m), "de", a)

def ej10a(h, m ,s):
    if(s >= 0 and s < 60 and m >= 0 and m < 60): 
        return(h * 3600 + m * 60 + s)
    else:
        return("Erorr")

def ej10b(s):
    seg = s % 60
    if(s / 60 >= 60):
        min = (s / 60) % 60
        hor = (s / 60) / 60 
    else:
        min = s / 60
        hor = 0

    print("H:",int(hor),"M:", int(min),"S:", seg)

def ej11():
    h = int(input("Ingrese Hora: "))
    m = int(input("Ingrese Minuto: "))
    s = int(input("Ingrese Segundo: "))
    h1 = int(input("Ingrese Hora: "))
    m1 = int(input("Ingrese Minuto: "))
    s1 = int(input("Ingrese Segundo: "))
    seg = ej10a(h, m, s) + ej10a(h1, m1, s1)
    ej10b(seg)

def ej13(t):
    if(t < 0):
        print("Helado")
    elif(t >= 0 and t < 10):
        print("Frio")
    elif(t >= 10 and t < 15):
        print("Fresco")
    elif(t >= 15 and t < 25):
        print("Agradable")
    elif(t >= 25 and t < 32):
        print("Caluroso")
    else:
        print("Muy Caluroso")

    if(t <= 15):
        print("No usar protector solar")
    else:
        print("Usar protector solar")

def ej14(d):
    if(d % 7 == 1):
        print("Lunes")
    elif(d % 7 == 2):
        print("Martes")
    elif(d % 7 == 3):
        print("Miercoles")
    elif(d % 7 == 4):
        print("Jueves")
    elif(d % 7 == 5):
        print("Viernes")
    elif(d % 7 == 6):
        print("Sabado")
    elif(d % 7 == 0):
        print("Domingo")
    else:
        print("Error")

#18,19,20

def ej18(n, m):
    for i in range(m, (n+m)*2):
        if(i % 2 == 0):
            print(i)
        
def ej21():
    '''Representamos la nota como un numero entero.
        n: int
       ej21: int -> String
        El parametro representa una nota de parcial y devuelve la condicion.
       ej21(2) = "Insuficiente"
       ej21(6) = "Aprobado"
       ej21(10) = "Excelente"
    '''

    for i in range(1,11):
        n = int(input("Ingrese nota 1: "))
        n1 = int(input("Ingrese nota 2: "))
        n2 = int(input("Ingrese nota 3: "))
        prom = (n + n1 + n2) / 3
        
        if(prom >= 1 and prom < 4):
            print("Nota",i, ": Insuficiente")
        elif(prom >= 4 and prom < 6):
            print("Nota",i, ": No aprobado")
        elif(prom >= 6 and prom < 8):
            print("Nota",i, ": Aprobado")
        elif(prom >= 8 and prom < 10):
            print("Nota",i, ": Muy bueno")
        else:
            print("Nota",i, ": Excelente")
