#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

class Particle{
	private:
		int position;
	public:
	    Particle(){
	}		
	Particle(int po){
		po = 0;
		position = po;
	}	

	int getPosition(){
		return position;
	}
	
	int MoveRight(int position){
		return position+1;
	}
	
	int MoveLeft(int position){
		return position-1;
	}

};


class Experiment{
	private:
		Particle p;
		int steps;
	public:
	    Experiment(){
	}		
	Experiment(int s){
		steps =s;
	}
		
	int run(){
		float k;
		int i, x;
		x = p.getPosition();
		srand( (unsigned)time( NULL ) );
		for(i = 1; i<= steps; i++)
			{
				k = (float)rand()/RAND_MAX;	
				if (k < 0.5)
				x = p.MoveLeft(x);
				else
				x =p.MoveRight(x);
			}
	return x;	
	}

};

int main(void){
	int fp, st;
	cout << "Random walk across axis" <<endl;
	for (st = 10 ; st<=100000 ; st *=10)
	{
		Experiment ex(st);
		fp = ex.run();
		cout << "steps= " << st << "\tfinal position: " << fp << endl;
	}
return 0;
}
