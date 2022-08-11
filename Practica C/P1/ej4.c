#include <stdio.h>

int main(){
    int temp = 1;

    if(temp < 0){
        printf("Solido");
    }else if(temp >= 0 && temp <= 100 ){
        printf("Liquido");
    }else{
        printf("Gas");
    }
    return 0;

}
