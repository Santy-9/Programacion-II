#Funes Santiago
#41489259

def convertir_claveMaestra(primaria, secundaria):
	''' convertir_ClaveMaestra : String String-> String
		Recibe la clave primaria y secundaria y devuelve la clave maestra
		convertir_claveMaestra("452", "78") = "47582"
		convertir_claveMaestra("895", "216") = "829156"
		convertir_claveMaestra("094", "12") = "01924"
	'''
	tamano = len(primaria) + len(secundaria)
	tamanoP = len(primaria)
	tamanoS = len(secundaria)
	PS = primaria + secundaria 
	clave = ""
	for i in range(0,tamano):
		if(i % 2 == 0):
			clave = clave + PS[i]
		else:
			clave = clave + PS[i]
			
	#clave = primaria[0] + secundaria[0] + primaria[1] + secundaria[1] + primaria[2]
	return clave
	
	

print(convertir_claveMaestra("452", "78"))


def extraer_ClavePrimaria(ClaveMaestra):
	''' extraer_ClavePrimaria : String -> String
		Recibe la clave maestra y extrae la primaria
		extraer_ClavePrimaria("47582") = "452"
	'''
	tamano = len(ClaveMaestra)
	clave = ""
	for i in range(0,tamano):
		if(i % 2 == 0):
			clave = clave + ClaveMaestra[i]
	return clave
			

def extraer_ClaveSecundaria(ClaveMaestra):
	''' extraer_ClaveSecundaira : String -> String
		Recibe la clave maestra y extrae la secundaria
		extraer_ClaveSecundaria("47582") = "78"
	'''
	tamano = len(ClaveMaestra)
	clave = ""
	for i in range(0,tamano):
		if(i % 2 != 0):
			clave = clave + ClaveMaestra[i]
	return clave 
	
def test_extraer_ClavePrimaria():
	assert(extraer_ClavePrimaria("47582")) == "452"
	assert(extraer_ClavePrimaria("47")) == "4"
	assert(extraer_ClavePrimaria("")) == ""
	
def test_extraer_ClaveSecundaria():
	assert(extraer_ClaveSecundaria("47582")) == "78"
	assert(extraer_ClaveSecundaria("47")) == "7"
	assert(extraer_ClaveSecundaria("")) == ""
			
			
			
			
			
			
			
			
			
