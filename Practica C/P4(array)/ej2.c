#include <stdio.h>

#define MAX 100

int main(){
    int n[MAX];
    int i, k;
    int cont = 0;

    for(i = 100; i<200; i++){
        if(i%2 == 0){
            n[cont] = i;
            cont++;
        }
    }

    for(k = 50; k > 0;k--){
        printf("%d\n",n[k]);
    }

    return 0;
}