/*
	short2f4ra1km.c
	
	$BF~NO%U%!%$%k$N7?$rJQ99$7$F!"(B1/10$B$K$7$F(B $B=PNO$9$k%W%m%0%i%`(B
	short $B"*(B float
		
	Jin SAITO
	12, July, 2012
	
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*--------------------------------------------------*/
#define IFN1 argv[1]			/* $BF~NO(B */
#define OFN1 argv[2]			/* $B=PNO(B */

#define NS 3360					/* 1km$B2r@O1+NL$NFnKL3J;R?t(B */
#define WE 2560					/* 1km$B2r@O1+NL$NEl@>3J;R?t(B */
/*--------------------------------------------------*/

short in[NS][WE];		/*  */
float out[NS][WE];				/*  */

int main(int argc, char *argv[]){
	
	/* $B%U%!%$%k%]%$%s%?$N@k8@(B */
	FILE *infile, *outfile;
	
	/* $BJQ?t$N@k8@(B */
	int n, m;
	
	/* $B%U%!%$%k$N%*!<%W%s(B */
	
	infile=fopen(IFN1, "rb");
	if(fread(in, NS*WE*sizeof(in[0][0]), 1, infile)!=1){
		printf("In file is error \n");
		exit(1);
	}
	
	outfile=fopen(OFN1, "wb");
	
	
		/* $B%W%m%0%i%`%9%?!<%H(B */
	
	for(n=0; n<NS; n++){
		for(m=0; m<WE; m++){
			
			out[n][m] = (float)(in[n][m]/10);
			
		}
	}
	fwrite(out, NS*WE*sizeof(out[0][0]), 1, outfile);
		
	/* $B%U%!%$%k$r%/%m!<%:$7$F=*N;(B */
	fclose(infile);
	fclose(outfile);
}
