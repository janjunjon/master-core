/*
	short2f4ra1km.c
	
	入力ファイルの型を変更して、1/10にして 出力するプログラム
	short → float
		
	Jin SAITO
	12, July, 2012
	
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*--------------------------------------------------*/
#define IFN1 argv[1]			/* 入力 */
#define OFN1 argv[2]			/* 出力 */

#define NS 3360					/* 1km解析雨量の南北格子数 */
#define WE 2560					/* 1km解析雨量の東西格子数 */
/*--------------------------------------------------*/

short in[NS][WE];		/*  */
float out[NS][WE];				/*  */

int main(int argc, char *argv[]){
	
	/* ファイルポインタの宣言 */
	FILE *infile, *outfile;
	
	/* 変数の宣言 */
	int n, m;
	
	/* ファイルのオープン */
	
	infile=fopen(IFN1, "rb");
	if(fread(in, NS*WE*sizeof(in[0][0]), 1, infile)!=1){
		printf("In file is error \n");
		exit(1);
	}
	
	outfile=fopen(OFN1, "wb");
	
	
		/* プログラムスタート */
	
	for(n=0; n<NS; n++){
		for(m=0; m<WE; m++){
			
			out[n][m] = (float)(in[n][m]/10);
			
		}
	}
	fwrite(out, NS*WE*sizeof(out[0][0]), 1, outfile);
		
	/* ファイルをクローズして終了 */
	fclose(infile);
	fclose(outfile);
}
