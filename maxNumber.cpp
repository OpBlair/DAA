#include<iostream>

int main(){
	
	int array [] = {1,2,3,9,5,4,6};
	int arraySize = sizeof(array)/sizeof(array[0]);
	int arrayMax = array[0];
	int maxIndex = 0;

	for(int a = 0; a < arraySize; a++){
		if(arrayMax <= array[a]){
			arrayMax = array[a];
			maxIndex = a;
		}
	}

	std::cout << "This program finds the maximum number in a given array\n";

	std::cout << "Array = ";

	for(int b = 0; b < arraySize; b++){
		std::cout << array[b] << " ";
	}

	std::cout << "\nThe maximum number in the array is " << arrayMax << " at position " << maxIndex + 1 << std::endl;

	return 0;
}