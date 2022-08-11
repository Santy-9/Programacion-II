#include <stdio.h>

int main(void){
  int cantidad=0;
  printf("Ingrese la cantidad de productos vendidos: ");
  scanf("%d", &cantidad);

  if(cantidad < 35){
    printf("\nA seguir vendiendo\n");
  }else if(cantidad >= 35 && cantidad < 50){
    printf("\nVenta promedio\n");    
  }else{
    printf("\nHoy ha sido un gran dia\n");
  }
  return 0;
} 