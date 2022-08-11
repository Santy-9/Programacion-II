#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>

#define MAX 25

void my_strcpy(char destino[MAX], char origen[MAX]);
void test_my_strcpy(void);

int main(void){
	 
  char cadena[MAX];
  char palabra[MAX]="banana";
  
  my_strcpy(cadena,palabra);
  printf("\nCadena almacena %s\n\n",cadena);

  test_my_strcpy();

  
  return 0;
}



/*
my_strcpy: String String -> Int

my_strcpy(" ", "hola") -> destino = "origen"

*/
void my_strcpy(char destino[MAX], char origen[MAX]){
   int i;

   for (i = 0; origen[i]!= '\0';i++){
      destino[i] = origen[i];
   }
   destino[i] = '\0';

   //printf("\n DEB -- La cadena que se copió es: \t %s", destino);
   
}


void test_my_strcpy(void){
   char prueba[MAX];
   char prueba2[MAX] ="hola";

   my_strcpy(prueba,prueba2);
   assert(!strcmp(prueba,"hola"));
   printf("\nListo!");

   my_strcpy(prueba," ");
   assert(!strcmp(prueba," "));
   printf("\nListo!");

   my_strcpy(prueba,"1234f");
   assert(!strcmp(prueba,"1234f"));
   printf("\nListo!");


}





