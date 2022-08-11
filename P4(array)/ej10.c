#include <stdio.h>

#define N 1000
#define TRUE 1
#define FALSE 0

int main(){
    int i, j, a[N+1];

    for(a[1] = 0 , i=2; i<=N; i++) {
        a[i] = 1;
    }

    for(i=2; i<= N/2; i++){     
        for(j=2; j<= N/i; j++){
            a[i*j] = 0;             //i=2 2*2, 2*3, 2*4, ..., 2*500 |i=3 3*2, 3*3, 3*4,...,3*333 | i=4 4*2, 4*3, 4*4, ..., 4*250  | ... |i=500 500*2
        }
    }

    for(i=1; i <= N; i++){
        if(a[i] == TRUE){
            printf("%d-", i);
        }
    }
    printf("\n");
    return 0;
}
