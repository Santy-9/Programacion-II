#include <stdio.h>
#include <string.h>
#include <math.h>


float farenheit_To_celsius (float temp);

float kelvin_To_celsius (float temp);


int main (void){
	float grados,FtoC, KtoC, promTotal;
	int cantC = 0, cantF = 0, cantK = 0;
	float promC = 0, promF = 0, promK = 0;
	char temp;
	
	printf("Ingrese tipo temperatura(C, K, F) y grados: (N para salir)\n");
	scanf("%s %f",&temp, &grados);
	
	while(temp != 'N'){
		
		switch(temp){
			case 'C':
				cantC += 1;
				promC += grados;
				//printf("%f",promC);
				break;
			case 'F':
				cantF += 1;
				promF += grados;
				//printf("%f",promF);
				break;
			case 'K':
				cantK += 1;
				promK += grados;
				//printf("%f",promK);
				break;
		}
		
		printf("Ingrese tipo temperatura(C, K, F) y grados: (N para salir)\n");
		scanf("%s %f",&temp, &grados);
			
	}
	//if para prevenir division por 0.
	if(cantC == 0){
		promC = 0;
	}else{
		promC = promC / cantC;
	}
	if(cantF == 0){
		promF = 0;
	}else{
		promF = promF / cantF;
	}
	if(cantK == 0){
		promK = 0;
	}else{
		promK = promK / cantK;
	}
	
	FtoC = farenheit_To_celsius(promF);
	KtoC = kelvin_To_celsius(promK);
	promTotal = (promC + FtoC + KtoC) / 3;
	
	printf("\nCantidad de Celcius registradas: %d \n",cantC);
	printf("Cantidad de Farenheit registradas: %d \n",cantF);
	printf("Cantidad de Kelvin registradas: %d \n",cantK);
	printf("Promedio de C: %f \nPromedio de F: %f \nPromedio de K: %f\n",promC, promF, promK);
	printf("Promedio total sobre Celcius: %f\n",promTotal);
	
	
	return 0;
}	



float farenheit_To_celsius (float temp){
	
	return ((temp -32.0)*(5.0/9.0));
}

float kelvin_To_celsius (float temp){
	
	return (temp - 273.15);
}
