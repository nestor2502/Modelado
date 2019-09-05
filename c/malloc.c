#include<stdio.h>
#include <stdlib.h>


void merge(int s[], int sub[][2]){
  int tamano = sub[1][1]+1;//longitud del arreglo
  int *L = malloc(tamano*sizeof(int));
  L[0] = 6;
  L[1] = 6;
  L[2] = 6;
  L[3] = 6;
  L[4] = 6;
  L[5] = 6;
  L[6] = 6;
  L[7] = 6;


  for(int z = 0; z<=tamano; z++){//se reasignan los valores delarreglo original
    s[z] = L[z];}
}



int main(){
  //int matriz[]= {0,2,4,6,1,3,5,7};
  int matriz[]= {1, 3, 5, 7, 0, 2, 4, 8};
  int longitud = sizeof(matriz) / sizeof(matriz[0]);
  int mitad;

  mitad = longitud/2;

  //printf("mitad %i\n",mitad );


  int sub [2][2];
  sub[0][0]=0;
  sub[0][1]=3;
  sub[1][0]=4;
  sub[1][1]=7;
  merge(matriz, sub);

  for(int i = 0; i<8; i++){
    printf("%i\n",matriz[i]);
  }

  return 0;
}
