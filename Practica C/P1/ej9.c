#include <stdio.h>
void E9();
void E10();
int E12(int num);

int main(){
    
    //printf("%d",E12(11));



    return 0;
}



void E9(){
    int i;
    while(i < 101){
        printf("%d\n",i);
        i++;
    }
}

void E10(){
    int i;
    while(i < 101){
        if(!(i % 2 == 0)){
            printf("%d\n",i);
            i++;
        }
        i++;    
    }
}

int E12(int num){
    int flag = 1, n = 2;

    while(flag == 1 && n <= num-1){
        if(num % n == 0){
            flag = 0;
        }
        n += 1;
    }
    return flag;
}

