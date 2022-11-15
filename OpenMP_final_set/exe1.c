//Eleanna Choraiti Sideri
//AEM 4406
//exe1 serial

#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <math.h>
//#include <omp.h>
#define _USE_MATH_DEFINES
#define NR_END 1
#define FREE_ARG char*

double **dmatrix(long , long , long, long);

int main(void){
    int i, j;
    double t0, tmax, dt, t, r;
    double **u;
    double **u0;
    double k = 0.8;
    double pi = M_PI;
    double x0 = 0, xmax = 2*pi, y0 = 0, ymax = 2*pi;
    double dx, dy, x, y, d;
    long N, M;
    FILE *f1;
    
    N = 50;
    M = 50; 
    t0 = 0;
	tmax = 2*pi;   
	dt = pi/2; 
	
    dx = (xmax - x0)/ (N-1);
    dy = (ymax - y0)/ (M-1);
	
	printf("x0=%f\n", x0);
	printf("xmax=%f\n", xmax);
	printf("y0=%f\n", y0);
	printf("ymax=%f\n", ymax);
	printf("dx=%f\n", dx);
	printf("dy=%f\n", dy);
	
	/*allocate u array*/
    u0 = dmatrix(0, N-1, 0, M-1);
	u = dmatrix(0, N-1, 0, M-1);
	
	/*initialization*/
	/*border conditions*/
	/*initial conditions*/
	
	x = x0;
	y = y0;
	
	f1 = fopen("data.txt","a");

	
	for( i = 0 ; i < M ; i++ ) 
    {
		for(j = 0; j < N; j++)	
		{	
			if(i==0 || i==M-1 || j==0 || j==N-1){
				
				u0[i][j] = 0;
				//printf("%lf \t", u0[i][j]);
				fprintf(f1,"%lf \t",u0[i][j]);
  
			}
			else{
       			u0[i][j] = sin(x)*sin(0.5*y);;
       			//printf("%lf \t", u0[i][j]);
       			fprintf(f1,"%lf \t",u0[i][j]);
			}
	   		y += dy;
		}
		fprintf(f1,"\n");
		
		x += dx;
		y=y0;
    }
    
    fprintf(f1,"\n");
    d = k*dt/pow(dx,2);
    printf("d= %f\n", d);
    
    t = t0;
    while(t<=tmax+dt)
	{	
    	//printf("\n");
    	if(t==pi/2 || t==pi || t==2*pi)
		{
		printf("%f\n",t);
		fprintf(f1,"\n");
		}
		for( i = 0 ; i < M ; i++ ) 
    	{
			for(j = 0; j < N; j++)	
			{	
				if(i==0 || i==M-1 || j==0 || j==N-1)
				{
					u[i][j] = 0;
					//printf("%lf \t", u[i][j]);
					if(t==pi/2 || t==pi || t==2*pi) fprintf(f1,"%lf \t",u[i][j]);
				}
				else
				{
					r = u0[i][j] +  d*(u0[i-1][j]+u0[i+1][j]-4*u0[i][j]+u0[i][j-1]+u0[i][j+1]);
					//printf("r = %f\n", r);
       				u[i][j] = r;
       				//printf("%lf \t", u[i][j]);
       				if(t==pi/2 || t==pi || t==2*pi) fprintf(f1,"%lf \t",u[i][j]);
				}
			}
			fprintf(f1,"\n");
	    }
   		t=t+dt;
   for(i= 0; i<M ; i++)
   {
        for(j=0; j<N; j++)
		{
    		u0[i][j] = u[i][j];
		}
	}
}
	
	fclose(f1);
    
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




