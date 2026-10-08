#include <stdio.h>

int main(void) 
{
    int age=18;
    printf("age=%d\n",age);
    printf("age住在%p\n",&age);
    printf(" int 户型大小%d字节\n",sizeof(int));
    printf(" age 户型大小%d字节\n",sizeof(&age));
    return 0;
}