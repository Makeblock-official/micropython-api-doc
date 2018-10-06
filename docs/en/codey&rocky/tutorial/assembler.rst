.. _TPYBoard_tutorial_assembler:

内联汇编
================

在这里，您将学习如何在MicroPython中编写内联汇编程序。

**注意**：这是一个高级教程，适用于了解微控制器和汇编语言的一些用户。

MicroPython包括一个内联汇编器。
它允许你写汇编程序时作为Python函数，您可以按照您的要求调用它们一个普通的Python函数。

返回一个值
-----------------

内联汇编器函数由特殊函数装饰器表示。首先，我们从最简单的例子开始：
::
    @micropython.asm_thumb
    def fun():
        movw(r0, 42)

您可以在脚本或REPL中输入。
此功能不需要参数并返回数字42，“r0“是一个寄存器和值。当函数返回时，在该寄存器中返回值。
MicroPython总是将“r0“解释为整数，并将其转换为调用者的整数对象。

如果你运行“print(fun())“你会看到它打印出来42。

访问外设
---------------------

对于一些有点复杂的事情，让我们打开一个LED灯：
::
    @micropython.asm_thumb
    def led_on():
        movwt(r0, stm.GPIOA)
        movw(r1, 1 << 13)
        strh(r1, [r0, stm.GPIO_BSRRL])

此代码使用以下几个新概念:

  - “stm“是一个提供一组常量的模块，访问TPYBoard微控制器的寄存器。
    尝试在REPL上运行“import stm“然后“help（stm）“，它会给你列出所有可用的常量。

  - “stm.GPIOA“是GPIOA外设的内存地址。
     在TPYBoard上，红色LED指示灯位于端口A，引脚PA13上。

  - “movwt“将32位数字移入一个寄存器。这是一个方便功能变成两个拇指指令：“movw“，后跟“movt“。
     “movt“也把立即数值右移16位。

  - “strh“存储一个半字（16位），上面的说明书“r1”的低16位进入内存位置“r0 + stm.GPIO_BSRRL“。
    这具有将端口A上的所有引脚设置为高的效果，“r0”中的相应位置为1。在上面的例子中，第13个“r0”中的位被设置，所以PA13被拉高，这将打开红色LED指示灯。

接受参数
-------------------

内联汇编程序函数最多可以接受4个参数，如果使用，它们必须被命名为“r0“，“r1“，“r2“和“r3“来反映寄存器和调用约定。

这里是一个添加其参数的函数：
::
    @micropython.asm_thumb
    def asm_add(r0, r1):
        add(r0, r0, r1)

这执行计算“r0 = r0 + r1“。 由于结果被放在“r0“里，就是返回的。所以去尝试“asm_add(1，2)“，它应该返回3。


循环
-----

我们可以使用“label(my_label)“分配标签，并使用它们分支“b(my_label)“，或“bgt(my_label)“条件分支。

以下示例闪烁绿色LED灯。它闪烁“r0“次“：
::
    @micropython.asm_thumb
    def flash_led(r0):
        # get the GPIOA address in r1
        movwt(r1, stm.GPIOA)

        # get the bit mask for PA14 (the pin LED #2 is on)
        movw(r2, 1 << 14)

        b(loop_entry)

        label(loop1)

        # turn LED on
        strh(r2, [r1, stm.GPIO_BSRRL])

        # delay for a bit
        movwt(r4, 5599900)
        label(delay_on)
        sub(r4, r4, 1)
        cmp(r4, 0)
        bgt(delay_on)

        # turn LED off
        strh(r2, [r1, stm.GPIO_BSRRH])

        # delay for a bit
        movwt(r4, 5599900)
        label(delay_off)
        sub(r4, r4, 1)
        cmp(r4, 0)
        bgt(delay_off)

        # loop r0 times
        sub(r0, r0, 1)
        label(loop_entry)
        cmp(r0, 0)
        bgt(loop1)

进一步阅读
---------------

有关内联汇编程序支持的指令的更多信息，
请参阅：ref:`reference documentation <asm_thumb2_index>`。
