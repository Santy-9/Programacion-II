from traceback import print_tb


def cuentaregresiva(n):
    ''' Diseño:
            Número: Natural.
        Signatura:
            Nat->None
        Propósito:
            Realiza una cuenta regresiva a partir de un numero
            natural dado, imprimiendo en pantalla un
            mensaje al llegar al valor cero.
    '''
    if(n == 0):
        print("Achis!!")
    else:
        print(n)
        cuentaregresiva(n-1)

def factorial(n):
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
    if(n == 0):
        return 1
    else:
        return( n*factorial(n-1))

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1

def main():
    n = int(input("Ingrese numero: "))
    print(factorial(n))


def factorial_pasos(n):
    print("--DEB: La función factorial se invocó con n = ", n )
    if n == 0:
        return 1
    else:
        resultado = n*factorial_pasos(n-1)
        print("--DEB: El resultado intermedio para ", n, " * factorial (", n-1, "): ", resultado)
        return resultado

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

def main():
    n = int(input("Ingrese numero: "))
    print(fibonacci(n))


def lucca(n):
    ''' n : Int
        lucca : Int -> Int
        Recibe un numero
        lucca(0) = 2
        lucca(1) = 1 
    '''
    if(n == 0):
        return 2
    elif(n == 1):
        return 1
    else:
        return lucca(n-1) + lucca(n-2)

def pell(n):
    ''' n : Int
        pell : Int -> Int
        Recibe un numero
        lucca(0) = 0
        lucca(0) = 1 
    '''
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return 2*pell(n-1) + pell(n-2)

def jacob(n):
    ''' n : Int
        jacob : Int -> Int
        Recibe un numero
        lucca(0) = 0
        lucca(0) = 1 
    '''
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return jacob(n-1) + 2*jacob(n-2)

def ej3a(n):
    ''' n : Int
        ej3a : Int -> Int
        Calcula la suma de los primeros n numeros naturales.
    '''
    if(n == 1):
        return 1
    else: 
        return n + ej3a(n-1)

def ej3c(n, m):
    ''' n : Int
        m : Int
        ej3c : Int Int -> Int
    '''
    if(n == m):
        return m
    else:
        return n + ej3c(n + 1,m)

def ej3d(n, k):
    if(n == 1):
        return k
    else:
        return k*n, ej3d(n-1, k) 

def div_nat(n, m):
    ''' n : Int
        m : Int
        div_nat : Int Int -> Int
    '''
    if(m > n):
        return 0
    else:
        return div_nat(n-m ,m)+1
    

