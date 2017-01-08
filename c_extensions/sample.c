#include <math.h>

int gcd(int x, int y){
	int g = y;
	while(x > 0){
		g = x;
		x = y % x;
		y = g;
	}
	return g;
}

int divide(int x, int y, int *reminder){
	int quotient = x / y;
	*reminder = x % y;
	return quotient;
}

double avg(double *a, int n){
	int i;
	double total = 0.0;
	for(i=0;i<n;i++){
		total += a[i];
	}
	return total/n;
}

typedef struct Point{
	double x, y;
}Point;

double distance(Point *p1, Point *p2){
	return hypot(p1->x - p2->x, p1->y - p2->y);
}