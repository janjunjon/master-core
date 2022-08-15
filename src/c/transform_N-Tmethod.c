/*
	transform_N-Tmethod.c

	1.0km���b�V���̉�͉J�ʒl��5.0km���b�V���ɕϊ�����v���O�����B
	(�x�[�X�ƂȂ����v���O�����́A1km���b�V����L�`�g���̊T�O��p����5km���b�V��
	�֕ҏW����transform_1.0-5.0_kai5.c�ł���B)

	���̃v���O�����ł́A�C�ے��̎w�j(�i�c�E�ґ� 2006)�Ɋ�Â����ꎞ�I��2.5km���b�V���̉�͉J�ʂ��쐬��
	(�t�@�C���o�͂͂��Ȃ�)�A2.5km���b�V�����̍ő�l5km���b�V����͉J�ʂƂ��č쐬����B

	�C�ے��̎w�j�Ɋ�Â�1km���b�V����2.5km��͉J�ʂɂ����ł́A�ʐς̏d�݂�t�������ς��s���B

	���}�[�N�l�i���[�_�[���ϑ����Ă��Ȃ��͈́j�͂��̂܂ܔz��̒��ɒl����ꂽ�B
	�������A���}�[�N�l�����̂܂ܓ���̂�30�i�q���ׂĂ������̏ꍇ�݂̂ł���B
	5�q�i�q���ɁA�S�i�q�ł͂Ȃ����̌����l�i-1�j���܂ޏꍇ�A
	���̒l���g�킸�A2.5�q�ꎞ��͉J�ʂ��Z�o�����B
	
	2009/03/10 Shinji Urita
	2009/03/11
	2009/07/14
	2009/07/15
	2009/07/16
	2009/12/25

	2011/01/19
	2011/01/20

	2011/12/14
	2012/02/01
	2012/02/22
	
	2013/07/25
	2013/07/29		�����l�Ή������� 
	2013/08/13�@�@�@�o�O�t�B�b�N�X���J�n
	2013/08/15		�o�O�t�B�b�N�X������
	
	2013/09/30      ���邤�N�Ή��N��ǉ�
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*-------------------------- �������牺������������ ----------------------------------------*/
#define NS 3360					/* RadarAMeDAS��5.0km�֕ϊ�����1.0km��͉J�ʂ̓�k�i�q�� */
#define WE 2560					/* RadarAMeDAS��5.0km�֕ϊ�����1.0km��͉J�ʂ̓����i�q�� */
#define PATH1 "./archive3/out/"		/* ����1.0km���b�V����͉J�ʃt�@�C��������ꏊ�ւ̃p�X */
#define RMK -1.0					/* 1km���b�V����͉J�ʂ̃��}�[�N�l */

#define NS5km 440						/* 5.0km�ɕϊ�������͉J�ʂ̓�k�i�q�� */
#define WE5km 352						/* 5.0km�ɕϊ�������͉J�ʂ̓����i�q�� */

#define RMK2 -999.0					/* 5km���b�V����͉J�ʂ̃��}�[�N�l */
#define STARTY 120						/* �������n�߂邽�Ă̔z��̈ʒu */
#define STARTX 600						/* �������n�߂鉡�̔z��̈ʒu */
#define ENDY 2762						/* �������I���邽�Ă̔z��̈ʒu */
#define ENDX 2361						/* �������I���鉡�̔z��̈ʒu */

#define PATH2 "./5km_mesh/"		/* �ꎞ�I�ɍ����2.5km���b�V�������Ƃɂ���5km���b�V����͉J�� */

//#define NS25km 1120					/* 2.5km���b�V����͉J�ʂ̓�k�i�q�� */
//#define WE25km 1024					/* 2.5km���b�V����͉J�ʂ̓����i�q�� */
//#define PATH4 "../../../../radar/1.0kmmesh/pre_made/pre_2.5km/"	/* 2.5km���b�V����͉J�ʃt�@�C���ւ̃p�X */
//#define START25Y 40						/* �������n�߂邽�Ă̔z��(2.5km)�̈ʒu */
//#define START25X 240						/* �������n�߂鉡�̔z��(2.5km)�̈ʒu */

#define STARTYEAR 2012 	/* �ҏW���J�n����N�̎w�� */
#define STARTMONTH 2	/* �ҏW���J�n���錎�̎w�� */
#define STARTDATE 29		/* �ҏW���J�n������̎w�� */
#define STARTTIME 1		/* �ҏW���J�n���鎞�Ԃ̐ݒ� */

#define ENDYEAR 2012	/* �ҏW���I������N�̎w�� */
#define ENDMONTH 3		/* �ҏW���I�����錎�̎w�� */
#define ENDDATE 1		/* �ҏW���I��������̎w�� */
#define ENDTIME 1		/* �ҏW���I�����鎞�Ԃ̎w�� */
/*-------------------------- �����܂ł����������� ---------------------------------------- */


short int rain[NS][WE];			/* 1.0km���b�V���̉J�ʂ���ꂽ�z�� */
float out[NS5km][WE5km];			/* 2.5km���b�V������ő�l���Ƃ���5km���b�V����͉J�ʂ�����z�� */
//float pre[NS25km][WE25km];		/* �ʐϏd�݂Â����ςŋ��߂�2.5km���b�V����͉J�ʂ�����z�� */


//��r�֐�
int comp(const void * a,const void * b){
    return (*(float *)b - *(float *)a);

}
int main(void){
	FILE *rainfile, *outfile, *prefile;
	int input[30], maximum;
	int cnt, i, j, n, m;
	float output[4], saidai, center[7];
	float temp=0.0;
	int year, month, date, time;
	char ipath[256], opath1[256], opath3[256];
		  
    /* �ŏ��̎����̎w�� */
    	time = STARTTIME;
		date = STARTDATE;
		month = STARTMONTH;
		year = STARTYEAR;
		
    //program start
    while(1){
		if(year == ENDYEAR){
			if(month == ENDMONTH){
				if(date == ENDDATE){
					if(time == ENDTIME){
						break;
					}
				}
			}
		}
	    
	    	/* ���o�̓t�@�C���̃I�[�v�� */
	    	sprintf(ipath, "%s%d/%02d/%02d/%d%02d%02d%02d00.bin", PATH1, year, month, date, year, month, date, time);
			rainfile=fopen(ipath, "rb");		//�@���̓t�@�C���̃I�[�v��
			printf("INPUTFILE = %d%02d%02d%02d00.bin\n", year, month, date, time);
			fread(rain, NS*WE*sizeof(rain[0][0]), 1, rainfile);

			sprintf(opath1, "%s%d/%02d/%02d/%d%02d%02d%02d.bin", PATH2, year, month, date, year, month, date, time);	
			outfile=fopen(opath1, "wb");

//			sprintf(opath3, "%s%d/%02d/%02d/%d%02d%02d%02d.bin", PATH4, year, month, date, year, month, date, time);	
//			prefile=fopen(opath3, "wb");
			
//			printf("%d,%d\n", (653-STARTY)/6, (1922-STARTX)/5);
			    //input�Ƃ����z��Ɏw�肵���s�N�Z���̉J�ʒl������
			    for(n=STARTY; n<ENDY; n=n+6){
					for(m=STARTX; m<ENDX; m=m+5){
						input[0]  = rain[n][m];
						input[1]  = rain[n][m+1];
						input[2]  = rain[n][m+2];
						input[3]  = rain[n][m+3];
						input[4]  = rain[n][m+4];
						input[5]  = rain[n+1][m];
						input[6]  = rain[n+1][m+1];
						input[7]  = rain[n+1][m+2];
						input[8]  = rain[n+1][m+3];
						input[9]  = rain[n+1][m+4];
						input[10] = rain[n+2][m];
						input[11] = rain[n+2][m+1];
						input[12] = rain[n+2][m+2];
						input[13] = rain[n+2][m+3];
						input[14] = rain[n+2][m+4];
						input[15] = rain[n+3][m];
						input[16] = rain[n+3][m+1];
						input[17] = rain[n+3][m+2];
						input[18] = rain[n+3][m+3];
						input[19] = rain[n+3][m+4];
						input[20] = rain[n+4][m];
						input[21] = rain[n+4][m+1];
						input[22] = rain[n+4][m+2];
						input[23] = rain[n+4][m+3];
						input[24] = rain[n+4][m+4];
						input[25] = rain[n+5][m];
						input[26] = rain[n+5][m+1];
						input[27] = rain[n+5][m+2];
						input[28] = rain[n+5][m+3];
						input[29] = rain[n+5][m+4];

						/* input���̔z��ɂ��ă��}�[�N�l���ǂ����`�F�b�N���� */
						if(input[0]==RMK && input[1]==RMK && input[2]==RMK && input[3]==RMK && input[4]==RMK && input[5]==RMK && input[6]==RMK && input[7]==RMK && input[8]==RMK && input[9]==RMK &&
						   input[10]==RMK && input[11]==RMK && input[12]==RMK && input[13]==RMK && input[14]==RMK && input[15]==RMK && input[16]==RMK && input[17]==RMK && input[18]==RMK && input[19]==RMK &&
						   input[20]==RMK && input[21]==RMK && input[22]==RMK && input[23]==RMK && input[24]==RMK && input[25]==RMK && input[26]==RMK && input[27]==RMK && input[28]==RMK && input[29]==RMK){
							out[(n-STARTY)/6][(m-STARTX)/5] = RMK2;
							
						}
						else{
						/* �ʐςŏd�݂Â����ꂽ2.5km���b�V����͉J�ʂ̎Z�o */
							/* ����O���b�h�̍쐬 */
							for(i=0,j=1; i<=10; i=i+5, j=j+5){
								if(input[i] != RMK){
									cnt=cnt+1;
								}
								else{
									input[i] = 0;
								}
								if(input[j] != RMK){
									cnt=cnt+1;
								}
								else{
									input[j] = 0;
								}
							}
							/* ����O���b�h���ԃ��b�V���̏��� */
							if(input[2] !=RMK){
								center[0] = input[2]/2;
								cnt = cnt + 0.5;
							}
							else{
								center[0] = 0;
							}
							if(input[7] !=RMK){
								center[1] = input[7]/2;
								cnt = cnt + 0.5;
							}
							else{
								center[1] = 0;
							}
							if(input[12] !=RMK){
								center[1] = input[7]/2;
								cnt = cnt + 0.5;
							}
							else{
								center[1] = 0;
							}
							/* ����O���b�h�̏����o�� */
							temp=input[0] + input[1] + input[5] + input[6] + input[10] + input[11] + center[0] + center[1] + center[2];
							if(temp==0){
								output[0] = 0;
							}
							else{
								output[0] = temp/cnt;
							}
							cnt = 0;
							temp = 0.0;
							
							/* �E��O���b�h�̍쐬 */
							for(i=3,j=4; i<=13; i=i+5, j=j+5){
								if(input[i] != RMK){
									cnt=cnt+1;
								}
								else{
									input[i] = 0;
								}
								if(input[j] != RMK){
									cnt=cnt+1;
								}
								else{
									input[j] = 0;
								}
							}
							/* �E��O���b�h���ԃ��b�V���̏��� */
							if(input[2] !=RMK){
								center[0] = input[2]/2;
								cnt = cnt + 0.5;
							}
							else{
								center[0] = 0;
							}
							if(input[7] !=RMK){
								center[1] = input[7]/2;
								cnt = cnt + 0.5;
							}
							else{
								center[1] = 0;
							}
							if(input[12] !=RMK){
								center[1] = input[7]/2;
								cnt = cnt + 0.5;
							}
							else{
								center[1] = 0;
							}
							/* �E��O���b�h�̏����o�� */
							temp = input[3] + input[4] + input[8] + input[9] + input[13] + input[14] + center[0] + center[1] + center[2];
							if(temp==0){
								output[1] = 0.0;
							}
							else{
								output[1] = temp/cnt;
							}
							cnt = 0;
							temp = 0.0;
							
							/* �����O���b�h�̍쐬 */
							for(i=15,j=16; i<=25; i=i+5, j=j+5){
								if(input[i] != RMK){
									cnt=cnt+1;
								}
								else{
									input[i] = 0;
								}
								if(input[j] != RMK){
									cnt=cnt+1;
								}
								else{
									input[j] = 0;
								}
							}
							/* �����O���b�h���ԃ��b�V���̏��� */
							if(input[17] !=RMK){
								center[3] = input[17]/2;
								cnt = cnt + 0.5;
							}
							else{
								center[3] = 0;
							}
							if(input[22] !=RMK){
								center[4] = input[22]/2;
								cnt = cnt + 0.5;
							}
							else{
								center[4] = 0;
							}
							if(input[27] !=RMK){
								center[5] = input[27]/2;
								cnt = cnt + 0.5;
							}
							else{
								center[5] = 0;
							}
							/* �����O���b�h�̏����o�� */
							temp= input[15] + input[16] + input[20] + input[21] + input[25] + input[26] + center[3] + center[4] + center[5];
							if(temp==0){
								output[2] = 0.0;
							}
							else{
								output[2] = temp/cnt;
							}
							cnt = 0;
							temp = 0.0;
							
							/* �E���O���b�h�̍쐬 */
							for(i=18,j=19; i<=28; i=i+5, j=j+5){
								if(input[i] != RMK){
									cnt=cnt+1;
								}
								else{
									input[i] = 0;
								}
								if(input[j] != RMK){
									cnt=cnt+1;
								}
								else{
									input[j] = 0;
								}
							}
							/* �E���O���b�h���ԃ��b�V���̏��� */
							if(input[17] !=RMK){
								center[3] = input[17]/2;
								cnt = cnt + 0.5;
							}
							else{
								center[3] = 0;
							}
							if(input[22] !=RMK){
								center[4] = input[22]/2;
								cnt = cnt + 0.5;
							}
							else{
								center[4] = 0;
							}
							if(input[27] !=RMK){
								center[5] = input[27]/2;
								cnt = cnt + 0.5;
							}
							else{
								center[5] = 0;
							}
							/* �E���O���b�h�̏����o�� */
							temp = input[18] + input[19] + input[23] + input[24] + input[28] + input[29] + center[3] + center[4] + center[5];
							if(temp==0){
								output[3] = 0.0;
							}
							else{
								output[3] = temp/cnt;
							}
							cnt = 0;
							temp = 0.0;
							
							
							//���ёւ�
							qsort(output, 4,sizeof(int), comp);
							/* 5km���b�V���ɊY������4���b�V�����ő�l�̎Z�o */
							maximum   = output[0];
							/*if(n==246 && m==1565 ){
								printf("after sort\n");
								printf("output[0]=%.1f\n", output[0]);
								printf("output[1]=%.1f\n", output[1]);
								printf("output[2]=%.1f\n", output[2]);
								printf("output[3]=%.1f\n", output[3]);
							}*/
						
							/* �ő�l��10�Ŋ����͉J�ʒl�̎Z�o */
							saidai = (float)maximum/10; 
							//printf("%.1f\n", level);
							
							out[(n-STARTY)/6][(m-STARTX)/5] = saidai;
								
						}
						/* �ϐ��Ɣz��̏����� */
						maximum = 0;
						saidai = 0;
						for(i=0; i<30; i++){
							input[i] = 0;
						}
						for(i=0; i<4; i++){
							output[i] = 0;
						}
						for(i=0; i<6; i++){
							center[i] = 0;
						}
					}
				}
			/* 5km���b�V����͉J�ʂ̏����o����2.5km���b�V���̍ő�l */
			fwrite(out, NS5km*WE5km*sizeof(out[0][0]), 1, outfile);

			/* 2.5km���b�V����͉J�ʂ̏����o�� */
			//fwrite(pre, NS25km*WE25km*sizeof(pre[0][0]), 1, prefile);
					
				// 1���Ԍ�̎�����ݒ�
			time = time+1;
			
			// ���t���܂����ꍇ�̐ݒ�
			if (time == 25){
				date = date+1;
				time = 1;
			}
					
			// �����܂����ꍇ�̏���
			if (date == 32){
				// ���̌����A12���̏ꍇ
				if (month == 12){
					year = year + 1;
					month = 1;
					date = 1;
				}
				// ���̌����A1���A3���A5���A7���A8���A10���̏ꍇ
				else if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10){
					month = month + 1;
					date = 1;
				}
			}
			// ���̌����A4���A6���A9���A11��
			if (date == 31){
				if (month == 4 || month == 6 || month == 9 || month == 11){
					month = month + 1;
					date = 1;
				}
			}
			// ���̌����A�[�N��2���̏ꍇ  ��1988�N�`2020�N�܂ł����Ή����Ă��܂���I�I
			if (date == 30){
				if (month == 2){
					if (year == 1988 || year == 1992 || year == 1996 || year == 2000 || year == 2004 || year == 2008 || year == 2012 || year == 2016 || year == 2020){
						month = month + 1;
						date = 1;
					}
				}
			}
			// ���̌����A�[�N�ȊO��2���̏ꍇ  ��1988�N�`2020�N�܂ł����Ή����Ă��܂���I�I
			if (date == 29){
				if (month == 2){
					if (year == 1988 || year == 1992 || year == 1996 || year == 2000 || year == 2004 || year == 2008 || year == 2012 || year == 2016 || year == 2020){
						date = date;
					}
					else {
						month = month + 1;
						date = 1;
					}
				}
			}
			fclose(rainfile);
			fclose(outfile);
			//fclose(prefile);
	}
	/* �t�@�C�����N���[�Y���ďI�� */
	fclose(rainfile);
	fclose(outfile);
	//fclose(prefile);
}
