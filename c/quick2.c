#include<stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

/**
*Metodo que ordena dos arreglos ordenados
*/
void merge(int s[], int sub[][2]){
  int tamano = sub[1][1]+1;//longitud del arreglo
  //int arr[tamano]; //arreglo donde se almacenara el numero ordenado
  int *arr = malloc(tamano*sizeof(int));
  int i = sub[0][0]; //inicio sub arreglo 1
  int j = sub[1][0]; //inicio sub arreglo 2
  int limite_superior1 = sub[0][1]; //cota sup del  sub arreglo 1
  int limite_superior2 = sub[1][1]; //cota sup del  sub arreglo 2
  int l = 0; //indice del arreglo ordenado
  while(i<=limite_superior1 && j<=limite_superior2){
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
  for(int z = 0; z<=limite_superior2; z++){//se reasignan los valores delarreglo original
    s[z]= arr[z];}
}

/**
*Intercambia dos valores
*/
void swap(int *a , int *b){
	int temp = *a;
	*a = *b;
	*b = temp;
}
/**
*Metodo
*
*/
void quicksort(int arr[] , int a, int b){
	if (a < b) {
        int i = a, j = b;
        int pivote = arr[(i + j) / 2];
            do {
                while (arr[i] < pivote)
                	i++;
                while (pivote < arr[j])
                	j--;
                if ( i <= j) {
                   swap(&arr[i], &arr[j]);
                    i++;
                    j--;
                }
            } while (i <= j);
            quicksort(arr, a, j);
            quicksort(arr, i, b);
	}}

/**
*Metodo que aplica quicksort
*/
void quicksort1(int a[] , int longitud){
	quicksort(a, 0, longitud-1);
	}

/**
*Metodo que aplica quick paralelo
*/
void quickParalelo(int a[] , int longitud){
  int mitad = longitud/2;
  int inicio1 = 0;
	int inicio2 =mitad ;
	int final1 =mitad-1 ;
	int final2 = longitud-1 ;
	int sub [2][2];
  sub[0][0]=0;
  sub[0][1]=final1;
  sub[1][0]=inicio2;
  sub[1][1]=final2;
	quicksort(a, 0, final1);
	quicksort(a, inicio2, final2);
	merge(a, sub);
}

int main(){
	int numeros = 0;
	//numero de elementos a ingresar
	scanf("%i", &numeros);
	int i ;
	int j =0;
	int elementos[numeros];
	for(i=0; i<numeros; i++){
		scanf("%i",&j);
		elementos[i]= j;
	}
	quickParalelo(elementos, numeros);
	for(i=0; i<numeros; i++){
		printf("%i\n", elementos[i]);
	}
}
