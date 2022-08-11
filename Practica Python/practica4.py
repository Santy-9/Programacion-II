from urllib import response


def ej1a(s):
    ''' s : String
        ej1a : String -> String
        Imprime los dos primeros caracteres.
        ej1a("Hola") = "Ho"
    '''
    return s[0]+s[1]

def main():
    s = input("Ingrese palabra a: ")
    print(ej1a(s))
    
def test_ej1a():
    assert ej1a("Hola") == "Ho"



def ej1b(s):
    ''' s : String
        ej1b : String -> String
        Imprime los tres ultimos caracteres.
        ej1("Hola") = "alo"
    '''
    return s[-1]+s[-2]+s[-3]

def main():
    s = input("Ingrese palabra b: ")
    print(ej1b(s))

def test_ej1b():
    assert ej1b("Hola") == "alo"



def ej1c(s):
    ''' s : String
        ej1c : String -> String
        Imprime la cadena cada dos caracteres.
        ej1c("Recta") = "Rca"
    '''
    
    return s[0]+s[0+2]+s[0+4]

def main():
    s = input("Ingrese palabra: ")
    print(ej1c(s))



def ej1d(s):
    ''' s : String
        ej1d : String -> String
        Imprime la cadena en sentido inverso.
        ej1c("hola mundo!") = "!odnum aloh"
    '''
    Resp = ""
    Resp += s[-1]
