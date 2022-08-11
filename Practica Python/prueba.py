'''
def fmaximo(x, y):
    if(x > y):
        return x
    else:
        return y

def test_fmaximo():
    assert fmaximo(5, 6) == 6
    assert fmaximo(0, -5) == 0
    assert fmaximo(5,6) == 6
    assert fmaximo(3,0) == 3


def potencia(base, n):
    if (n == 0):
        return 1
    else:
        return potencia(base, n-1) * base


def test_potencia():
    assert potencia(5, 2) == 25
    assert potencia(3, 0) == 1
    assert potencia(1, 1) == 1


def pot_ele(b, n):
    if (n == 0):
        return 1
    elif(n % 2 == 0):
        return pot_ele(b, n/2) * pot_ele(b, n/2)
    else:
        return pot_ele(b,(n-1)/2) * pot_ele(b,(n-1)/2) * b



def test_pot_ele():
    assert pot_ele(5,4) == 625
    assert pot_ele(5,5) == 3125
'''

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


# ------------#
# Pregunta 1 #
# ------------#

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


# Conteo: String List(Tuple) String -> Integer
# Recibe una string con el nombre del barrio a elegir, una lista de tuplas de Separador, y una string con el tipo de habitacion y
# devuelve la cantidad de dicha habitacion en el barrio elegido.
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
                        ('Entire home/apt', 'Private room', 'Shared room', 'Hotel room', 'Private room')) == [0, 1, 0,
                                                                                                              1]


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