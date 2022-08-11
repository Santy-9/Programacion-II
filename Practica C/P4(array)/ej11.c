#include <stdio.h>

void Copia(int arr1[], int arr2[], int arr3[], int n);
void Duplica(int arr1[], int arr2[], int arr3[], int n);
int Muestra(int arr3[], int n);

int main(){
    int n, i, ctr;

    printf("\n Ingrese el nro de elementos a almacenar en el arreglo: ");
    scanf("%d", &n);

    int arr1[n], arr2[n], arr3[n];

    printf("\n Ingrese los %d elementos en el arreglo: ", n);
    for(i=0; i < n; i++){
        printf("\nElemento - %d: ", i);
        scanf("%d", &arr1[i]);
    }

    Copia(arr1, arr2, arr3, n);

    Duplica(arr1, arr2, arr3, n);

    ctr = Muestra(arr3, n);

    printf("\nLa cantidad de duplicados en el arreglo es: %d", ctr);
    
    return 0;

}

void Copia(int arr1[], int arr2[], int arr3[], int n){
    int i;

    for(i = 0; i < n; i++){
        arr2[i] = arr1[i];
        arr3[i] = 0;
    }
}

void Duplica(int arr1[], int arr2[], int arr3[], int n){
    int i, j, mm = 1;

    for(i=0; i<n ; i++){                                //arr1 = {1, 1, 3, 4, 5}
        for(j=0; j<n; j++){                             //arr2 = {1, 2, 3, 4, 5}
            if(arr1[i] == arr2[j]){                     //arr3 = {3, 0, 0, 0, 0} mm = 4
                arr3[j] = mm;
                mm++;
            }
        }
        mm = 1;
    }
}

int Muestra(int arr3[], int n){
    int i, ctr = 0;

    for(i = 0; i < n; i++){
        if(arr3[i] == 2){
            ctr++;
        }
    }

    return ctr;

    //printf("\nLa cantidad de duplicados en el arreglo es: %d", ctr);
    //printf("\n");
}