TPBasic_STM32F405RGT6的定时器使用
==================================

一、什么是TPBasic_STM32F405RGT6最小系统板
--------------------------------

	TPBasic_STM32F405RGT6最小系统板是基于STM32F405RGT6芯片开发制作的最小系统板，方便开发与集成使用。
	

二、利用TPBasic_STM32F405RGT6最小系统板完成定时器对LED的闪烁快慢控制
------------------------------------------------------------

1、具体要求
----------------------

	1,DS0 LED灯(连接在PB9)
    2,DS1 LED灯(连接在PB10)
    
2、所需器件
------------------------

	- TPBasic_STM32F405RGT6最小系统板		一块

	- 杜邦线					若干根

	- LED灯                 二个


三、制作主要过程
-------------------------

1、制作流程
----------------------

	DS0用来指示程序运行，400ms为一个周期。DS1用于定时器中断取反，指示
	定时器中断状态，1000ms为一个周期。下载完后，可以看到DS0快闪，DS1慢闪。
    

2、主要代码
----------------------

.. code-block:: c

#include "sys.h"
#include "delay.h"
#include "usart.h"
#include "led.h"
#include "timer.h"

int main(void)
{ 
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);//设置系统中断优先级分组2
	delay_init(168);  //初始化延时函数
	LED_Init();				//初始化LED端口

 	TIM3_Int_Init(5000-1,8400-1);	//定时器时钟84M，分频系数8400，所以84M/8400=10Khz的计数频率，计数5000次为500ms     
	while(1)
	{
		LED0=!LED0;//DS0翻转
		delay_ms(200);//延时200ms
	};
}

