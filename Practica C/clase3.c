#include <stdio.h>

int main(void){
  int numero = 0;
  printf("\nIntroduce numero: ");
  scanf("%d", &numero);
  switch(numero){
    case 1: 
      printf("Es 1\n");
    case 2:
      printf("Es 2\n");
      break;
    case 3:
      printf("Es 3\n");
      break;
    default:
      printf("No es 1 ni 2 ni 3\n");
      break;   
  }
return 0;
}

  