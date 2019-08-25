#include<stdio.h>
#include <stdlib.h>
#include <time.h>


 
int main()
{
    int num=0;
    int c;
    srand(time(NULL));
    
    for(c = 1; c <= 10; c++)
    {
        num = 1 + rand() % (11 - 1);
        
    }
    	printf("Numero aleatorio: %i seleccionado", num);

    return 0;
}