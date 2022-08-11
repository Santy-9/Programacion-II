######################################
#Ejemplo 1:
#######################################
# Un Diccionario para registrar la población de ciudades,
# queda definido por la estructura  {ciudad : población}
# para,
#	ciudad: String (clave)
# 	población: Int
# donde,
#	 población > 0
#######################################	

dic_población =  {"Nueva York":8550405,
				  "Los Angeles":3971883,
				  "Chicago":2720546,
				  "Houston":2296224,
				  "Rosario":1198528,
				  "Cordoba": 1391000 }

#type(dic_población)
#-print(dic_población)

dic_población["Paris"] = 12292895
dic_población["Berlín"]= 3769495 
dic_población["Buenos Aires"]=3075646 
dic_población["Mendoza"] = 1198528

#-print(dic_población)

#Accedemos a los datos por medio de los corchetes y las claves. 
#print(dic_población["Rosario"])
#print(dic_población["Cordoba"])
#print(dic_población["Bs As"]) #-- no existe la clave nos da ERROR!

#pensemos y hagamos! ¿Cómo hacemos para conocer la ciudad con la máxima población?

maximo = dic_población["Nueva York"]
clave_max = "Nueva York"
for claves in dic_población.keys():
  if dic_población[claves] > maximo:
    maximo = dic_población[claves]
    clave_max = claves

print ("La maxima población es: ", maximo)
print ("Ocurre en la ciudad de: ", clave_max)


minimo = dic_población["Nueva York"]
clave_min = dic_población["Nueva York"]
for claves in dic_población.keys():
    if dic_población[claves] < minimo:
        minimo = dic_población[claves]
        clave_min = claves

print("La minima poblacion es: ", minimo)
print("Ocurre en la ciudad de:  ", clave_min)

######################################
#Ejemplo 2:
#######################################
# Un Diccionario para traduccion de palabras en distinto idioma,
# queda definido por la estructura  {palabra : traducción}
# para,
#	palabra: String (clave)
# 	traducción: String
#######################################

#Español:Inglés
es_en = {"rojo":"red",
		 "verde":"green",
		 "azul":"blue",
		 "amarillo":"yellow"}

#Inglés:Francés
en_fr = {"red" : "rouge",
		 "green" : "vert",
		 "blue" : "bleu",
		 "yellow":"jaune"}

#Portugues:Español
pt_es = {"vermelho" : "rojo",
         "verde" : "verde",
         "azul" : "azul",
         "amarelo" : "amarillo"}



#print(es_en)
#print(es_en["rojo"])
#color="rojo"
#print("El color ", color,  " en frances es ", en_fr[es_en[color]])

#Las "claves" tienen que ser datos inmutables (strings, tuplas,números, etc.),
#mientras que los "valores" pueden ser de cualquier tipo:

#dic = { [1,2,3]:"abc"}

#Tuplas y números como claves:
dic = { (1,2,3):"abc", 3.1415:"cba"}
#print(dic)
#print(dic[(1,2,3)])
#print(dic[3.1415])

#Diccionarios como valores
diccionarios = {"es_en" : es_en, "en_fr" : en_fr, "pt_es" : pt_es }
#print(diccionarios["es_en"]["azul"])
#print(diccionarios["en_fr"]["blue"])

#Tarea:
#Utilizando google, buscar las traducciones en portugues de las claves (colores)
#del diccionario español e inglés. Crear un diccionario para esta traducción: pt_es
#(del portugues al español) agregarlo a los datos de diccionarios.
#Pedir al usuario que ingrese un color en portugués y traducirlo simultaneamente al:
#español, inglés, y el francés.

color = input("Ingrese color en portugues: ")
español = diccionarios["pt_es"][color]
ingles = diccionarios["es_en"][español]
frances = diccionarios["en_fr"][ingles]
print(color, "en español:", español, "en ingles:" ,ingles,"en frances:" ,frances)





