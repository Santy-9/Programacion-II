#include <stdio.h>
#include <assert.h>

typedef struct {
    int H;
    int M;
    int S;
}Tiempo;

//typedef struct tiempo Tiempo;
Tiempo Crea_Tiempo(int h, int m, int s);

void imprimir_Tiempo(Tiempo tiempo);

Tiempo suma_Tiempo(Tiempo tiempo, Tiempo tiempo2);

Tiempo resta_Tiempo(Tiempo tiempo, Tiempo tiempo2);

int main(){
    Tiempo tiempo;
    Tiempo tiempo2;
    int h, m, s;
    int h1, m1, s1;

    printf("Ingrese hora, minutos y segundos: ");
    scanf("%d %d %d",&h, &m, &s);
    //printf("%d %d %d", h, m, s);
    printf("Ingrese hora, minutos y segundos: ");
    scanf("%d %d %d",&h1, &m1, &s1);

    tiempo = Crea_Tiempo(h, m, s);
    tiempo2 = Crea_Tiempo(h1, m1, s1);
    //printf("%d %d %d", tiempo.H, tiempo.M, tiempo.S);
    tiempo = resta_Tiempo(tiempo, tiempo2);

    imprimir_Tiempo(tiempo);



}

/*
Crea_Tiempo: Int Int Int -> Tiempo
Recibe tres datos, hora, minutos y segundos y crea una estructura tipo Tiempo.
Crea_Tiempo(12,23,56) = Tiempo{12, 23, 56}
*/
Tiempo Crea_Tiempo(int h, int m, int s){
    Tiempo tiempo = {h, m, s};
    return tiempo;
}


/*
imprimir_Tiempo: Tiempo -> void
Recibe un dato de tipo Tiempo e imprime con el formato hh:mm:ss
*/
void imprimir_Tiempo(Tiempo tiempo){

    printf("%d:%d:%d",tiempo.H, tiempo.M, tiempo.S);

}

/*
suma_Tiempo: Tiempo Tiempo -> Tiempo
Recibe un dos datos de tipo Tiempo y suma ambos.
*/
Tiempo suma_Tiempo(Tiempo tiempo, Tiempo tiempo2){

    tiempo.H = tiempo.H + tiempo2.H;
    tiempo.M = tiempo.M + tiempo2.M;
    tiempo.S = tiempo.S + tiempo2.S;

    return tiempo;
}

/*
suma_Tiempo: Tiempo Tiempo -> Tiempo
Recibe un dos datos de tipo Tiempo y resta ambos.
*/
Tiempo resta_Tiempo(Tiempo tiempo, Tiempo tiempo2){

    tiempo.H = tiempo.H - tiempo2.H;
    tiempo.M = tiempo.M - tiempo2.M;
    tiempo.S = tiempo.S - tiempo2.S;

    return tiempo;
}

/*
int Tiempo_dias(Tiempo tiempo){
    int dias, año, min;

    if (tiempo.H >= 8760){
        min = tiempo.H - 8760;
        año = 1;
    }
}
*/