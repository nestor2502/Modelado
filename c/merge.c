#include<stdio.h>
#define SIZE 10000000
/**
*Metodo que ordena dos arreglos ordenados
*/
void merge(int s[], int sub[][2]){
  int arr[8]; //arreglo donde se almacenara el numero ordenado
  int i = sub[0][0]; //inicio sub arreglo 1
  int j = sub[1][0]; //inicio sub arreglo 2
  int limite_superior1 = sub[0][1]; //cota sup del  sub arreglo 1
  int limite_superior2 = sub[1][1]; //cota sup del  sub arreglo 2
  //int tamaño1 = sub[0][1]+1;
  //int tamaño2 = sub[1][1]+1-sub[0][1];//tamaño del sub arreglo 2 
  //int *A = malloc(tamaño1*sizeof(int));	
  //int *B = malloc(tamaño2*sizeof(int);
  //int *C = malloc(sub[1][1]+1);
  int l = 0; //indice del arreglo ordenado
  while(i<=limite_superior1 && j<=limite_superior2){//me vale verga
    if(s[i]<=s[j] && i<=limite_superior1){//si el elemento del indice i es menor o igual al indice j
      arr[l]=s[i];
      l++;//se aumenta el indice del nuevo arreglo
      i++;}
    else if ( s[j]<=s[i] && j<=limite_superior2 ) {//si el elemento del indice i es menor o igual al indice j
      arr[l]=s[j];
      l++;//se aumenta el indice del nuevo arreglo
      j++;}
  }

  if(i<=limite_superior1){//se meten lo numeros del primer intervalo sobrantes 
    for(int r = i; r<=limite_superior1;r++){
      arr[l]=s[i];
      l++;
      i++;
    }
  }
  else if(j<=limite_superior2){//se meten lo numeros del segundo intervalo sobrantes 
    for(int r = j; r<=limite_superior2;r++){
      arr[l]=s[j];
      l++;
      j++;
    }
  }
  for(int z = 0; z<=limite_superior2; z++){
    s[z]= arr[z];}
}


int main(){
  //int longitud = sizeof(tuArreglo) / sizeof(tuArreglo[0]);
  //int matriz[]= {0,2,4,6,1,3,5,7};
  int matriz[]= {1, 3, 5, 7, 0, 2, 4, 8};
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

