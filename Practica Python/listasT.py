#Lista de contactos.
#---------------------

#Lista de contactos:
#a) Diseño de datos
#b) Crear un contacto
#c) Ingresar un contacto
#d) Buscar un contacto
#e) Mostrar contactos existentes
#f) Eliminar un contacto
#g) Menu con todas las opciones anteriores

#a) Diseño de datos:
#¿Qué es un contacto?
#Administrar una agenda similar a la de un celular.


#nombre: string
#apellido: string
#telefono: int
#edad: int

#Un contacto es:
#(nombre, apellido, telefono, edad)
#donde:
    #nombre, apellido: string
    #telefono, edad: int
    #telefono, edad>=0

#TAREA: definir los seteadores de la tupla Contacto.

#Agenda: list(contacto)
#Agenda es una lista de contactos

#b) Crear un contacto:

#-Opción 1.

#crea_Contacto: string string int int -> Contacto
#crea_Contacto crea un elemento del tipo contacto con los datos ingresados
#Ejemplos:
    #crea_Contacto("Pedro", "Picapiedra", 4802649, 50) = ("Pedro", "Picapiedra", 4802649, 50)
    #crea_Contacto("Vilma", "Picapiedra", -1, 50)      = ("Vilma", "Picapiedra", 0, 50)
    #crea_Contacto("Bam-Bam", "Picapiedra", 4802649, -1) =("Bam-Bam", "Picapiedra", 4802649, 0)
    #crea_Contacto("Pablo", "Picapiedra", -1, -1)=("Pablo", "Picapiedra", 0, 0)
            
def crea_Contacto(nombre, apellido, telefono, edad):
    if (edad<0):
        edad=0
    if (telefono<0):
        telefono=0
    return (nombre, apellido, telefono, edad)

#testing

def test_crea_Contactos():
    assert crea_Contacto("Pedro", "Picapiedra", 4802649, 50)==("Pedro", "Picapiedra", 4802649, 50)
    assert crea_Contacto("Pedro", "Picapiedra", -1, 50)==("Pedro", "Picapiedra", 0, 50)
    assert crea_Contacto("Pedro", "Picapiedra", 4802649, -1)==("Pedro", "Picapiedra", 4802649, 0)
    assert crea_Contacto("Pedro", "Picapiedra", -1, -1)==("Pedro", "Picapiedra", 0, 0)

#c)
#-Opción 2-
#carga_Contacto: none-> Contacto
#Pide al usuario el ingreso de datos para crear el contacto
#Ejemplos:
    #Entrada: "Pedro" "Picapiedra" 4802649 50       Salida: ("Pedro", "Picapiedra", 4802649, 50)
    #Entrada: "Vilma" "Picapiedra" -1 50            Salida: ("Vilma", "Picapiedra", 0, 50)
    #Entrada: "Pedro" "Picapiedra" 4802649 -1       Salida: ("Pedro", "Picapiedra", 4802649, 0)
    #Entrada:
    

def carga_Contacto():
    nombre=input("Ingrese el nombre: ")
    apellido=input("Ingrese el apellido: ")
    telefono=int(input("Ingrese telefono: "))
    edad=int(input("Ingrese edad: "))
    if (edad<0):
        edad=0
    if (telefono<0):
        telefono=0
    return (nombre, apellido, telefono, edad)

#d)
#1) Búsqueda por nombre y apellido:

#busqueda_Contacto: [Contactos] String String->[Contacto]
#Nuestra agenda admite elementos repetidos. AL ingresar contacto no se chequea unicidad.
#Devolvemos todos los contactos que coincidan con el nombre y el apellido dado. También se podría haber considerado
#que retorne la primera coincidencia.
#Busca en la agenda dada los contactos que coinciden con el nombre y apellido especificado.
#Ejemplos:
#lista_contactos=
  #[("Pedro", "Picapiedra", 4802649, 50), 
  # ("Vilma", "Picapiedra", 4802649, 50), 
  # ("Monica", "Fein", 3413454632, 38),
  # ("Ana", "Lahacker", 0, 40),
  # ("Pablo", "Picasso", 4321212, 70),
  # ("Sanatorio", " ", 4202020, 0),
  # ("Pedro", "Picapiedra", 3471554499, 50)]
  
#   busqueda_Contactos(lista_Contacto, "Pablo", "Picasso")=[("Pablo", "Picasso", 4321212, 70)]
#   busqueda_Contactos(lista_Contacto, "Pedro", "Picapiedra")=[("Pedro", "Picapiedra", 4802649, 50), ("Pedro", "Picapiedra", 3471554499, 50)]
#   busqueda_Contactos(lista_Contacto, "Vilma", "Palma")=[]
#   busqueda_Contactios([], "Vilma", "Palma")=[]
#   busqueda_Contactos(lista_Contacto, " ", "Palma")=[]
#   busqueda_Contactos(lista_Contacto, "Sanatorio", " ")=[("Sanatorio", " ", 4202020, 0)]

def busqueda_Contactos(lista, nombre, apellido):
    longitud=len(lista)
    lista_resp=[]
    for i in range(longitud):
        contacto=lista[i]
        if (contacto[0]==nombre) and (contacto[1]==apellido):
            lista_resp.append(contacto)

    return lista_resp


#testing
def test_busqueda_Contactos():
    lista_Contactos=[("Pedro", "Picapiedra", 4802649, 50),
                     ("Vilma", "Picapiedra", 4802649, 50),
                     ("Pedro", "Picapiedra", 4812648, 50), 
                     ("Monica", "Fein", 3413454632, 38),
                     ("Ana", "Lahacker", 0, 40),
                     ("Pablo", "Picasso", 4321212, 70),
                     ("Sanatorio", " ", 4202020, 0)]
    assert busqueda_Contactos(lista_Contactos, "Pablo", "Picasso")==[("Pablo", "Picasso", 4321212, 70)]
    assert busqueda_Contactos(lista_Contactos,
                              "Pedro", 
                              "Picapiedra")== [("Pedro", "Picapiedra", 4802649, 50),
                                               ("Pedro", "Picapiedra", 4812648, 50)]
    assert busqueda_Contactos(lista_Contactos, "Vilma", "Palma")==[]
    assert busqueda_Contactos([], "Vilma", "Palma")==[]
    assert busqueda_Contactos(lista_Contactos, " ", "Palma")==[]
    assert busqueda_Contactos(lista_Contactos, "Sanatorio", " ")==[("Sanatorio", " ", 4202020, 0)]


def eliminar_contacto(l,nombre, apellido):
    '''
    '''
    lcontacto = busqueda_Contactos(l, nombre, apellido)
    cant = len(lcontacto)
    for i in range(0,cant):
        l.remove(lcontacto[i])
    return l

def eliminar_contacto1(l, contacto):
    cant = l.count(contacto)
    for i in range(0, cant):
        l.remove(contacto)
    return l

lista_contactos = [("Pedro", "Picapiedra", 3413454732, 50), 
                   ("Vilma", "Picapiedra", 4802649, 50), 
                   ("Monica", "Fein", 3413454632, 38),
                   ("Ana", "Lahacker", 0, 40),
                   ("Pablo", "Picasso", 4321212, 70),
                   ("Sanatorio", " ", 4202020, 0),
                   ("Pedro", "Picapiedra", 4802649, 50)]

print(eliminar_contacto(lista_contactos,"Pedro", "Picapiedra"))
print(eliminar_contacto1(lista_contactos, ("Pedro", "Picapiedra", 4802649, 50, )))











#TAREA 1:  definir la funcion buscar_elPrimerContacto (lista, nombre, apellido) que nos devuelte el primer contacto de la lista que coincide con el nombre y el apellido dado. 
  
#e) Mostrar contacto y agenda:
#1) mostrar_Contacto: Contacto -> None
#2) mostrar_Agenda: [Contacto] -> None

#1)Los datos aparecen de la siguiente forma:
#Apellido: "Picapiedra"
#Nombre: "Pedro"
#Telefono: 4802649      Edad: 50

#mostrar_Contacto: Contacto->None
#Muestra de una forma organizada el contacto dado en pantalla.
#Entrada:
#("Pedro", "Picapiedra", 4802649, 50)  
#Salida: 
#Apellido: "Picapiedra"
#Nombre: "Pedro"
#Telefono: 4802649      Edad: 50

def mostrar_Contacto(contacto):
    print("Apellido: ", contacto[1])
    print("Nombre: ", contacto[0])
    print("Telefono: ", contacto[2], "\t Edad: ", contacto[3])

#2) Los datos aparecen de la siguiente forma:
    
#===========================
#Contacto:0
#Apellido: Picapiedra
#Nombre: Pedro
#Telefono: 4802649  Edad: 50
#===========================

#===========================
#Contacto:1
#Apellido: Picapiedra
#Nombre: Vilma
#Telefono: 4802649  Edad: 50
#===========================

#mostrar_Agenda: [Contacto]->None
#Muestra los datos de la agenda según lo especificado anteriormente.
#Ejemplo:

#Entrada:

#[("Pedro", "Picapiedra", 4802649, 50), ("Vilma", "Picapiedra", 4802649, 50)]

#Salida:

#===========================
#Contacto:0
#Apellido: Picapiedra
#Nombre: Pedro
#Telefono: 4802649  Edad: 50
#===========================

#===========================
#Contacto:1
#Apellido: Picapiedra
#Nombre: Vilma
#Telefono: 4802649  Edad: 50
#===========================

def mostrar_Agenda(lista):
    longitud=len(lista)
    for i in range(longitud):
        print("="*30)
        print("Nro Contacto: ", i)
        mostrar_Contacto(lista[i])
        print("="*30)

#g) TAREA 2: Diseñar el menú que nos permita ejecutar estas primeras tres acciones: Ingresar, Mostrar y Buscar (el primero y todos)
#1) Menú simple:
#       1) Ingresar contacto
#       2) Mostrar agenda
#       3) Buscar el primero 
#       4) Buscar todos 
#       5) Salir

