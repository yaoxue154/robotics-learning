#include<stdio.h>
struct student
{
    char name[20];
    int age;
};
int main(void)
{
    struct student Alice={"Alice",20};
    struct student bob=Alice;
    struct student *p=&bob;
    (&bob)->age=33;
    p->age=22;
    printf("%s:%d\n",Alice.name,Alice.age);

}