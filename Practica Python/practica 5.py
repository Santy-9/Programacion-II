def ej1():
    for i in range (10, 21):
        print(i)


def ej2():
    ''' Diseño: 
            Numero: Integer
        Signatura:
            Nat -> Nat
        Proposito:
            Dados n numeros ingresados calcular el factorial de cada uno
        Ejemplos:
            
    '''
    cant = int(input("Ingrese cantidad: "))
    n = int(input("Ingrese numero: "))
    for i in range(0,cant-1):
        print( factorial(n))
        n = int(input("Ingrese numero: "))
    print(factorial(n)) 

def factorial(n):
    if(n == 0):
        return 1
    else:
        return( n*factorial(n-1))

#ej 3

def main():
    for i in range(0, 121, 10):
        print(far_cel(i))

def far_cel(temp_f):
    temp_c = (temp_f -32)*5/9
    return temp_c


#def ej4 (c, x, n):
def ej8(s, c):
    ''' s : Int
        c : Int
        ej8 : Int Int -> Float

    '''
    if(c == 0):
        prom = "Division por 0"
    else:
        prom = s / c
    return prom

def main():
    ''' main : None -> None
        
    '''
    cont = 0
    suma = 0
    
    n = int(input("Ingrese un numero natural o -1 para salir: "))
    while(n != -1):
        cont += 1
        suma += n
        n = int(input("Ingrese un numero natural o -1 para salir: "))
    
    print("Cantidad de numeros ingresados:", cont,"\nSuma total:", suma,"\nPromedio:", ej8(suma, cont) )



