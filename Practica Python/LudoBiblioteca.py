#libro es: (Nombre del autor, titulo, año de edicion, cantidad de paginas, posicion en el estante)
#siendo: (String, String, Int, Int, Int)
#donde :
#   -

#juego es: (Nombre, cantidad de jugadores, fabricante, posicion en el estante)
#siendo: (String, Int, String, Int)
#donde :
#   -

def crear_libro(NombreA, Titulo, Año, CantPaginas, PosEstante):
    '''
        crear_libro : String String Int Int Int -> Tupla
        Recibe la informacion de un libro y construye una tupla
    '''
    return (NombreA, Titulo, Año, CantPaginas, PosEstante)

def crear_juego(Nombre, CantJugadores, Fabricante, PosEstante):
    '''
        crear_juego : String Int String Int -> Tupla
        Recibe la informacion de un juego y construye una tupla
    '''
    return (Nombre, CantJugadores, Fabricante, PosEstante)

libro1 = crear_libro("Charles Perrault" , "Caperucita roja y el lobo", 2015, 5, 1)

def inicializar():
    '''
        inicializar : None -> List
    '''
    a = input("Ingrese nombre autor: ")
    b = input
    libro = crear_libro("Charles Perrault" , "Caperucita roja y el lobo", 2015, 5, 1)
