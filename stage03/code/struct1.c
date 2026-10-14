# include<stdio.h>
struct Student
{
    char name[20];
    int age;
};

int main(void)
{
    struct Student Alice ={"Alice",20};
    printf("%s:%d\n",Alice.name,Alice.age);
    Alice.age=88;
    printf("%s:%d\n",Alice.name,Alice.age);

    struct Student Bob={"Bob",30};
    struct Student *p=&Bob;
    p->age=35;
    printf("%s:%d\n",p->name,p->age);
    return 0;
}