TPBasic_STM32F405RGT6的外部中断使用
==================================

一、什么是TPBasic_STM32F405RGT6最小系统板
--------------------------------

	TPBasic_STM32F405RGT6最小系统板是基于STM32F405RGT6芯片开发制作的最小系统板，方便开发与集成使用。
	

二、利用TPBasic_STM32F405RGT6最小系统板学习外部中断的使用
------------------------------------------------------------

1、具体要求
----------------------

	1,DS0 LED灯(连接在PB9)
    2,DS1 LED灯(连接在PB10)
	2,蜂鸣器(连接在PB8) 
	3,按键KEY0(PA3)/KEY1(PA4)/KEY2(PA5)/KEY_UP(PA0,也称之为WK_UP)
    
2、所需器件
------------------------

	- TPBasic_STM32F405RGT6最小系统板		一块

	- 杜邦线					若干根

	- 按键					四个
    
    - 蜂鸣器                 一个
    
    - LED灯                 二个


三、制作主要过程
-------------------------

1、制作流程
----------------------

	通过开发外接的4个按	钮（KEY_UP、KEY0、KEY1和KEY2），来控制外接的2个LED（DS0、DS1）和蜂鸣器
	，其中WK_UP控制蜂鸣器，按一次叫，再按一次停；KEY2控制DS0，按一次亮，再按
	一次灭；KEY1控制DS1，效果同KEY2；KEY0则同时控制DS0和DS1，按一次，他们的
	状态就翻转一次。
    

2、主要代码
----------------------

.. code-block:: c

#include "sys.h"
#include "delay.h"
#include "usart.h"
#include "led.h"
#include "beep.h"
#include "key.h"
#include "exti.h"

int main(void)
{ 
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);//设置系统中断优先级分组2
	delay_init(168);    //初始化延时函数
	
	LED_Init();				  //初始化LED端口  
	BEEP_Init();        //初始化蜂鸣器端口
	EXTIX_Init();       //初始化外部中断输入 
	LED0=0;					    //先点亮红灯
	while(1)
	{
	}

}
