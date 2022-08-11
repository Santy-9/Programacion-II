#include <stdio.h>
#include <stdlib.h>

#define TOPERAND 20 // Tope de aleatoriedad.
#define MAX 5  // Dimension arreglo.


// Prototipo de las Funciones
void simulaCargarDatos (int aDatos []);
void cargarDatos (int aDatos []);
void imprimeDatos (int aDatos[MAX]);
float calculoPromedio (int aDatos[MAX]);

//Función main.
int main (void){
  
  int intArray[MAX]={0};// inicialización del arreglo.
  float prom=0;
  
  cargarDatos(intArray);
  
  printf("\n El Arreglo Ingresado es: \n");
  
  imprimeDatos(intArray);
  prom= calculoPromedio(intArray);
  
  printf("\n El promedio del arreglo es: %2.f", prom);
  printf("\n");
  
  simulaCargarDatos(intArray);
  
  printf("\n El Arreglo Generado es : \n");
  
  imprimeDatos(intArray);
  prom = calculoPromedio(intArray);
  
  printf("\n El promedio del arreglo es: %2.f", prom);
  printf("\n");

  return 0;
  
}

//-----------------------------------------------------------------------------------------
// Definición de las Funciones
//-----------------------------------------------------------------------------------------

//-----------------------------------------------------------------------------------------
//Diseño de Datos: 
// aDatos es un arreglo de enteros utilizados para representar una lista de números enteros
// el entero que retorna la función representa si la operación fue exitosa o no.
//Signatura:
// simulaCargarDatos: [Int] -> Void;
//Propósito:
// La función toma los datos de la entrada estandar y los almacena en el arreglo pasado como argumento.
// Entrada: Arreglo de enteros, un entero.
// Salida: Void

void cargarDatos (int aDatos []){
     int i;
     for (i=0; i<MAX; i++){
        printf("\n Ingrese el elemento %d - :", i);
        scanf ("%d", &aDatos[i]);
     }
}
//==========================================================================================

//-----------------------------------------------------------------------------------------
//Diseño de Datos: 
// aDatos es un arreglo de enteros utilizados para representar una lista de numeros enteros.
//Signatura:
// simulaCargarDatos: [Int] -> Void;
//Propósito:
// La función carga con datos aleatorios el arreglo pasado como argumento. Los datos aleatorios tienen son menores que los especificados en TOPERAND.
// Entrada: Arreglo de enteros (por referencia)
// Salida: Void

void simulaCargarDatos (int aDatos []){
    int i;
     for (i=0; i<MAX; i++){
        aDatos[i]=(rand()%TOPERAND);
     }
}
//==========================================================================================

//-----------------------------------------------------------------------------------------
//Diseño de Datos: 
// aDatos es un arreglo de enteros utilizados para representar una lista de numeros enteros
//Signatura:
// imprimeDatos: [Int] -> Void;
//Propósito:
// La función recibe un arreglo de enteros con su dimensión e imprime en patalla el contenido del mismo.
// Entrada: Arreglo de enteros (por valor)
// Salida: Void. 

void  imprimeDatos (int aDatos [MAX]){
     int i;
     for (i=0; i<MAX; i++){
        printf("\n El elemento %d - es:  %d", i, aDatos[i]);
     }
}
//==========================================================================================

//-----------------------------------------------------------------------------------------
//Diseño de Datos: 
// aDatos es un arreglo de enteros utilizados para representar una lista de numeros enteros
//Signatura:
// calculaPromedio: [Int] -> Float;
//Propósito:
// La función recibe un arreglo de enteros con su dimensión y retorna el promedio del mismo.
// Entrada: Arreglo de enteros (por valor).
// Salida: Float.

float calculoPromedio (int aDatos [MAX]){
     int i;
     int suma=0;
     for (i=0; i<MAX; i++){
        suma += aDatos[i];
     }
     
     return !MAX ?: (float)suma/MAX ;
}
//==========================================================================================