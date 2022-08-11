#include<stdio.h>

int serie_fibonacci(int);
int serie_fibonacci_iterativo(int);

int main(){
   int terminos;
   printf("Ingrese el nro. de términos:");
   scanf("%d",&terminos);
 
   printf("\nNúmeros de Fibonacci:\n");
   int cantidad = 0, i;
   for ( i = 1 ; i <= terminos ; i++ ){
      printf("%d\n", serie_fibonacci_iterativo(cantidad));
      cantidad++; 
   }
   return 0;
}

// serie_fibonacci: Int -> Int
int serie_fibonacci(int num){
   if ( num == 0 )
     return 0;
   else if ( num == 1 )
     return 1;
   else
     return ( serie_fibonacci(num-1) + serie_fibonacci(num-2) );
}

int serie_fibonacci_iterativo(int num){
   int inicial = 0;
   int inicial2 = 1;
   int generado = 0;

   inicial = inicial2;
   inicial2 = generado;
   generado = inicial + inicial2;
   return generado;
}


// Tarea 1: Cómo lo transformamos en iterativo?
// Tarea 2: Como completamos la receta?