#include <stdio.h>
#include <math.h>
#include <assert.h>

typedef struct {
    double x;
    double y;
}Point;

//typedef struct point Point;

double POINTdist(Point Point1, Point Point2);
void test_POINTdist();

int POINTeq(Point Point1, Point Point2);
void test_POINTeq();

int main(){
    Point Point1;
    Point Point2;
    double pot;

    //struct point Point;
    //struct point Point1;

    printf("Ingrese coordenada x del primer punto: ");
    scanf("%lf", &Point1.x);
    printf("\nIngrese coordenada y del primer punto: ");
    scanf("%lf", &Point1.y);

    printf("\nIngrese coordenada x del segundo punto: ");
    scanf("%lf", &Point2.x);
    printf("\nIngrese coordenada y del segundo punto: ");
    scanf("%lf", &Point2.y);
/*  Ejercicio 1
    //printf("%f %f %f %f",Point1.x, Point1.y, Point2.x, Point2.y);
    //pot = Point2.x - Point1.x;
    //pot = pow((Point2.x - Point1.x),2) + pow((Point2.y - Point1.y),2);
    //printf("%f", pot);
    //printf("%.2f", sqrt(pow((Point2.x - Point1.x),2) + pow((Point2.y - Point1.y),2)));
    printf("%.2f", POINTdist(Point1, Point2));
*/
    //Ejercicio 2
    printf("%d", POINTeq(Point1, Point2));


    //Test
    test_POINTdist();
    test_POINTeq();

    return 0;
}

double POINTdist(Point Point1, Point Point2){
    double dist;

    dist = sqrt(pow((Point1.x - Point2.x),2) + pow((Point1.y - Point2.y),2));

    return dist;
}

void test_POINTdist(){
    Point Point1 = {1, 1};
    Point Point2 = {5, 4};
    assert(POINTdist(Point1 ,Point2 ) == 5.0);
    //printf("Listo");
}


int POINTeq(Point Point1, Point Point2){
    return Point1.x == Point2.x && Point1.y == Point2.y;
}

void test_POINTeq(){
    Point Point1 = {1, 2};
    Point Point2 = {1, 2};
    Point Point3 = {5, 2};
    assert(POINTeq(Point1, Point2) == 1);
    assert(POINTeq(Point1, Point3) == 0);
}