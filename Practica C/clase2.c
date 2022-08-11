#include <stdio.h>

int main(void){
  int cantidad=0;
  printf("Ingrese la cantidad de productos vendidos: ");
  scanf("%d", &cantidad);

  if(cantidad >= 35){
    if(cantidad < 50){
    printf("\nVenta promedio\n");
    }else{
    printf("\nHoy ha sido un gran dia\n");
    }
  }else{
  printf("\nA seguir vendiendo\n");
  }
return  0;
}
