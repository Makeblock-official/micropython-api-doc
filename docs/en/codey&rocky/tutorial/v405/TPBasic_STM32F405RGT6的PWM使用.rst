TPBasic_STM32F405RGT6的PWM使用
==================================

	一、什么是TPBasic_STM32F405RGT6最小系统板
-------------------------------------------------

		TPBasic_STM32F405RGT6最小系统板是基于STM32F405RGT6芯片开发制作的最小系统板，方便开发与集成使用。
		

	二、利用TPBasic_STM32F405RGT6最小系统板完成PWM对LED呼吸灯控制
------------------------------------------------------------

	1、具体要求
----------------------

		1,DS0 LED灯(连接在PA7)
		2,定时器14(TIM14),使用TIM14的通道1(CH1),将TIM14_CH1输出到PF9.	从而实
		现PWM输出控制DS0亮度.
		
	2、所需器件
------------------------

		- TPBasic_STM32F405RGT6最小系统板		一块

		- 杜邦线					若干根

		- LED灯                 一个


	三、制作主要过程
-------------------------

	1、制作流程
----------------------

		定时器14(TIM14),使用TIM14的通道1(CH1),将TIM14_CH1输出到PF9.	从而实
		现PWM输出控制DS0亮度.
		DS0由暗到亮,再由亮到暗,再由暗到亮,依次循环.

	2、主要代码
----------------------

		code-block::

			#include "sys.h"
			#include "delay.h"
			#include "usart.h"
			#include "led.h"
			#include "pwm.h"

			int main(void)
			{ 
				u16 led0pwmval=0;    
				u8 dir=1;
				NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);//设置系统中断优先级分组2
				delay_init(168);  //初始化延时函数
				TIM14_PWM_Init(500-1,84-1);	//84M/84=1Mhz的计数频率,重装载值500，所以PWM频率为 1M/500=2Khz.     
			   while(1) //实现比较值从0-300递增，到300后从300-0递减，循环
				{
					delay_ms(10);	 
					if(dir)led0pwmval++;//dir==1 led0pwmval递增
					else led0pwmval--;	//dir==0 led0pwmval递减 
					if(led0pwmval>300)dir=0;//led0pwmval到达300后，方向为递减
					if(led0pwmval==0)dir=1;	//led0pwmval递减到0后，方向改为递增
			 
					TIM_SetCompare1(TIM14,led0pwmval);	//修改比较值，修改占空比
				}
			}
