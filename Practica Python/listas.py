# clear : None -> [x]


from cmath import log10


def eliminar_todos(list, n):
    '''
    eliminar_todos: [X] X -> [X]
    eliminar_todos([1,2,1,6,5,1],1) = [2,6,5]
    '''
    dato = n
    cantidad = list.count(dato)
    for i in range(0, cantidad):
        list.remove(dato)
    #return list

def eliminar_todos1(list, n):
    '''
    eliminar_todos1: [X] X -> [X]
    '''
    dato = n
    index = 0
    longitud = len(list)
    nueva_lista = []
    for index in range(0,longitud):
        if(list[index] != dato):
            nueva_lista.append(list[index])
    #return nueva_lista
    

def main():
  lista1 =[1,2,1,6,5,1] 
  lista2 =[]
  lista3 =[1,1,1,1,1]
  print(lista1)
  eliminar_todos1(lista1, 1)
  print(lista1)
  eliminar_todos1(lista1, 5)
  print(lista1)
  eliminar_todos1(lista1, 12)
  print(lista2)
  eliminar_todos1(lista2, 1)
  print(lista3)
  eliminar_todos1(lista3, 1)


#ej 1 
def PosicionesMultiplo(l, n):
    ''' PosicionesMultiplo : List Int -> List
        Recibe una  lista y, un número, y retorne la lista formada por los elementos que están en las posiciones múltiplos de ese número
        posicionesMultiplo([1,2,3,4,5,6,7],2) == [1,3,5,7]

    '''
    index = 0
    mult = 0
    long = len(l)
    l1 = []
    while(mult < long):
        l1.append(l[mult])
        mult += n
    return l1







