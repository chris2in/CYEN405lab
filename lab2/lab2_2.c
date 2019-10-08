#include <stdio.h>
#include <time.h>
#include "mpi.h"

int main(int argc,char *argv[]){
	printf("WHY");

	int rank,size;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	
	printf("Hello yli027 and World! from #%d of %d!\n",rank,size);
	
	MPI_Finalize();
	return 0;

}
