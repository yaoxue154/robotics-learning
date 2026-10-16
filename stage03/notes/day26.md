# 第 20 课《结构体——C 里的"图纸"》
## class的一半，struct
- class捆绑函数的行为和数据的处理
- struct捆绑数据，无法捆绑行为
- 代码示例
```
#include <stdio.h>

struct Student              /* 图纸：声明"学生"长什么样 */
{
    char name[20];          /* 字符串是 char 数组——下节课的主角，今天先凑合用 */
    int grade;
};

int main(void)
{
    struct Student alice = { "Alice", 85 };    /* 照图纸盖房，按顺序填 */

    printf("%s: %d\n", alice.name, alice.grade);
    alice.grade = 90;                          /* 点号 . 上门 */
    printf("%s: %d\n", alice.name, alice.grade);
    return 0;
}
```
## ->
- p->grade 就是 (*p).grade 的简写——先按地址上门，再点号取货
- 在作用域（指{}）里，可以直接用.。来处理（修改）数据
- 此处有两种方法处理数据分别是->和.
# 点灯的解读
- GPIOA->ODR |= (1 << 5);
- GPIOA是一个已经定义好的struct指针，.ODR是它的成员，现在用上一节课的掩码开灯
- kimi的注解：“STM32 的官方库干的事就是：用 struct 把芯片手册里的寄存器地址表原样描成 C 的户型图。你写 GPIOA->ODR，编译器一算偏移，正好落在那个寄存器的真实地址上——struct 的成员在内存里是挨个连排的，和寄存器的排布严丝合缝。”
# 新概念
- 作用域（scope）：变量能被看见的势力范围——就是它出生的那对 { }。出了大括号，名字就失效
- 生命周期（）：变量实际存活的时间——函数结束，房间里出生的变量全部销毁
# git add . && git commit -m "第20课：结构体与指针" && git push (&&是and)