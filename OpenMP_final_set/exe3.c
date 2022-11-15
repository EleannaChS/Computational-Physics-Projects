//Eleanna Choraiti Sideri
//AEM 4406
//bisection method parallel

#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <math.h>

long double f(long double);

int main(void){
    long double fx, x, a, b, m, alpha, beta, acc, root;
    int maxit = 1000;
    int idnum, nthreads,i;

    a = -100;
    b = -2;
    acc = pow(10,-10000000);

    double tstart = omp_get_wtime();

    #pragma omp parallel private(idnum, alpha, beta, m, i, root)\
                         shared(nthreads,a,b,acc)\
                         firstprivate(maxit)
    {
       nthreads = omp_get_num_threads();
       idnum = omp_get_thread_num();
       alpha = a + idnum*(b-a)/nthreads;
       beta = a + (idnum+1)*(b-a)/nthreads;
       if(idnum == nthreads - 1) beta = b;
       m = (alpha + beta)/2;
    
       if(f(alpha)*f(beta)>0){
            printf("\nThread num: %d\n", idnum);
            printf("Interval is (%Lf,%Lf)\n", alpha, beta);
            printf("There is no root in the interval\n");
            //printf("There is no root in the interval (%Lf,%Lf)\n", alpha, beta);
       }
       else{
           printf("\nThread num: %d\n", idnum);
           printf("Interval is (%Lf,%Lf)\n", alpha, beta);
           for (i=0; i<maxit;i++){
               //printf("f(m) = %f", f(m));
               if(fabs(f(m))>acc){
                      if(f(alpha)*f(m)<0){
                        beta = m;
                        m = (alpha + beta)/2;
                        } 
                        else if(f(alpha*f(m)>0)){
                        alpha = m;
                        m = (alpha + beta)/2;
                        }
               }
               else i = maxit;
           }
            root = m;
            printf("Root is %Lf\n\n", root);
       }      
      
    }  
    
    double tend = omp_get_wtime();  
    printf("Time: %f seconds\n\n", tend - tstart);               
    return 0;
}

long double f(long double x){
    long double y = 0.2*(x+4)*(x+1)*(x-1)*(x-3)+0.5;
    return y;
}