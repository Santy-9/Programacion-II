#include <stdio.h>
#include <string.h>
#include <assert.h>

#define MAX 256

int ej19(char palabra[MAX], char ch);
void test_ej19(void);

int main(){
    char palabra[MAX];
    char ch;

    printf("Ingrese palabra: ");
    fgets(palabra, sizeof(palabra), stdin);

    printf("\nIngrese caracter a buscar: ");
    scanf("%c", &ch);

    printf("%d", ej19(palabra, ch));


}

int ej19(char palabra[MAX], char ch){
    int i;
    int cont = 0;

    for (i = 0; palabra[i] != '\0'; i++){
        if(ch == palabra[i]){
            cont++;
        }
    }
    return cont;
}

void test_ej19(void){
    assert(ej19("hola", 'l') == 1);
    assert(ej19("que onda pa", 'a') == 2);
    assert(ej19(" ", 'i') == 0);
}