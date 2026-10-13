# include <stdio.h>
int main(void)
{
    unsigned int REG=0;  /* 无符号(unsigned)整数房子，只能装 0 和正数 */
    REG |=1<<3; // set the third bit of REG
    REG |=1<<5; // set the fifth bit of REG
    printf("lit the third and fifth bits of REG: 0x%x\n", REG);
    
    REG ^=1<<3; // toggle the third bit of REG(turn down)
    printf("toggle the third bit of REG: 0x%x\n",REG);

    if (REG & 1<<5) 
    {
        printf("the fifth bit of REG is set\n"); //lighting
    }
    REG &= ~(1<<5); // clear the fifth bit of REG
    printf("after clearing the fifth bit of REG: 0x%x\n", REG);
    return 0;
}