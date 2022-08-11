#include <stdio.h>
#include <stdlib.h>


#define MAX 5 // dimensión máxima para el arreglo.

//Probamos distintas formas de inicializar un arreglo.

int main(){
  
  int arreglo1[MAX];
  int arreglo2[MAX]={0}; // inicializamos todos los valores a 0.
  int arreglo3[5]={1,-1,4,5,100}; //inicializamos con valores especificos.
  int arreglo6[MAX];

  float arreglo4[MAX]={1.0,2.5,3.3};

  // crea un  arreglo con dimensión 5, y lo inicializa con los valores dados. 
  double arreglo5[]={1.0,2.5,3.3,8.7,0.0,1.1,6.7,2.7}; 


  //inicializamos valor a valor utilizando un ciclo.
  int i;
  for (i=0; i<MAX; i++){
    arreglo1[i] = 5;
  }
  
  
  // imprimimos los resultados:
  printf("\n Los valores del arreglo 1 inicializados por el for son:");
  printf ("\n---------------------------------------------------------");
   for (i=0; i<MAX; i++){
    printf("\n El elemento %d es %d ", i, arreglo1[i]);
  }
  
  printf("\n");
  
  printf("\n Los valores del arreglo 2 inicializados por único valor en la declaración son:");
  printf ("\n---------------------------------------------------------");
   for (i=0; i<MAX; i++){
    printf("\n El elemento %d es %d ", i, arreglo2[i]);
  }
  
  printf("\n");
    
  printf("\n Los valores del arreglo 3 inicializados con valores específicos");
  printf ("\n---------------------------------------------------------");
   for (i=0; i<MAX; i++){
    printf("\n El elemento %d es %d ", i, arreglo3[i]);
  }
  
  printf("\n");
  
  printf("\n Los valores del arreglo 4 sólo inicializa las posiciones dadas.");
  printf ("\n---------------------------------------------------------");
   for (i=0; i<MAX; i++){
    printf("\n El elemento %d es %.1f ", i, arreglo4[i]);
  }
  
  printf("\n");
  
  printf("\n Los valores del arreglo 5 creado e inicilizado con sus valores.");
  printf ("\n---------------------------------------------------------");
   for (i=0; i<8; i++){
    printf("\n El elemento %d es %lf ", i, arreglo5[i]);
  }
  
  printf("\n");
  
  arreglo6[1] = 2;
  for (i=0; i<MAX; i++){
    printf("\n El elemento %d es %d ", i, arreglo6[i]);
  }  
 return 0; 

}