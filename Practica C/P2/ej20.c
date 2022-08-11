#include <stdio.h>
#include <string.h>
#include <assert.h>

#define MAX 256

int revez(char palabra[MAX]);
int es_capicua(char frase[MAX]);

int main(){
    char n[MAX] = "anilina";

    //revez(n);
    //printf("%s", n);
    printf("%d",es_capicua(n));
    
}

int revez(char palabra[MAX]){
    char nueva[MAX];
    char ch;
    int i, longitud;

    longitud = strlen(palabra);
    
    for (i = 0; palabra[i] != '\0'; i++){
        longitud--;
        ch = palabra[longitud];
        nueva[i] = ch;
    }
    nueva[i] = '\0';
    strcpy(palabra, nueva);
    return 0;
}

int es_capicua(char frase[MAX]){
    char original[MAX];

    strcpy(original, frase);
    revez(frase);
    return strcmp(original,frase);
}
