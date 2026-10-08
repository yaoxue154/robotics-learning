#include<stdio.h>
int main(void)
{
    int age=18;
    int *p=&age;

    printf("%p\n",p);
    printf("%d\n",*p);

    *p=20;
    printf("%d\n",age);
    age=300;
    printf("%d\n",age);
    return 0;
}