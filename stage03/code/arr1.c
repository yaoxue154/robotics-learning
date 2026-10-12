# include <stdio.h>
void birthday(int age)
{
    age=age+1;
}

int main(void)
{
    int scores[6]={100,22,33,67,89,90};

    printf("%d\n",scores[0]);
    printf("%d\n",*scores);
    printf("%d\n",*(scores+1));

    printf("%p\n",scores);
    printf("%p\n",scores+1);
    int age=18;
    birthday(age);
    printf("%d\n",age);
}