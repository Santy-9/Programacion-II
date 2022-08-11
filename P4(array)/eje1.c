#include <stdio.h>

#define MAX 100

int main(){
    int n[MAX];
    int i;

    for(i = 0; i<100; i++){
        n[i] = i;
        printf("%d\n", n[i]);
    }
    return 0;
}