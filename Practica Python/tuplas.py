import math
from re import X
from tracemalloc import reset_peak
'''
#TUPLAS
#-Las Tuplas permiten agrupar información. 
#-Las Tuplas en Pyhton son el equivalente al define-struct de Racket.

#¿Cómo las escribimos?
T1 = (25,"Mayo",1810) # fecha como tupla
T2 = (1,5,2019) # fecha como tupla

T0 = () #tupla vacía
T3 = (3,) #tupla unitaria (ojo debe contener la coma)  

 # ¿Cuál el es tipo asociado?
print(type(T1))
print(type(T2))


#¿Cómo representamos una fecha?
T4 = (9,7,1816) # fecha como tupla
T5 = (2,"Abril",1982) # fecha como tupla

#Ambas representaciones estan bien, pero es importante dejar el diseño de la tupla de antemano. Por ejemplo para el diseño uno tendríamos:

# Diseño de datos 1:
# Una Fecha es: (dia,mes,año)
# siendo (Int, String, Int)
# donde:
# -dia : el dia es un valor comprendidon entre 1 y 31
# -mes : es un valor del conjunto {Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dec"}
# -año : es un entero positivo.

print(T1)
print(type(T1))
print(T5)
print(type(T5))


# Diseño de datos 2:
# una Fecha es: (dia,mes,año)
# siendo (Int, Int, Int)
# donde:
# -dia : el dia es un valor comprendido entre 1 <= dia <= 31
# -mes : es un valor comprendido entre 1 <= mes <= 12
# -año : es un entero positivo, año >=0

#¿Cómo construimos una tupla de tipo Fecha?

 # Opcion 1: new_Fecha: Int Int Int -> (Int, Int, Int)
 # Opción 2: new_Fecha: Int Int Int -> Fecha

def esBisiesto (año):
  """ año: Integer
      esBisiesto: Integer -> Boolean
      Usando la regla de que un año es bisiesto si es divisible por cuatro, y no divisible por 100, o es divisible por 4 y divisible por 400.
  esBisiesto(2000)= True
  esBisiesto(2400)= True
  esBisiesto(1900)= False
  esBisiesto(1988)= True
  """
  divisible4 = (año % 4 == 0)
  divisible100 = (año % 100 == 0)
  divisible400 = (año % 400 == 0)
  return (divisible4 and (not divisible100 or divisible400))

def datos_fuera_rango(dia, mes, año):
  return (año < 0) or (mes >12) or (mes <1) or (dia >31) or (dia <1)

def datos_mes_31(dia, mes, año):
  return (((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)) and (1 <= dia <= 31))


def datos_mes_30(dia, mes, año):
  return (((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)) and (1 <= dia <= 30))
    
def validar_Fecha (dia, mes, año):
  """
  validar_Fecha: Int Int Int -> Boolean
  Determina si los valores dados corresponde a
  un día posible, un mes posible, y un año 
  posible. 
  validar_Fecha(10,5,2021) = #True
  validar_Fecha(32,1,2021) = #False
  validar_Fecha(2,-1,2021) = #False
  validar_Fecha(2,11,-5)   = #False
  """
  if datos_fuera_rango(dia, mes, año):
     respuesta = False
  elif datos_mes_31(dia, mes, año):
     respuesta = True
  elif datos_mes_30(dia, mes, año):
     respuesta = True
  elif (mes == 2) and not esBisiesto(año) and (1 <= dia <= 28):
     respuesta = True
  elif (mes == 2) and esBisiesto(año) and (1 <= dia <= 29):
     respuesta = True
  else: respuesta = False
                                                             
  return respuesta



def new_Fecha (dia, mes, año):
  """
  new_Fecha: Int Int Int -> Fecha
  Crea una Fecha validando los datos para que se ajusten a las restricciones que nos pide el diseño del tipo Fecha.
  new_Fecha(10,5,2021) = (10,5,2021)
  new_Fecha(32,1,2021) = (-1, -1, -1)
  new_Fecha(2,-1,2021) = (-1, -1, -1)
  new_Fecha(2,11,-5)   = (1, -1, -1)
  """
  if validar_Fecha (dia, mes, año):
    respuesta =(dia, mes, año)
  else:
    respuesta =(-1,-1,-1)
  
  return respuesta

print(validar_Fecha (12,5,1988))
print(validar_Fecha (-12,5,1988))
print (new_Fecha (10,4,1988))
'''
#a = 15
#b = 20
#c = "hola"
#tupla = (a, b, c)
#tupla[0] == 15
#len(tupla) == 3

#diseño producto supermercado
#un producto es (codigo, fecha_vencimiento, fecha_elaborado, precio, nombre)
#Siendo (Int, Fecha, Fecha, Float, String)
#Donde:
#   -codigo: es un dato numerico que identifica al producto
#   -fecha_vencimiento: 
#prod1 = (3031, (25, 4, 2022), (3, 1, 2022), 500, "Chocolate")

from itertools import product
from lib2to3.pytree import convert


fecha1 = (25, 5, 1990)

def convertir_mes(mes):
    '''
        mes : Integer
        convertir_mes : Int -> String
        Recibe el mes en numero y lo devuelve en letras.
        convertir_mes(7) = "Jul"
        convertir_mes(12) = "Dec"
    '''
    meses = ("Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic")
    return meses[mes-1]

def convertir_fecha(fecha1):
    '''
        fecha1 : Fecha
        convertir_fecha : Fecha -> Fecha
        Recibe una fecha con el mes en numero y lo devuelve en letras.
        convertir_fecha((25, 5, 1990)) = (25, "May", 1990)
        convertir_fecha((7, 10, 2015)) = (7, "Oct", 2015)
    '''
    fecha2 = (fecha1[0], convertir_mes(fecha1[1]), fecha1[2])
    return fecha2

def test_convertir_fecha():
    assert convertir_fecha((25, 5, 1990)) == (25, "May", 1990)
    assert convertir_fecha((7, 10, 2015)) == (7, "Oct", 2015)

nombre = "Carina"
nombre1 = "K" + nombre[1:]

nombre2 = "Veronika"
nombre3 = nombre2[:3] + "ó" + nombre2[4:6] + "c" + nombre2[7:]

nombre4 = "don josé de san martín"
nombre5 = "D" + nombre4[1:4] + "J" + nombre4[5:12] + "S" + nombre4[13:16] + "M" + nombre4[17:]

t1 = (1, "Abril", 1810)
t2 = t1[:1] + ("Mayo",) + t1[2:]
t3 = (25,) + t1[1:]
t4 = t1 [:2] + (1816,)

#Diseño
#Persona es (nombre, apellido, DNI, telefono, edad)
#siendo     (String, String, Integer, Integer, Integer)
p1 = ("Pedro", "Picapiedra", 41489259, 4092381, 35)

def set_telefono(persona, telefono):
    ''' 
        telefono : Integer
        set_telefono : persona Integer -> persona
    '''
    persona = persona[:3] + (telefono,) + persona[4:]
    return persona

def mostrar_persona(persona):
    '''Mostramos adecuadamente los campos de la persona
        mostrar_persona : Persona -> None
    '''
    print("Nombre: \t ", persona[0])
    print("Apellido:\t ", persona[1])
    print("DNI:    \t ", persona[2])
    print("Telefono:    \t ", persona[3])
    print("Edad:    \t ", persona[4])


#Diseño:
#Una Coordenada en el plano es: (x, y)
#siendo (float, float)
#donde:
#- x: representa la coordenada en el eje x
#- y: representa la coordenada en el eje y
def suma_puntos(punto1, punto2):
  """
  punto: Coordenada
  suma_puntos: Coordenada Coodenada ->Coordenada
  Suma dos coordenadas matemáticamente, es decir, componente a componente.
  suma_puntos ((1,1),(2,3)) = (3,4)
  suma_puntos ((0,0),(2,3)) = (2,3)
  suma_puntos ((-1,1),(2,3)) = (1,4)
  """
  respuesta = (punto1[0]+punto2[0], punto1[0]+punto2[0])
  return respuesta

def mult_puntos(punto1, n):
  """
  punto: Coordenada
  n: Float
  suma_puntos: Coordenada Float -> Coordenada
  Multiplica una coordenada por un numero.
  mult_puntos ((1,3), 2) = (2,6)
  mult_puntos ((0,0), 1) = (0,0)
  mult_puntos ((-1,1), 3) = (-3,3)
  """
  respuesta = (punto1[0] * n, punto1[1]*n)
  return respuesta

def producto_escalar(punto1, punto2):
  """
  punto: Coordenada
  suma_puntos: Coordenada Coordenada -> Float
  Calcula el prducto escalar entre dos puntos.
  producto_escalar ((1,1), (3,5)) = 8
  producto_escalar ((0,0), (3,5) = 0
  producto_escalar ((0,2), (3,5) = 10
  """
  x1,y1 = punto1
  x2,y2 = punto2
  respuesta = x1*x2 + y1*y2
  return respuesta

def dist_puntos(punto1, punto2):
  """
  punto: Coordenada
  dist_puntos: Coordenada Coordenada -> Float
  Calcula la distancia entre dos puntos.
  dist_puntos ((-4,-3), (2,5)) = 8
  dist_puntos ((-2,6), (-5,2) = 5
  dist_puntos ((0,2), (3,5) = 4.24
  """
  x1,y1 = punto1
  x2,y2 = punto2
  x = (x2 - x1) ** 2 
  y = (y2 - y1) ** 2
  respuesta = math.sqrt(x + y)
  return round(respuesta,2)

def esta_ejeX(punto):
  '''
    punto: Coordenada
    esta_ejeX: Coordenada -> Boolean
    Determina si el punto se encuentra en el eje x.
    esta_ejeX ((0,4)) = False
    esta_ejeX ((1,4)) = False
    esta_ejeX ((4,0)) = True
    esta_ejeX ((0,0)) = True
  '''
  return (punto[1] == 0)

def cuadrante(punto):
  '''
  punto: Coordenada
  cuadrante: Coordenada -> String
  Recibe un punto y determina en que cuadrante esta.
  cuadrante((1,1)) = "Primer cuadrante"
  cuadrante((-1,1)) = "Segundo cuadrante"
  cuadrante((-1,-1)) = "Tercer cuadrante"
  cuadrante((1,-1)) = "Cuarto cuadrante"
  cuadrante((0,0)) = "Todos los cuadrantes"
  '''
  x,y = punto

  if(x > 0 and y > 0):
    respuesta = "Primer cuadrante"
  elif(x < 0 and y > 0):
    respuesta = "Segundo cuadrante"
  elif(x < 0 and y < 0):
    respuesta = "Tercer cuadrante"
  elif(x > 0 and y < 0):
    respuesta = "Cuarto cuadrante"
  else:
    respuesta = "Todos los cuadrantes"
  return respuesta


#Recorriendo Secuencias-----------------------------------------------------------------------------------

# Secuencia for sobre un string:

for letra in "Hola":
	print (letra, end = "\t")
	
	
# De la misma forma para la secuencia tupla:
print ("\n")
for lenguaje in ("Racket","Python","C","Java"):
	print("Hola mundo! estoy en ",lenguaje)
	
	
# Ahora utilizando while:

lenguajes = ("Racket","Python","C","Java")
index = 0
longitud = len(lenguajes)
while(index < longitud):
	print("Hola mundo! estoy en",lenguajes[index])
	index += 1

# Empaquetado y desempaquetado de elementos:

# Empaquetar (armar la tupla):
# >> a = "Hola"
# >> b = "Casa"
# >> c =  1234
# >> t = (a,b,c)    (Construye, empaqueta la tupla)
# >> type(t)        

# Desempaquetar (desarmar la tupla):
# >> t = ("Pedro","Picapiedra",15)
# >> nom, ape, edad = t
# >> nom
# >> ape
# >> edad

# Errores(Desempaquetado):
# >> nom, ape, edad, tel = t	(Error en el interprete, sobra un elemento)
# >> nom, ape = t				(Error en el interprete, falta un elemento)
# >> nom, nom, nom = t			(Error no detectado en el interprete, error de diseño. 'nom' asume el ultimo valor, 15 en este caso)

# Transformación:
# >> tuple("Casa")
# >> s = "Verónica"
# >> t = tuple(s)
# >> t 


def es_panagrama2():
	"""
	Palabra: 
		String
	es_panagrama: 
		None -> None
	Proposito: 
		Verifica si una palabra es un panagrama.
	Ejemplos:
		Entrada E/S: "Paralelepipedo", Salida I/O: "No es un panagrama"
		Entrada I/O: "Murcielago", Salida I/O: "Es un panagrama"
	"""
	palabra = input("Ingrese una palabra: ")
	contador = 0
	for vocal in ("a","e","i","o","u"):
		if (vocal in palabra):
			contador += 1
			
	if (contador == 5):
		print("Es un panagrama")
	else:
		print("No es un panagrama")

def es_panagrama(palabra):
	"""
	Palabra: 
		String
	es_panagrama: 
		String -> Booleano
	Proposito: 
		Verifica si una palabra es un panagrama.
	Ejemplos:
		Entrada E/S: "Paralelepipedo", Salida I/O: "No es un panagrama"
		Entrada I/O: "Murcielago", Salida I/O: "Es un panagrama"
	"""
	contador = 0
  #palabra= sexagesimocuarto
  #palabra = albaricoque
  # letra {m, u, r, c, i, e, l, a, g, o }
for letra in palabra:
  # chequear si  letra es vocal.
  # si es vocal procesala vocal actualizando el contador correspondiete a la vocal encontrada seguir con siguiente letra
  # si no es vocal no hago nada, paso a la siguiente letra

 
  #for vocal in ("a","e","i","o","u"):
	#	if (vocal in palabra):
	#		contador += 1
  #contador = cantA + cantE+ cantI+ cantO+cantU
  resultado = (cantA >= 1) and (cantE >= 1) and(cantI >= 1) and(cantO >= 1) and (cantU >= 1)
  return resultado


def main():
  for i in range(5):
    palabra = input("Ingrese una palabra: ")
    palabra_normaliza = normalizar_palabra(palabra)
    if es_panagrama(palabra):
      print("Es un panagrama")
    else:
      print("No es un panagrama")

    

main()

#Se nos pide:
#1) Hacer que la función sea testeable
#2) Chequear que sucede si la palabra tiene mas de una vocal repetida.
#3) Normalizar la palabra.
#4) Chequear una cantidad indefinida de veces si una palabra es una panagrama o no.

#Extra:
#Palabras con una sola vocal:
# - ananá
# - bebé
# - vivir
# - oso
# - tutú.
# Escribir una funcion que detecte si la palabra que se ingreso contiene solamente un único tipo de vocal. 
# Escribir dos versiones una usando el operador "in" y otra sin usarlo. 

