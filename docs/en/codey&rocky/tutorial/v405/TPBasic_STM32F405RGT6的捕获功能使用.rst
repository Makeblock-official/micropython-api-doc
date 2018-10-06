TPBasic_STM32F405RGT6的捕获功能使用
==================================

一、什么是TPBasic_STM32F405RGT6最小系统板
--------------------------------

	TPBasic_STM32F405RGT6最小系统板是基于STM32F405RGT6芯片开发制作的最小系统板，方便开发与集成使用。
	

二、利用TPBasic_STM32F405RGT6最小系统板完成通过捕获功能捕获按键模拟的高电平时间并通过串口发送出来
------------------------------------------------------------

1、具体要求
----------------------

    1,KEY_UP按键(PA0)
    2,定时器5(TIM5),TIM5的通道1(TIM5_CH1,连接在PA0上面),使用定时器的输入捕获功能来
	捕捉PA0上面的高电平脉宽.
    
2、所需器件
------------------------

	- TPBasic_STM32F405RGT6最小系统板		一块

	- 杜邦线					若干根



三、制作主要过程
-------------------------

1、制作流程
----------------------

	本实验利用TIM5_CH1来做输入捕获，我们将捕获PA0上的高电平脉宽，并将脉宽时间通过串
	口打印出来

2、主要代码
----------------------

.. code-block:: c

#include "sys.h"
#include "delay.h"
#include "usart.h"
#include "led.h"
#include "timer.h"

extern u8  TIM5CH1_CAPTURE_STA;		//输入捕获状态		    				
extern u32	TIM5CH1_CAPTURE_VAL;	//输入捕获值  
  
	
int main(void)
{ 
	long long temp=0;  
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);//设置系统中断优先级分组2
	delay_init(168);  //初始化延时函数
	uart_init(115200);//初始化串口波特率为115200
	
 	TIM5_CH1_Cap_Init(0XFFFFFFFF,84-1); //以1Mhz的频率计数 
   	while(1)
	{
 		delay_ms(10);
 		if(TIM5CH1_CAPTURE_STA&0X80)        //成功捕获到了一次高电平
		{
			temp=TIM5CH1_CAPTURE_STA&0X3F; 
			temp*=0XFFFFFFFF;		 		         //溢出时间总和
			temp+=TIM5CH1_CAPTURE_VAL;		   //得到总的高电平时间
			printf("HIGH:%lld us\r\n",temp); //打印总的高点平时间
			TIM5CH1_CAPTURE_STA=0;			     //开启下一次捕获
		}
	}
}
