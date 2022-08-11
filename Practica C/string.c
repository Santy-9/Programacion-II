#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>



int main(void){ 
	
  char palabra[7]="banana";   
  char dato[]="7215";
  int longitud=0; 
  
  printf ("\nLa cadena %s tiene longitud %d\n",palabra,(int)strlen(palabra));
  longitud=strlen(dato);
  printf("\nEl dato %s tiene %d longitud\n\n",dato,longitud); 
  
  return 0;
}


