#include <stdio.h>
#include <assert.h> 
#include <math.h>

int a(int n);
void test_a();

int b(int n1);
void test_b();

int c(int n2);
void test_c();

int main(){
	
	printf("%d\n", a(3));
	
	printf("\n%d\n", b(4));
	
	printf("\n%d\n", c(5));
	
	//testeo
	test_a();
	test_b();
	test_c();
	
	return 0;
}

/*
 a: Int -> Int
 Recibe un entero y calcula la sumatoria de i**2 hasta el valor n 
 con un ciclo for.
 a(5) == 5 * (5 + 1) * (2*5 + 1) / 6
 a(10) == 10 * (10 + 1) * (2*10 + 1) / 6
 a(0) == 0 * (0 + 1) * (2*0 + 1) / 6
 */
int a(int n){ //Ciclo for
	int i;
	int suma = 0;
	
	for (i = 0 ; i <= n ; i++){
		suma += pow(i,2);
		//printf("%d\n", suma);
	}
	return suma;
}

void test_a(){
	
	assert(a(5) == 5 * (5 + 1) * (2*5 + 1) / 6);
	assert(a(10) == 10 * (10 + 1) * (2*10 + 1) / 6);
	assert(a(0) == 0 * (0 + 1) * (2*0 + 1) / 6);
	printf("Listo\n");
}


/*
 b: Int -> Int
 Recibe un entero y calcula la sumatoria de i**2 hasta el valor n
 con un ciclo while.
 b(5) == 5 * (5 + 1) * (2*5 + 1) / 6
 b(10) == 10 * (10 + 1) * (2*10 + 1) / 6
 b(0) == 0 * (0 + 1) * (2*0 + 1) / 6
 */
int b(int n1){ //Ciclo  while
	int i = 0;
	int suma1 = 0;
	
	while (i <= n1){
		suma1 += pow(i,2);
		i++;
		//printf("%d\n", suma1);
	}
	return suma1;
}

void test_b(){
	
	assert(b(5) == 5 * (5 + 1) * (2*5 + 1) / 6);
	assert(b(10) == 10 * (10 + 1) * (2*10 + 1) / 6);
	assert(b(0) == 0 * (0 + 1) * (2*0 + 1) / 6);
	printf("Listo\n");
}


/*
 c: Int -> Int
 Recibe un entero y calcula la sumatoria de i**2 hasta el valor n
 con un ciclo do-while.
 c(5) == 5 * (5 + 1) * (2*5 + 1) / 6
 c(10) == 10 * (10 + 1) * (2*10 + 1) / 6
 c(0) == 0 * (0 + 1) * (2*0 + 1) / 6
 */
int c(int n2){ //Ciclo  while
	int i = 0;
	int suma2 = 0;
	
	do{
		suma2 += pow(i, 2);
		i++;
		//printf("%d\n", suma2);
		}while(i <= n2);
		
	return suma2;
}

void test_c(){
	
	assert(c(5) == 5 * (5 + 1) * (2*5 + 1) / 6);
	assert(c(10) == 10 * (10 + 1) * (2*10 + 1) / 6);
	assert(c(0) == 0 * (0 + 1) * (2*0 + 1) / 6);
	printf("Listo\n");
}


