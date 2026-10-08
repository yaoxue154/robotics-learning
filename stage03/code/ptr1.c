#include<stdio.h>
int main(void)
{
    int age=18;
    int *p=&age;

    printf("%p\n",p);
    printf("%d\n",*p);
    return 0;
}