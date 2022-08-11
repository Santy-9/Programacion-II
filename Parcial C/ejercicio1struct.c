/*
 Santiago Funes
 Legajo: F-3672/2
 DNI: 41489259
 */


#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>

#define MAX 50



typedef struct{
	char nombre[MAX];
	int altura;
	char categoria[MAX];
	char tipo[MAX];
	int ultima_erupcion;
	char ubicacion[MAX];
	int ranking;
	}Volcan;
	
Volcan crearVolcan(char nombre[MAX], int altura, char categoria[MAX], char tipo[MAX], int ultima_erupcion, char ubicacion[MAX], int ranking);

Volcan activar_volcan(Volcan volcan);

int es_peligroso_volcan(Volcan volcan);	
	
int main(){
	
	Volcan volcan;
	char nombre[MAX];
	char categoria[MAX];
	char tipo[MAX];
	char ubicacion[MAX];
	int altura, ultima_erupcion, ranking;
	int Bool;
	
	//Ejercicio 2
	
	
	printf("Ingrese nombre del volcan: ");
	fgets(nombre, sizeof(nombre), stdin);
	
	printf("\nIngrese altura del volcan: ");
	scanf("%d", &altura);
	
	//while(getchar()!= '\n');
	
	printf("\nIngrese categoria del volcan: ");
	fgets(categoria, sizeof(categoria), stdin);
	
	while(getchar()!= '\n');
	
	printf("\nIngrese tipo de volcan: ");
	fgets(tipo, sizeof(tipo), stdin);
	
	printf("\nIngrese la ultima erupcion: ");
	scanf("%d", &ultima_erupcion);
	
	while(getchar()!= '\n');
	
	printf("\nIngrese la ubicacion: ");
	fgets(ubicacion, sizeof(ubicacion), stdin);
	
	printf("\nIngrese ranking: ");
	scanf("%d", &ranking);
	
	
	volcan = crearVolcan(nombre, altura, categoria, tipo, ultima_erupcion, ubicacion, ranking);
	
	
	//printf("\nNombre: %s\n Altura: %d\n Categoria: %s\n Tipo: %s\n Ultima erupcion: %d\n Ubicacion: %s\n Ranking: %d\n",
	//		volcan.nombre, volcan.altura, volcan.categoria, volcan.tipo, volcan.ultima_erupcion, volcan.ubicacion, volcan.ranking);
	
	//Ejercicio 3
	Volcan volcan1 = {"San jose", 6070, "estratovolcan", "activo", 1960, "Mendoza", 7};
	Volcan volcan2 = {"Maipo", 5323, "estratovolcan", "activo", 1912, "Mendoza", 6};
	Volcan volcan3 = {"Peteroa", 3977, "estratovolcan", "activo", 2019, "Mendoza", 2};
	Volcan volcan4 = {"Maule", 3092, "estratovolcan", "inactivo", -1, "Neuquen", 3};
	Volcan volcan5 = {"Tromen", 4114, "estratovolcan", "inactivo", 1828, "Neuquen", 7};
	
	//Ejercicio 4
	volcan4 = activar_volcan(volcan4);
	
	printf("\nNombre: %s\n Altura: %d\n Categoria: %s\n Tipo: %s\n Ultima erupcion: %d\n Ubicacion: %s\n Ranking: %d\n",
			volcan4.nombre, volcan4.altura, volcan4.categoria, volcan4.tipo, volcan4.ultima_erupcion, volcan4.ubicacion, volcan4.ranking);
	
	//Ejercicio 5
	
	Bool = es_peligroso_volcan(volcan5);
	
	
	if(Bool){
		printf("\n%s Es peligroso", volcan5.nombre);
	
	}else{
		printf("\n%s No es peligroso", volcan5.nombre);
	}
	
	
	
}

/*
 crearVolcan: char int char char int char int -> Volcan
 Recibe 5 datos relacionados al volcan y crea una estructura tipo Volcan.
 crearVolcan("San jose", 6070, "estratovolcan", "activo", 1960, "Mendoza", 7) -> volcan = {"San jose", 6070, "estratovolcan", "activo", 1960, "Mendoza", 7}
 */
Volcan crearVolcan(char nombre[MAX], int altura, char categoria[MAX], char tipo[MAX], int ultima_erupcion, char ubicacion[MAX], int ranking){
	
	Volcan volcan;
	
	strcpy(volcan.nombre, nombre);
	volcan.altura = altura;
	strcpy(volcan.categoria, categoria);
	strcpy(volcan.tipo, tipo);
	volcan.ultima_erupcion = ultima_erupcion;
	strcpy(volcan.ubicacion, ubicacion);
	volcan.ranking = ranking;
	
	return volcan;
	
	}

/*
 activar_volcan: Volcan -> Volcan
 Recibe un dato tipo volcan y devuele otro dato de tipo Volcan actualizado con el tipo, ultima erupcion y ranking.
 */
Volcan activar_volcan(Volcan volcan){
	
	strcpy(volcan.tipo, "activo");
	
	volcan.ultima_erupcion = 2022;
	
	volcan.ranking = 1;
	
	return volcan;
	}


/*
 es_peligroso_volcan: Volcan -> int
 Recibe un dato de tipo Volcan y devuelve 0 si es:
	-Extinto
	-Inactivo y la ultima erupcion fue anterior a 1850
	-Inactivo y el ranking es mayor o igual a 7
*/
int es_peligroso_volcan(Volcan volcan){
	int Boolean;
	char Extinto[8] = "extinto";
	char Inactivo[9] = "inactivo";
	
	
	if( strcmp(volcan.tipo, Extinto) == 0 || 
		(strcmp(volcan.tipo, Inactivo) == 0 && volcan.ultima_erupcion < 1850) ||
		(strcmp(volcan.tipo, Inactivo) == 0 && volcan.ranking >= 7)){
			
		Boolean = 0;
		
	}else{
		
		Boolean = 1;
	}
		
	return Boolean;
	
}

	
	
	
	
	
	
