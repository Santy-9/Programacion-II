#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

void aleatorio(int arr[], int n);

int main(){
    int n = 0;
    int i, x;

    printf("Ingrese longitud del array: ");
    scanf("%d",&n);

    int arr[n];

    aleatorio(arr, n);

    printf("Ingrese 1 para ver en orden directo o cualquier otro numero para orden inverso: ");
    scanf("%d", &x);

    if(x == 1){
        for(i = 0; i < n; i++){
        printf("%d\n", arr[i]);
    }
    }else{
        for(i = n-1; i >= 0; i--){
        printf("%d\n", arr[i]);
    }
    }
    
    return 0;
}


/*
aleatorio: [Int] Int -> Void
Recibe un array, un entero n y completa dicho array con numeros aleatorios con una longitud n.
*/
void aleatorio(int arr[], int n){
    int i;

    for(i = 0; i<n ; i++){
        arr[i] = rand();
    }

}
