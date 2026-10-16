#include<stdio.h>
void gg(void)
{
    char a[5]="alice";
    printf("%s\n",a);

}
int main(void)
{
    char name[20]="Alice";
    int i=0;
    while(name[i]!='\0')
    {
        printf("%c\n",name[i]);
        i=i+1;
    }
    printf("'\\0'is the end of string,%d\n",i);
    gg();
    return 0;
}
