#Diseño de datos:
#Carta es: (valor, palo)
#siendo (Int, String)
#donde:
#-valor : el valor de la carta comprendido entre 1 y 13
#-palo : es un valor del conjunto {"Pica", "Corazon", "Diamante", "Trebol"}

def DatosValor(valor):
    return valor >= 1 and valor <= 13

def DatosPalo(palo):
    ''' DatosPalo String -> Boolean
        Determina si el palo dado es valido
    '''
    return palo == "Diamante" or palo == "Trebol" or palo == "Corazon" or palo == "Pica" 

def ValidarCarta(valor, palo):
    ''' ValidarCarta : Int String -> Boolean
        Determina si los valores dados correspenden a un valor y palo posibles.
        ValidarCarta(3, "Diamante") = True
        ValidarCarta(25, "Trebol") = False
    '''
    return DatosValor(valor) and DatosPalo(palo)
        

def CrearCarta(valor, palo):
    ''' CrearCarta : Int String -> Carta
        Crea una carta a partir de los valores asignados, verificando que sean correctos.
        CrearCarta(3, "Diamante") = (3, "Diamante")
        CrearCarta(24, "Trebol") = (-1, -1)
    '''
    if(ValidarCarta(valor, palo)):
        Carta = (valor, palo)
    else:
        Carta = "Error"
    print(Carta)
    return Carta

def es_poker(c):
    ''' es_poker : Carta -> Boolean
        Determina si las cartas forman poker(cuatro cartas con el mismo valor)
    '''
    if(c[0] == c[2] and c[0] == c[4] and c[0] == c[6]):
        resp = True
    elif(c[0] == c[4] and c[0] == c[6] and c[0] == c[8]):
        resp = True
    elif(c[0] == c[2] and c[0] == c[6] and c[0] == c[8]):
        resp = True
    elif(c[0] == c[2] and c[0] == c[4] and c[0] == c[8]):
        resp = True
    else:
        resp = False
    return resp
        
def main():
    v = int(input("Ingrese un valor: "))
    p = input("Ingrese el palo: ")
    cartas = CrearCarta(v, p)
    for i in range(1, 5):
         v = int(input("Ingrese un valor: "))
         p = input("Ingrese el palo: ")
         cartas = cartas + CrearCarta(v, p)
    print(es_poker(cartas))


def test_es_poker():
    assert es_poker((4, "Pica", 4, "Pica", 4, "Pica", 4, "Pica", 5, "Pica")) == True
    assert es_poker((4, "Pica", 5, "Pica", 4, "Pica", 4, "Pica", 4, "Pica")) == True
    assert es_poker((4, "Pica", 4, "Pica", 5, "Pica", 4, "Pica", 4, "Pica")) == True
    assert es_poker((4, "Pica", 4, "Pica", 4, "Pica", 5, "Pica", 4, "Pica")) == True
    assert es_poker((4, "Pica", 2, "Pica", 3, "Pica", 4, "Pica", 4, "Pica")) == False
