#include <stdio.h>
#include <string.h>

#define MAX 256

int main(void){


    char string[MAX];
    char ch;
    int i = 0, contiene = 1;

    printf("\nIngrese una frase: ");
    //scanf("%[^\n]",string);
    fgets(string, sizeof(string), stdin);
    printf("\nIngrese caracter a buscar: ");
    scanf("%c ", &ch);

    for(i = 0; string[i] != '\0'; i++){
        printf("%c",ch);
        if(ch == string[i]){
            
            contiene = 0;
        }
    }

    printf("%d\n",contiene);
    return 0;



}