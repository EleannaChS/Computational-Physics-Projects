#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#define NR_END 1
#define FREE_ARG char*


double **dmatrix(long , long , long, long);
double random(double, double);
double **sort(double **, long , long);

int main(void)
{
    int i,j; 	
	long M, N;
	double **table, r;
	time_t t;
	double low=1001.0,high=1201.0;
	char error_text;

    printf("Enter the sizes of the Matrix M,N: \n");
    scanf("%ld%ld", &M, &N);
    table = dmatrix(0, M-1, 0, N-1);
     
    /* Intializes random number generator */
   	srand((unsigned) time(&t));
   
    printf("Initial table: \n");
    for( i = 0 ; i < M ; i++ ) 
    {
		for(j = 0; j < N; j++)	
		{
			r = random(low, high);
       		table[i][j] = r;
       		printf("%lf \t", table[i][j]);
		}
		printf("\n");
    }
    
    table = sort(table, M, N);
    
    printf("\nSorted table: \n");
    for( i = 0 ; i < M ; i++ ) 
    {
		for(j = 0; j < N; j++)	
		{
       		printf("%lf \t", table[i][j]);
		}
		printf("\n");
   }
   return 0;
}


void nrerror(char error_text[])
/* Numerical Recipes standard error handler */
{
	fprintf(stderr,"Numerical Recipes run-time error...\n");
	fprintf(stderr,"%s\n",error_text);
	fprintf(stderr,"...now exiting to system...\n");
	exit(1);
}

double **dmatrix(long nrl, long nrh, long ncl, long nch)
/* allocate a double matrix with subscript range m[nrl..nrh][ncl..nch] */
{
	long i, nrow=nrh-nrl+1,ncol=nch-ncl+1;
	double **m;

	/* allocate pointers to rows */
	m=(double **) malloc((size_t)((nrow+NR_END)*sizeof(double*)));
	if (!m) nrerror("allocation failure 1 in matrix()");
	m += NR_END;
	m -= nrl;

	/* allocate rows and set pointers to them */
	m[nrl]=(double *) malloc((size_t)((nrow*ncol+NR_END)*sizeof(double)));
	if (!m[nrl]) nrerror("allocation failure 2 in matrix()");
	m[nrl] += NR_END;
	m[nrl] -= ncl;

	for(i=nrl+1;i<=nrh;i++) m[i]=m[i-1]+ncol;

	/* return pointer to array of pointers to rows */
	return m;
}

double random(double l, double h)
{
	double f;
	f =l + (float) (rand())/((float) (RAND_MAX/(h-l)));
	return f;
}

// Εφόσον δεν είχα καταφέρει το merge sort όπως σας έστειλα κάνω sort τον πίνακα με άλλον τρόπο απλά για να
//δείξω το function. Δεν περιμένω να βαθμολογηθώ για αυτό το sorting ωστόσο θέλησα να ολοκληρώσω την άσκηση.
double **sort(double **matr, long lin, long col)
{
	int i,j,k;
	double temp;
	
	for( i = 0 ; i < col ; i++)
    {
    	for( j= 0 ; j < lin ; j++)
    	{
    		for (k = j+1 ; k< lin; k++)
    		{
    			if(matr[j][i] > matr[k][i])
    			{
    				temp = matr[j][i];
    				matr[j][i] = matr[k][i];
					matr[k][i] = temp;
			    }
			}
    	
		}
	}
    return matr;
}
    
 
