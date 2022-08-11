#include <stdio.h>
#include <assert.h>
#include <string.h>

#define MAX 256

typedef struct{
    char nombre[MAX];
    char apellido[MAX];
    int dni;
    int telefono;
    int edad;
    
}Persona;

//typedef struct{
//    Persona persona5;
//    int legajo;
//}Estudiante;

Persona crear_persona(char nombre[], char apellido[], int dni, int telefono, int edad);

void imprimir_Persona(Persona persona);

int igual_identidad(Persona persona, Persona persona1);

int es_familiar(Persona persona, Persona persona1);

int main(){
    Persona persona;
    Persona persona1;// = {"mart", "mar", 41489, 2356, 18};
    //Estudiante estudiante ={persona, 25};
    char nombre[MAX];
    char apellido[MAX];
    int dni, telefono, edad;
    char nombre1[MAX];
    char apellido1[MAX];
    int dni1, telefono1, edad1;

    printf("Ingrese nombre: ");
    fgets(nombre, sizeof(nombre), stdin);

    //while(getchar()!= '\n');

    printf("Ingrese apellido: ");
    fgets(apellido, sizeof(apellido), stdin);

    printf("Ingrese dni, telefono y edad: ");
    scanf("%d %d %d",&dni, &telefono, &edad);
    //---------------------------------
    while(getchar()!= '\n');
    printf("Ingrese nombre: ");
    fgets(nombre1, sizeof(nombre1), stdin);

    printf("Ingrese apellido: ");
    fgets(apellido1, sizeof(apellido1), stdin);

    printf("Ingrese dni, telefono y edad: ");
    scanf("%d %d %d",&dni1, &telefono1, &edad1);


    persona = crear_persona(nombre, apellido, dni, telefono, edad);
    persona1 = crear_persona(nombre1, apellido1, dni1, telefono1, edad1);

    if(igual_identidad(persona, persona1)){
        printf("Misma persona.\n");
    }else{
        printf("Disitnta persona\n");
    }

    if(es_familiar(persona, persona1)){
        printf("No es familiar.\n");
    }else{
        printf("Es familiar.\n");
    }

}

/*
crear_persona: String String Int Int Int -> Persona
Recibe cinco datos:
    -Nombre
    -Apellido
    -dni
    -telefono
    -edad
Devuelve una estructura tipo Persona.
*/
Persona crear_persona(char nombre[], char apellido[], int dni, int telefono, int edad){
    Persona persona1;

    strcpy(persona1.nombre, nombre);
    strcpy(persona1.apellido, apellido);
    persona1.dni = dni;
    persona1.telefono = telefono;
    persona1.edad = edad;

    return persona1;
}

/*
imprimir_Persona: Persona -> Void
Recibe un dato de tipo Persona y lo muestra por pantalla.
*/
void imprimir_Persona(Persona persona){

    printf("Nombre: %s Apellido: %s DNI: %d\n Telefono: %d\n Edad: %d",
    persona.nombre, persona.apellido, persona.dni, persona.telefono, persona.edad);

}

/*
igual_identidad: Persona Persona -> Int
Recibe dos datos de tipo Persona y compara si es la misma persona segun su DNI.
*/
int igual_identidad(Persona persona, Persona persona1){

    return persona.dni == persona1.dni;
}

/*
es_familiar: Persona Persona -> Int
Recibe dos datos de tipo Persona y comprueba si son familiares.
*/
int es_familiar(Persona persona, Persona persona1){

    //printf("%d" ,strcmp(persona.apellido, persona1.apellido));
    return strcmp(persona.apellido, persona1.apellido);

}
