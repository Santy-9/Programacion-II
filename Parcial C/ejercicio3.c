#include <stdio.h>
#include <string.h>
#include <assert.h> 

#define MAX 256 //-

int b(char palabra[MAX]);
int a(char palabra[MAX]);

int main(){
	char p[MAX] = "tu, un chucrut";
	
	if(a(p) >= 3 && b(p)){ //3 espacios en blanco, la frase tiene minimo 4 palabras.
		printf("Palabra valida");
	}else{
		printf("Palabra no valida");
	}
	
	return 0;
}


int a(char palabra[MAX]){
	int i;
	int cont = 0;
	char ch = ' ';

	for(i = 0; palabra[i] != '\0'; i++){
		if(ch == palabra[i]){
			cont++;
		}
	}
	return cont;
}

/*
 b: String -> Int
 Recibe una palabra verifica si la frase tiene una sola vocal.
 */
int b(char palabra[MAX]){
	int i;
	int cont_a = 0, cont_e = 0, cont_i = 0, cont_o = 0, cont_u = 0;
	int boolean;
	//int longitud = strlen(palabra);
	
	for(i = 0 ; palabra[i] != '\0' ; i++){
		//printf("%s", palabra);
		switch(palabra[i]){
			case 'a':
				cont_a += 1;
				break;
			case 'e':
				cont_e += 1;
				break;
			case 'i':
				cont_i += 1;
				break;
			case 'o':
				cont_o += 1;
				break;
			case 'u':
				cont_u += 1 ;
				break;
		}
	}
	
	if(cont_a > 0 && cont_e == 0 && cont_i == 0 && cont_o == 0 && cont_u == 0){
		boolean = 1;  //palabra valida
	}else if(cont_a == 0 && cont_e > 0 && cont_i == 0 && cont_o == 0 && cont_u == 0){
		boolean = 1;
	}else if(cont_a == 0 && cont_e == 0 && cont_i > 0 && cont_o == 0 && cont_u == 0){
		boolean = 1;
	}else if(cont_a == 0 && cont_e == 0 && cont_i == 0 && cont_o > 0 && cont_u == 0){
		boolean = 1;
	}else if(cont_a == 0 && cont_e == 0 && cont_i == 0 && cont_o == 0 && cont_u > 0){
		boolean = 1;
	}else{
		boolean = 0;  //palabra no valida
	}
		
	return boolean;
}
