#include <stdio.h>

int main(){
    int nota ;

    //scanf("%d", &nota);

    if(nota >= 2 && nota <= 10){
        if(nota >= 6 && nota <= 10){
            if(nota >= 7 && nota <= 10){
                if(nota >= 8 && nota <= 10){
                    if(nota >= 9 && nota <= 10){
                        if(nota == 9){
                            printf("distinguido");
                        }else{
                            printf("sobresaliente");
                        }
                    }else{
                        printf("muy bueno");
                    }
                }else{
                    printf("bueno");
                }
            }else{
                printf("aprobado");
            }
        }else{
            printf("insuficiente");
        }
    }else{
        printf("incorrecto");
    }
    return 0;
}