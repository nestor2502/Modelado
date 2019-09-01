#include<stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>
//#include​ ​<omp.h>

int generaRandom(int inicio, int final){
	int numero, i;
	int limite_superior = final+1;
	int limite_inferior = inicio;
	int intervalo = limite_superior - limite_inferior;
	srand(time(NULL));
	for(i = 1; i<100; i++){
		numero =  rand() % (intervalo);

	}
	return numero;
} 
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

void quicksort1(int a[] , int longitud){
	quicksort(a, 0, longitud-1);
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
	quicksort(elementos, 0, numeros-1);
	//quicksort1(elementos, numeros);
	for(i=0; i<numeros; i++){
		
		printf("%i\n", elementos[i]);

	}
	
}