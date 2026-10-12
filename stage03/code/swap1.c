# include <stdio.h>
void birthday(int *age) //像之前的一样，这里的*age是一个纸条，对应的是一个地址
{
    *age=*age+1; // 这里也是一样，取用的时候*又有了解的作用，*age取到的东西
}

int main(void)
{
    int age=18;
    birthday(&age);
    printf("%d\n",age);
}