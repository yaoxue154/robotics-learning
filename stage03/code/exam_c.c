#include<stdio.h>
int count_on(unsigned int reg)
{
    int count=0;
    int i=0;
    while(i<8)
    {
        if(reg&(1<<i))
        {
            count+=1;
        }
        i+=1;
    }
    return count;
}
int main(void)
{
    unsigned int reg=0;
        reg|=(1<<0);
        reg|=(1<<2);
        reg|=1<<7;
        printf("number of lighting bits in reg is %d\n",count_on(reg));
        printf("reg=%x\n",reg);
        reg &=~(1<<2);
        printf("number of lighting bits in reg is %d\n",count_on(reg));
        return 0;
}