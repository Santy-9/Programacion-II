#include <stdio.h>
#include <math.h>
#include <string.h>

#define secreto 369

int f();
int f2();
float f3();
float f4();
int f5();
void f6();

void main(){
    //f();
    //f2();
    //printf("%lf", f4());
    f6();
}

int f(){
    int n;

    printf("Ingrese numero de dado :\n");
    scanf("%d", &n);
    switch(n){
        case 1:
            printf("Seis");
            break;
        case 2:
            printf("Cinco");
            break;
        case 3:
            printf("Cuatro");
            break;
        case 4:
            printf("Tres");
            break;
        case 5:
            printf("Dos");
            break;
        case 6:
            printf("Uno");
            break;
        default:
            printf("Numero incorrecto");
            break; 
    }
    return 0;
}

int f2(){
    int n;

    printf("1.Azul\n2.Roja\n3.Verde\n4.Rosa\n5.Gris");
    printf("\n Ingrese numero de habitacion: \n");
    scanf("%d", &n);

    switch(n){
        case 1:
            printf("Primera Planta\n2 Camas");
            break;
        case 2:
            printf("Primera Planta\n1 Camas");
            break;
        case 3:
            printf("Segunda Planta\n3 Camas");
            break;
        case 4:
            printf("Segunda Planta\n2 Camas");
            break;
        case 5:
            printf("Tercera Planta\n1 Camas");
            break;
        default:
            printf("Número no asociado a habitación.");
    }
    return 0;
}

float f3(){
    float n = 0;
    float i;

    for (i = 1; i <= 100; i++){
        n += 1/i;
        //printf("%f\n",n);
    }
    return n;
}

float f4(){
    float n = 0;
    float i;

    for (i = 1; i <= 30; i++){
        n += 1/pow(i,2);
    }
    return n;
}

int f5(){
    int i, n;

    for (i = 0 ; i < 15 ; i++){
        printf("Ingrese numero: \n");
        scanf("%d",&n);
        if(n == secreto){
            printf("Correcto\n");
            i = 15;
        }else if(n < secreto){
            printf("el numero secreto es mayor\n");
        }else{
            printf("el numero secreto es menor\n");
        }
        }
    printf("Sin intentos");
    return 0;
}
    
void f6(){
    int i;
    int n = 5;
    char a ;
    char palabra[25] = "bucle";
    char pal[25];

    for(i = 1 ; i < 6; i++){
        //printf("%is %d", palabra, &n-1);
        printf("%d\n", n);
        n -= 1;
    }

}

