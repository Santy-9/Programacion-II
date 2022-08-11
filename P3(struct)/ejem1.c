#include <stdio.h>

struct point {
    double x;
    double y;
};

int main(){
    struct point test;
    test.x = .25;
    test.y = .75;
    printf("[%.3f, %.3f]",test.x, test.y);
    return 0;
}


/*

typedef struct{
    double x;
    double y;
} Point;

int main(){
    Point test;
    test.x = .25;
    test.y = .75;
    printf("[%.3f, %.3f]",test.x, test.y);
    return 0;
}

*/

/*
typedef struct{
    double x;
    double y;
} Point;

int main(){
    Point test ={.25, .75};
    printf("[%.3f, %.3f]",test.x, test.y);
    return 0;
}
*/