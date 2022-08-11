#include <stdio.h>
#include <assert.h>

int maximo(int n, int n1);
void test_maximo(void);

int ladosTriangulo(int l1, int l2, int l3);

void main(){
    int n1, n2, n3, n4;
    int max;

    /*
    printf("Ingrese 4 enteros: ");
    scanf("%d %d %d %d",&n1, &n2, &n3, &n4);

    int max1 = (maximo(n1, n2));
    int max2 = (maximo(n1, n2));
    if(max1 > max2){
        max = max1;
    }else{
        max = max2;
    }
    printf("el maximo es: %d", max);
    */
    //printf("%d", ladosTriangulo(1,3,6));
    //test_maximo();

}
/*
maximo: Int Int -> Int
Calcula el maximo entre dos numeros.
maximo(4, 6) = 6
maximo(10, 2) = 10
*/
int maximo(int n, int n1){
    int max;
    if (n > n1){
        max = n;
    }else{
        max = n1;
    }
    return max;
}

/*
test_maximo: Void -> Void
test de la funcion maximo.
*/
void test_maximo(void){
    assert(maximo(4, 6) == 6);
    assert(maximo(7, 4) == 7);
}

int ladosTriangulo(int l1, int l2, int l3){
    int max, min, min2, resp;
    if (l1 > l2){
        max = l1;
        min = l2;
    }else{
        max = l2;
        min = l1;
    }
    if (l3 > max){
        max = l3;
        min2 = max;
    }else{
        min2 = l3;
    }
    if(max < min + min2){
        resp = 1;
    }else{
        resp = 0;
    }
    return resp;
}

