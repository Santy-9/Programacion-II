#include <stdio.h>

int  main()  
{  
    int arreglo[10]; 
    int i;  
    printf("\n\n Lee e Imprime los Elementos de un Arreglo:\n");
    printf("-----------------------------------------\n");	
  
    printf("Ingrese los 10 elementos del arreglo :\n");  
    for(i=0; i<10; i++)  
    {  
	    printf("elemento - %d : ",i);
        scanf("%d", &arreglo[i]);  
    }  
  
    printf("\n Los elements del arreglo son : ");  
    for(i=0; i<10; i++)  
    {  
        printf("%d  ", arreglo[i]);  
    } 
    printf("\n");	
   
   return 0;
}

