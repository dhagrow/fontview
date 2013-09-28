#include <stdio.h>
#include <stdlib.h>
 
/********************************************************/
/*                                                      */
/*                                                      */
/*    Initialise a 4-d array with successive numbers.   */
/*                                                      */
/*                                                      */
/*     The array is formed dynamically using malloc.    */
/*                                                      */
/*     g.watt.porteous (gemera)     17th June 2012      */
/*                                                      */
/*                 graemewp@yahoo.com                   */
/********************************************************/
 
#define d4 4
#define d3 4
#define d2 4
#define d1 4
 
 
void initarr(int ****array,int hyp_sz,int plane_sz,int row_sz,int col_sz);
 
int main(void)
{
    int ****array;
    int hyp_sz = d4,plane_sz = d3,row_sz = d2,col_sz = d1;
    int h,i,j;
 
    array = malloc(hyp_sz * sizeof(int***));
    if (array == NULL)
    {
        fprintf(stderr,"Out Of Memory");
        exit(EXIT_FAILURE);
    }
 
    for(h = 0;h < hyp_sz;h++)
    {
        array[h] = malloc(plane_sz * sizeof(int**));
        if(array[h] == NULL)
        {
            fprintf(stderr,"Out Of Memory");
            exit(EXIT_FAILURE);
        }
 
        for(i = 0;i < plane_sz;i++)
        {
            array[h][i] = malloc(row_sz * sizeof(int*));
            if(array[h][i] == NULL)
            {
                fprintf(stderr,"Out Of Memory");
                exit(EXIT_FAILURE);
            }
            for(j = 0;j < row_sz;j++)
            {
                array[h][i][j] = malloc(col_sz * sizeof(int));
                if(array[h][i][j] == NULL)
                {
                    fprintf(stderr,"Out Of Memory");
                    exit(EXIT_FAILURE);
                }
            }
        }
    }
    printf("\n\n");
 
    initarr(array,hyp_sz,plane_sz,row_sz,col_sz);   // initialise and display array
 
    getchar();
    return 0;
}
 
void initarr(int ****array,int hyp_sz,int plane_sz,int row_sz,int col_sz)
{
    int g,h,i,j;
 
    for(g = 0 ;g < hyp_sz; g++)
    {
        for(h = 0;h < plane_sz; h++)
        {
            for(i = 0;i < row_sz; i++)
            {
                for(j = 0;j < col_sz; j++)
                {
                    array[g][h][i][j] = (g*plane_sz*row_sz*col_sz) + (h*row_sz*col_sz) + (i*col_sz )+ j + 1;
                    printf("%5d", array[g][h][i][j]);
                }
                printf("\n");
            }
            printf("\n");
        }
        printf("\n\n");
    }
}
