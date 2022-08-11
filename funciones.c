#include <stdio.h>

int fact(int);
int calculo(void);

int  main(void){
   int suma = 0,i = 0;
   int cont = 6;
    
   //Debugging 
   printf ("DEBUG- El Factorial de  %d es %d", 1, fact(1));
   printf ("DEBUG- El Factorial de  %d es %d", 2, fact(2));
   printf ("DEBUG- El Factorial de  %d es %d", 3, fact(3));
   printf ("DEBUG- El Factorial de  %d es %d", 5, fact(5));
   //Fin Debugging
    
   //suma=fact(1)/1+fact(2)/2+fact(3)/3+fact(4)/4+fact(5)/5;
  
  /*
   for (i=1; i < cont; i++) {
      suma = suma + fact(i)/i;
   }
  */
	printf("\n\n Función : Encuentra la suma de  1!/1+2!/2+3!/3+4!/4+5!/5 :\n");
	printf("----------------------------------------------------------\n");    
  printf(" La suma de la serie es : %d\n\n",calculo());
    
return 0;
}

int calculo(void){
  int suma = 0,i = 0;
  int cont = 6;
  
  for (i=1; i < cont; i++) {
      suma = suma + fact(i)/i;
   }
return suma;
}


int fact(int n)
    {
        int num=1,factorial=1;
        
        while(num <= n)
        {
            factorial *= num;
            num++;
        }
    return factorial;
    }

