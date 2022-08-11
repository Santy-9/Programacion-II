import matplotlib.pyplot as plt
import datetime
import time
import streamlit as st
import pandas as pd
import numpy as np
from csv import reader

#---------------------#
# Pregunta Alejandro  #
#---------------------#

# tiene_alojamiento_enfecha: alojamiento string -> boolean

# alojamiento: alojamiento.
# fecha: string

# tiene_alojamiento_enfecha: esta función recibe un alojamiento y una fecha en formato
# de string, devuelve un boolean indicando si el lugar está abierto o no
# en la fecha ingresada.


def tiene_alojamiento_enfecha(alojamiento, fecha):
    return alojamiento[1] == fecha

def test_tiene_alojamiento_enfecha():

    assert tiene_alojamiento_enfecha(['561418072780605554', '2022-12-24', 't', '$20.00', '$20.00', '1', '365'], '2022-12-24') == True
    assert tiene_alojamiento_enfecha(['543543353', '2022-12-21', 't', '$50.00', '$50.00', '6', '365'], '2022-12-24') == False

#esta_ocupado: alojamiento -> boolean

#alojamiento: alojamiento

#esta_ocupado: esta función recibe como parametro un alojamiento y devuelve un boolean dependiendo
#si está ocupado o no.

def esta_ocupado(alojamiento):
    return alojamiento[2] == "t"

def test_esta_ocupado():
    assert esta_ocupado(['561418072780605554', '2022-12-24', 't', '$20.00', '$20.00', '1', '365']) == True
    assert esta_ocupado(['543543353', '2022-12-21', 'f', '$50.00', '$50.00', '6', '365']) == False

#ocupados_disponibles: list list list ->

#listaalojamientos: list
#listadisponibles: list
#listaocupados: list

#ocupados_disponibles: esta función recibe tres listas, una lista con los alojamientos totales de cada día
#y dos listas vacías, toma los alojamientos de la primer lista de alojamientos y los separa en ocupados
#y disponibles en las otras dos listas.

def ocupados_disponibles(listaalojamientos, listadisponibles, listaocupados):
    
    for alojamiento in listaalojamientos:
        if esta_ocupado(alojamiento):
            listaocupados.append(alojamiento)
        else:
            listadisponibles.append(alojamiento)
            
#get_data1: list list list list list ->

#listaañonuevo: list
#listanaviad: list
#listadiadeltrabajo: list
#listalunesdepascua: list
#totalalojamientos: list

#getdata1: recibe cinco listas vacias, una del total de alojamientos y cuatro más, una para cada día festivo.
#itera sobre el archivo csv y guarda todos los alojamientos en la lista total de alojamientos y en las otras cuatro
#filtra los alojamientos segun si están abiertos esos días o no.

def get_data1(listaañonuevo,
              listanavidad,
              listadiadeltrabajo,
              listalunesdepascua,
              totalalojamientos):
    with open('calendar-modificado.csv', 'r') as file:

        csv_reader = reader(file)

        for alojamiento in csv_reader:

            totalalojamientos.append(list(alojamiento))

            if tiene_alojamiento_enfecha(alojamiento, "2022-12-31"):
                listaañonuevo.append(alojamiento)
            elif tiene_alojamiento_enfecha(alojamiento, "2022-12-24"):
                listanavidad.append(alojamiento)
            elif tiene_alojamiento_enfecha(alojamiento, "2022-05-01"):
                listadiadeltrabajo.append(alojamiento)
            elif tiene_alojamiento_enfecha(alojamiento, "2022-04-10"):
                listalunesdepascua.append(alojamiento)


# --------------------#
# Pregunta 2 Santiago #
# --------------------#

# Separar: Tuple String Tuple Tuple -> List(Tuple)
# Recibe una tupla con los barrios, un string con el barrio a elegir, una tupla con los nombres de los host, y el id de los host.
# Devuelve una lista de tuplas con el barrio elegido, el nombre e id de los hosts.
def Separar(barrios, nombreb, nombreh, id):
    l = []
    cont = 0
    for i in barrios:
        if (i == nombreb):
            l += [(i, nombreh[cont], id[cont])]
        cont += 1
    return l


# st.write(Separar(neighbourhood, "Penzing", host_name, host_id))

def test_Separar():
    assert Separar(("Alsergrund", "Penzing", "Favoriten", "Penzing", "Penzing"),
                   "Penzing",
                   ("Mario", "Martin", "Eva", "Michael", "Martin"),
                   (4587159, 4268935, 129864, 786219, 4268935)) == [("Penzing", "Martin", 4268935),
                                                                    ("Penzing", "Michael", 786219),
                                                                    ("Penzing", "Martin", 4268935)]


# Separar: Tuple String Tuple Tuple -> List
# Recibe una tupla con los barrios, un string con el barrio a elegir, y el id de los host.
# Devuelve una lista con los id unicos del barrio elegido.
def SepararSet(barrios, nombreb, id):
    l = []
    cont = 0
    for i in barrios:
        if (i == nombreb):
            l += [id[cont]]
        cont += 1
    l = tuple(set(l))
    return l


# st.write(SepararSet(neighbourhood, "Penzing", host_id))

def test_SepararSet():
    assert SepararSet(("Alsergrund", "Penzing", "Favoriten", "Penzing", "Penzing"),
                   "Penzing",
                   (4587159, 4268935, 129864, 786219, 4268935)) == (786219, 4268935)


# Separar: List(Tuple) List -> List(Tuple)
# Recibe una lista de tuplas de Separar, y una lista de SepararSet
# Devuelve una lista de tuplas con el nombre del host, el id y la cantidad de alquileres.
# Si la cantidad de alquileres no supera 1 se omite.
def Conteo2(l, l3):
    cont = 0
    cant = 0
    l1 = []
    for k in l3:
        for i in range(0, len(l)):
            if (l[i][2] == l3[cont]):
                cant += 1
                nombre = l[i][1]
        if (cant > 1):
            l1 += [(nombre, k, cant)]
        cont += 1
        cant = 0
    return l1


# st.write (Conteo2 (Separar(neighbourhood, "Penzing", host_name, host_id), (SepararSet(neighbourhood, "Penzing", host_id)))))

def test_Conteo2():
    assert Conteo2([("Penzing", "Martin", 4268935), ("Penzing", "Michael", 786219), ("Penzing", "Martin", 4268935)],
                   (4268935, 786219)) == [("Martin", 4268935, 2)]


# Nombre_Host: List(Tuple) -> List
# Recibe una lista de tuplas de Conteo2 y separa en una nueva lista los nombres de los host.
def Nombre_Host(l):
    l1 = []
    for i in l:
        l1 += [i[0]]
    return l1


def test_Nombre_Host():
    assert Nombre_Host([("Martin", 4268935, 2)]) == ["Martin"]


# ID: List(Tuple) -> List
# Recibe una lista de tuplas de Conteo2 y separa en una nueva lista los ID de los host.
def ID(l):
    l1 = []
    for i in l:
        l1 += [i[1]]
    return l1


def test_ID():
    assert ID([("Martin", 4268935, 2)]) == [4268935]


# Cantidad: List(Tuple) -> List
# Recibe una lista de tuplas de Conteo2 y separa en una nueva lista la cantidad de alquileres.
def Cantidad(l):
    l1 = []
    for i in l:
        l1 += [i[2]]
    return l1


def test_Cantidad():
    assert Cantidad([("Martin", 4268935, 2)]) == [2]


# --------------------#
# Pregunta 1 Santiago #
# --------------------#

# Separador: Tuple Tuple String -> List(Tuple)
# Recibe una tupla con los barrios y sus tipo de habitacion y una string con el tipo de habitacion
# a elegir y devuelve un tupla con las habitaciones elegidas y el nombre del barrio en la que se encuentra.
def Separador(barrios, habitaciones, tipo_habitacion):
    new = []
    cont = 0
    for i in habitaciones:
        if (i == tipo_habitacion):
            new += (i, barrios[cont])
        cont += 1
    return new


# st.write(Separador(neighbourhood, room_type, 'Shared room'))
# Entera = (Separador(neighbourhood, room_type, 'Entire home/apt'))
# Privada = (Separador(neighbourhood, room_type, 'Private room'))
# Compartida = (Separador(neighbourhood, room_type, 'Shared room'))
# Hotel = (Separador(neighbourhood, room_type, 'Hotel room'))

def Test_Separador():
    assert Separador(("Alsergrund", "Penzing", "Favoriten", "Penzing", "Liesing"),
                     ('Entire home/apt', 'Private room', 'Shared room', 'Hotel room', 'Private room'),
                     "Private room") == ('Private room', "Penzing"), ('Private room', "Liesing")


# Conteo: String Tuple Tuple String -> Integer
# Recibe una string con el nombre del barrio a elegir, una tupla con los barrios y los tipos de habitaciones, y una string 
# con el tipo de habitacion y devuelve la cantidad de dicha habitacion en el barrio elegido.
def Conteo(Nombre_barrio, neighbourhood, room_type, tipo_hab):
    cont = 0
    Sep = (Separador(neighbourhood, room_type, tipo_hab))
    for i in Sep:
        if (i == Nombre_barrio):
            cont += 1
    return cont


def Test_Conteo():
    assert Conteo("Penzing",
                  ("Alsergrund", "Penzing", "Favoriten", "Penzing", "Liesing"),
                  ('Entire home/apt', 'Private room', 'Shared room', 'Hotel room', 'Private room'),
                  "Private room") == 1


# Conteo_Total: String Tuple Tuple -> List
# Recibe una string con el barrio, una tupla con todos los barrios, y los tipos de habitaciones
# y devuelve una lista con las cantidades en los cuatro tipo de habitaciones de dicho barrio.
def Conteo_Total(barrio, neighbourhood, room_type):
    Ent = Conteo(barrio, neighbourhood, room_type, 'Entire home/apt')
    Priv = Conteo(barrio, neighbourhood, room_type, 'Private room')
    Comp = Conteo(barrio, neighbourhood, room_type, 'Shared room')
    Hot = Conteo(barrio, neighbourhood, room_type, 'Hotel room')
    total = [Ent, Priv, Comp, Hot]
    return total


def Test_Conteo_Total():
    assert Conteo_Total("Penzing",
                        ("Alsergrund", "Penzing", "Favoriten", "Penzing", "Liesing"),
                        ('Entire home/apt', 'Private room', 'Shared room', 'Hotel room', 'Private room')) == [0, 1, 0,1]


#----------------------#
# Pregunta 1 Alexandro #
#----------------------#

# asignacion(barrios, tipos): neighbourhood room_type --> list(tuple(neighbourhood, room_type))
# se ocupa de asignar a cada tipo de habitacion un barrio segun la tabla
def asignacion(barrios, tipos):
    if len(barrios) == len(tipos):
        l = []
        for i in range(0, len(barrios)):
            l += [(barrios[i], tipos[i])]
        return l
    else:
        return "error"
# casos de prueba:
assert asignacion(('Leopoldstadt', 'Alsergrund', 'Favoriten', 'Donaustadt'),
                  ('Entire home/apt', 'Hotel room', 'Hotel room', 'Private room')) == [
                  ('Leopoldstadt', 'Entire home/apt'), ('Alsergrund', 'Hotel room'), ('Favoriten', 'Hotel room'),
                  ('Donaustadt', 'Private room')]
assert asignacion(('Leopoldstadt', 'Alsergrund'), ('Private room')) == "error"
assert asignacion((), ()) == []



# calculo_zona(): asignacion(barrios, tipos) tuple(neighbourhood, room_type) --> int
# cuenta cuantos del elementos con el barrio y tipo de habitacion
# especificada hay en el objeto asignacion
def calculo_zona(tuple, buscado):
    cont = 0
    if tuple != ():
        for i in tuple:
            if i == buscado:
                cont += 1
        # print(cont)
        return cont
    else:
        return "error"
# casos de prueba:
assert calculo_zona([('Leopoldstadt', 'Entire home/apt'), ('Alsergrund', 'Hotel room'), ('Favoriten', 'Hotel room'),
                     ('Donaustadt', 'Private room'), ("Favoriten", 'Hotel room')], ("Favoriten", 'Hotel room')) == 2
assert calculo_zona((), ()) == "error"


# calculo_del_barrio(col, type, asignacion): list(string) string tuple(string) --> tuple(tuple(int, string), string, list(tuple(int, string)))
# calculo_del_barrio(col, type, asignacion): "neighbourhood_solos" "neighbourhood" "tipo de habitacion" --> el area (barrio) con mayor cantidad de "tipo de habitacion", el "tipo de habitacion", una lista con el barrio junto con su cantidad de "tipo de habitacion"
# calcula de todos los barrios, cual tiene mayor cantidad de "tipo de habitacion"
def calculo_del_barrio(col, type, asignacion):
    if col == {} or asignacion == []:
        return "error"
    cant = []
    for i in col:
        cant += [(calculo_zona(asignacion, (i, type)), i)]
    temporal = cant[0]
    for e in range(0, len(cant)):
        try:
            if temporal[0] >= cant[e + 1][0]:
                continue
            else:
                temporal = cant[e + 1]
        except:
            return (temporal, type, cant)

# casos de prueba:

#print(calculo_del_barrio({'Wieden', 'Ottakring', 'Donaustadt', 'Alsergrund'},
#                          'Entire home/apt',
#                          [('Leopoldstadt', 'Entire home/apt'), ('Alsergrund', 'Hotel room'),
#                           ('Favoriten', 'Hotel room'), ('Donaustadt', 'Private room')]
#                          ))

#assert calculo_del_barrio({'Wieden', 'Ottakring', 'Donaustadt', 'Alsergrund'},
#                          'Entire home/apt',
#                          [('Leopoldstadt', 'Entire home/apt'), ('Alsergrund', 'Hotel room'),
#                           ('Favoriten', 'Hotel room'), ('Donaustadt', 'Private room')]
#                          ) == ((0, 'Wieden'),'Entire home/apt', [(0, 'Wieden'), (0, 'Alsergrund'), (0, 'Ottakring'), (0, 'Donaustadt')])

#assert calculo_del_barrio({'Wieden', 'Ottakring', 'Donaustadt', 'Alsergrund'},
#                          'Hotel room',
#                          [('Leopoldstadt', 'Entire home/apt'), ('Alsergrund', 'Hotel room'),
#                           ('Favoriten', 'Hotel room'), ('Donaustadt', 'Private room')]
#                          ) == (
#                          (1, 'Alsergrund'),
#                          'Hotel room',
#                          [(0, 'Donaustadt'), (1, 'Alsergrund'), (0, 'Ottakring'), (0, 'Wieden')])

assert calculo_del_barrio({},
                          'Hotel room',
                          []) == "error"





# todas_las_graficas(graficas): None
# muestra las graficas que son tablas (dataframes)
def todas_las_graficas(graficas):
    for grafica in graficas:
        st.write("El barrio con mayor cantidad de ", grafica[2], "es ", grafica[1][1], "con ", grafica[1][0])
        grafica[0]





# creacion_data_frames(): neighbourhood_solos room_type_solo list(tuple(neighbourhood, room_type)) --> list(pd.DataFrame)
# crea el conjunto de tablas que seran guardadas en una lista
def creacion_data_frames(a, b, asignacion):
    l = []
    for i in b:
        z = calculo_del_barrio(a, i, asignacion)
        l += [(pd.DataFrame(z[2], columns=("Cantidad", "Barrio")), z[0], z[1])]
    return l


# separacion(l) list(tuple(string, int)) --> list(list(string), list(int))
# separa los datos en dos listas
def separacion(l):
    lista1 = []
    lista2 = []
    for i in l:
        try:
            lista1 += [i[0]]
            lista2 += [i[1]]
        except:
            return "error"
    return [lista1, lista2]

#casos de prueba:
assert  separacion([(1, 2), (3, 4)]) == [[1, 3], [2, 4]]
assert  separacion([(1, 2), (4)]) == "error"
assert  separacion([]) == [[], []]

# Funciones para st.map

# asigna: Tuple Tuple Tuple Tuple -> List(Tuple)
# Recibe una tupla con los barrios, sus tipo de habitacion, las latitudes y longitudes, y devuelve
# una lista de tuplas con las respectivas latitudes y longitudes de los hoteles.
def asigna(barrios, tipos, lat, lon):
    l = []
    cont = 0
    for i in tipos:
        if (i == "Hotel room"):
            l += [(barrios[cont], lat[cont], lon[cont])]
        cont += 1
    return l

def test_asigna():
    assert asigna(("Alsergrund", "Penzing", "Favoriten", "Alsergrund", "Penzing"),
                   ('Entire home/apt', 'Hotel room', 'Shared room', 'Hotel room', 'Private room'),
                   (48.203,48.958 ,48.598 ,48.167 ,48.759),
                   (16.358, 16.897, 16.679, 16.249, 16.453)) == [("Penzing", 48.958, 16.897),
                                                                ("Alsergrund", 48.167, 16.249)]


# separaLat: List(Tuple) String -> List
# Recibe una lista de tuplas con los barrios, sus latitudes y longitudes de los hoteles, y un barrio a elegir
# y devuelve una lista con las latitudes del barrio elegido.
def separaLat(l, barrio):
    lat = []
    for i in l:
        if (i[0] == barrio):
            lat += [i[1]]
    return lat

def test_separaLat():
    assert separaLat([("Penzing", 48.958, 16.897),("Alsergrund", 48.167, 16.249)],
                    "Penzing") == [48.958]


# separaLat: List(Tuple) String -> List
# Recibe una lista de tuplas con los barrios, sus latitudes y longitudes de los hoteles, y un barrio a elegir
# y devuelve una lista con las longitudes del barrio elegido.
def separaLon(l, barrio):
    lon = []
    for i in l:
        if (i[0] == barrio):
            lon += [i[2]]
    return lon

def test_separaLon():
    assert separaLon([("Penzing", 48.958, 16.897),("Alsergrund", 48.167, 16.249)],
                    "Penzing") == [16.897]




# Inicio(): void --> void
# inicia la aplicacion
def Inicio():
    df = pd.read_csv('listings.csv')  # usecols=["id", "name"]) # en usecols se especifican las columnas

    name = tuple(df["name"])  # hoteles
    name_solo = set(df["name"])  # print(name)

    neighbourhood = tuple(df["neighbourhood"])  # barrios
    neighbourhood_solos = set(neighbourhood)  # print(neighbourhood_solos)

    room_type = tuple(df["room_type"])  # toda la cantidad de tipo de habitaciones
    room_type_solo = set(room_type)  # print(room_type_solos)
    # {'Shared room', 'Private room', 'Hotel room', 'Entire home/apt'}

    latitud = tuple(df["latitude"])
    longitud = tuple(df["longitude"])

    host_id = tuple(df["host_id"])
    host_name = tuple(df["host_name"])

    df1 = pd.read_csv("neighbourhoods.csv")  # barrios
    neighbourhood_solos = tuple(df1["neighbourhood"])

    # ----------------------------Radio Button
    with st.sidebar:
        barrios = st.radio(
            "Barrios",
            neighbourhood_solos, )

    st.info("Pregunta 1 - Alexandro")

    st.success(
    """
    ¿Cual es el barrio con la mayor cantidad de hoteles de la ciudad? 
    ¿Y de habitaciones privadas? 
    ¿Y de habitaciones compartidas? 
    ¿Y de casa completa?

    + Mostrar por medio de tablas 
    """)




    asignaciones = asignacion(neighbourhood, room_type)
    todas_las_graficas(creacion_data_frames(neighbourhood_solos, room_type_solo, asignaciones))

    st.info("Pregunta 2 - Alexandro")

    st.success(
    """
    Mostrar la cantidad de hoteles por barrios
    + Usar la funcion map para representar la ubicacion de los hoteles
    + Usar un grafico de barras para mostrar la cantidad de hoteles por barrios
    """)

    st.header("Grafica de barras horizontales")
    # grafica de barras para la consigna 2
    datos = calculo_del_barrio(neighbourhood_solos, "Hotel room", asignaciones)
    print(datos[2])
    nuevo = separacion(datos[2])
    fig, ax = plt.subplots()
    # https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python
    ax.barh(nuevo[1], nuevo[0])
    ax.set_title('Grafica de cantidad de hoteles por barrio')
    st.pyplot(fig)

    # --  Mapa

    st.header("Ubicacion de los hoteles en el barrio elegido")
    #Si muestra el mapa completo quiere decir que no hay hoteles en el barrio.

    data = pd.DataFrame({
        'lat': separaLat(asigna(neighbourhood, room_type, latitud, longitud), barrios),
        'lon': separaLon(asigna(neighbourhood, room_type, latitud, longitud), barrios)})

    st.map(data)

    # --

    st.info("Pregunta 1 - Santiago")
    st.success("Cuáles son los 10 hosts con más alquileres en un barrio específico, y que cantidad de alquileres tienen ?")
    # -----------------Tabla
    #Sorted by "Cantidad" (descending)

    Host_id_unico = (SepararSet(neighbourhood, barrios, host_id))

    a = Nombre_Host(Conteo2(Separar(neighbourhood, barrios, host_name, host_id), Host_id_unico))
    b = ID(Conteo2(Separar(neighbourhood, barrios, host_name, host_id), Host_id_unico))
    c = Cantidad(Conteo2(Separar(neighbourhood, barrios, host_name, host_id), Host_id_unico))

    data1 = pd.DataFrame({
        'Nombre': (a),
        'id': (b),
        'Cantidad': (c)
    })

    st.dataframe(data1, None, 310)


    st.info("Pregunta 2 - Santiago")
    st.success(
        "Cuál es el porcentaje de casas enteras, habitaciones privadas, habitaciones compartidas y habitaciones de hoteles en un barrio ?")

    # ---------------------------Grafico de tortas
    col1, col2, col3, col4 = st.columns(4)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Entera', 'Privada', 'Compartida', 'Hotel'

    for cada_barrios in neighbourhood_solos:
        if (cada_barrios == barrios):
            sizes = (Conteo_Total(cada_barrios, neighbourhood, room_type))
            with col1:
                st.header("Enteras")
                st.write((Conteo_Total(cada_barrios, neighbourhood, room_type))[0])
            with col2:
                st.header("Privada")
                st.write((Conteo_Total(cada_barrios, neighbourhood, room_type))[1])
            with col3:
                st.header("Comp")
                st.write((Conteo_Total(cada_barrios, neighbourhood, room_type))[2])
            with col4:
                st.header("Hotel")
                st.write((Conteo_Total(cada_barrios, neighbourhood, room_type))[3])

    explode = (0.1, 0.1, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)





    # st.dataframe(df)

    df = pd.read_csv("calendar-modificado.csv")
    totalalojamientos = []

    dic_NocheVieja = {'Total': [], 'Ocupados': [], 'Disponibles': []}

    dic_Navidad = {'Total': [], 'Ocupados': [], 'Disponibles': []}

    dic_DiaDelTrabajador = {'Total': [], 'Ocupados': [], 'Disponibles': []}

    dic_LunesDePascuas = {'Total': [], 'Ocupados': [], 'Disponibles': []}

    dias = {'NocheVieja': dic_NocheVieja, 'Navidad': dic_Navidad, 'DiaDelTrabajo': dic_DiaDelTrabajador,
            'LunesDePascua': dic_LunesDePascuas}

    get_data1(dias['NocheVieja']['Total'], dias['Navidad']['Total'], dias['DiaDelTrabajo']['Total'],
              dias['LunesDePascua']['Total'], totalalojamientos)

    for key in dias:
        ocupados_disponibles(dias[key]['Total'], dias[key]['Ocupados'],
                             dias[key]['Disponibles'])

    st.info("Pregunta 1 - Alejandro")
    st.success("¿Cuáles son los alojamientos abiertos en los días festivos de la región? ¿Y cuáles están disponibles?")


    option = st.selectbox('Day', dias)
    st.write('You selected:', option)

    st.write('Filter by:')
    disponibles = st.checkbox('Disponibles')

    columns_names = df.columns.values

    for key in dias:
        if option == key:
            if disponibles:
                df = pd.DataFrame(dias[key]['Disponibles'], columns=columns_names)
            else:
                df = pd.DataFrame(dias[key]['Total'], columns=columns_names)

    st.dataframe(df)

    st.info("Pregunta 2 - Alejandro")
    st.success("¿Cuál es el porcentaje de alojamientos ocupados sobre el total de abiertos en cada uno de estos días?")

    for key in dias:
        if len(dias[key]['Total']) != 0:
            st.write(key + ":", (len(dias[key]['Ocupados']) * 100) / len(dias[key]['Total']), "%")
        else:
            st.write(key + ":", "No hay alojamientos disponibles en este día.")

if __name__ == "__main__":
    Inicio()





