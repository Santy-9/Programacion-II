/*
 Santiago Funes
 Legajo: F-3672/2
 DNI: 41489259
 */

#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>

void imprime_no_usados(int camiones[10]);

void cuantos_manejo(int camiones[10], int n, int arr[4]);

void km_total(int choferes[15], int n, int km);

void cobro(int choferes[15], int pago, int pagos[15]);

int main(){
	
	int choferes[15] = {6523, 0, 2533, 1500, 548, 0, 0, 1855, 0, 0, 7855, 12584, 0, 5241, 522};
	int camiones[10] = {1, 2, 1, 10, 1, 5, 0, 0, 2, 1};
	int arr[4] = {0}; //coches que manejo un chofer
	int pagos[15] = {0}; 
	int i, km, k, pago;
	int cont = 0;
	int n; //numero de chofer
	
	//Ejercicio 2
	imprime_no_usados(camiones);
	
	
	//carga de datos
	
	printf("Ingrese numero de chofer: ");
	scanf("%d", &n);
	
	printf("Ingrese cantidad de kilometros del chofer: ");
	scanf("%d", &km);
	
	printf("Ingrese pago por kilometro recorrido: ");
	scanf("%d", &pago);
	
	//Ejercicio 3
	
	cuantos_manejo(camiones, n, arr);
	
	printf("El chofer %d manejo: \n",n);
	
	//cuenta cuantos camiones manejo
	for(k = 0; k < 10; k++){
		if(camiones[k] == n){
			cont++;
		}
	}
	
	for(i = 0; i < cont; i++){
		
		printf("Camion %d\n",arr[i]);
	}
	
	
	//Ejercicio 4
	
	km_total(choferes, n, km);
	
	printf("Kilometros totales del chofer %d: %d",n, choferes[n-1]);
	
	
	//Ejercicio 5
	
	cobro(choferes, pago, pagos);
	
	printf("\nEl chofer %d recibe un pago de %d",n ,pagos[n-1]);
	
	return 0;
}




/*
 imprime_no_usados: [int] -> Void
 Recibe un arreglo de camiones e imprime en pantalla los camiones que  no se usaron. 
 */
void imprime_no_usados(int camiones[10]){
	int i;
	
	for(i = 0; i < 10; i++){
		if(camiones[i] == 0){
			
			printf("El camion %d no se uso\n", i+1);
		}
	}
}


/*
 cuantos_manejo: [int] int [int] -> Void
 Recibe un arreglo de camiones, el numero de chofer, un arreglo vacio y devuelve todos los coches que manejo dicho chofer.
 cuantos_manejo({1, 2, 1, 10, 1, 5, 0, 0, 2, 1}, 1, {0, 0, 0, 0}) == {1, 3, 5, 10} 
 cuantos_manejo({1, 2, 1, 10, 1, 5, 0, 0, 2, 1}, 10, {0, 0, 0, 0}) == {1, 0, 0, 0}
 cuantos_manejo({1, 2, 1, 10, 1, 5, 0, 0, 2, 1}, 14, {0, 0, 0, 0}) == {0, 0, 0, 0}  
 */
void cuantos_manejo(int camiones[10], int n, int arr[4]){
	int i;
	int cont = 0;
	
	for(i = 0; i < 10; i++){
		if(camiones[i] == n){
			
			arr[cont] = i+1;
			cont++;
		}
	}
	
}

/*
 km_total: [int] int int -> Void
 Recibe un arreglo de choferes, el numero de chofer y los kilometros que recorridos, y actualiza el arreglo choferes con los kilometros totales.
 km_total({6523, 0, 2533, 1500, 548, 0, 0, 1855, 0, 0, 7855, 12584, 0, 5241, 522}, 1, 1000) == {7523, 0, 2533, 1500, 548, 0, 0, 1855, 0, 0, 7855, 12584, 0, 5241, 522}
 km_total({6523, 0, 2533, 1500, 548, 0, 0, 1855, 0, 0, 7855, 12584, 0, 5241, 522}, 6, 500) == {6523, 0, 2533, 1500, 548, 500, 0, 1855, 0, 0, 7855, 12584, 0, 5241, 522}
 km_total({6523, 0, 2533, 1500, 548, 0, 0, 1855, 0, 0, 7855, 12584, 0, 5241, 522}, 15, 489) == {6523, 0, 2533, 1500, 548, 0, 0, 1855, 0, 0, 7855, 12584, 0, 5241, 1011}
 */
void km_total(int choferes[15], int n, int km){
	
	choferes[n - 1] = choferes[n - 1] + km;
	
}


/*
 cobro: [int] int [int] -> Void
 Recibe un arreglo de choferes, el pago por kilometro y una arreglo de pagos vacio, y actualiza el arreglo de pagos con los cobros de cada chofer.
cobro({6523, 0, 2533, 1500, 548, 0, 0, 1855, 0, 0, 7855, 12584, 0, 5241, 522}, 10, {65230, 0, 25330, 15000, 5480, 0, 0, 18550, 0, 0, 78550, 125840, 0, 52410, 5220}
 */
void cobro(int choferes[15], int pago, int pagos[15]){
	int i;
	
	for(i = 0; i < 15; i++){
		
		pagos[i] = choferes[i] * pago;
		
	}
}


