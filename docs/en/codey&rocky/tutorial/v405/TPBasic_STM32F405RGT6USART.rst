TPBasic_STM32F405RGT6的串口使用
==================================

	一、什么是TPBasic_STM32F405RGT6最小系统板
---------------------------------------------------------

		TPBasic_STM32F405RGT6最小系统板是基于STM32F405RGT6芯片开发制作的最小系统板，方便开发与集成使用。


	二、利用TPBasic_STM32F405RGT6最小系统板完成串口通讯
---------------------------------------------------------------------

	1、具体要求
--------------------------------

		利用TPBasic_STM32F405RGT6最小系统板完成通过串口1和上位机对话，STM32在收到上位机发过来的字符串(以回车换
		行结束)后，原原本本的返回给上位机。同时每隔一定时间，通过串口1输出一段信息到电脑。

	2、所需器件
-----------------------------

		- TPBasic_STM32F405RGT6最小系统板		一块

		- 杜邦线					若干根

		- USB转TTL串口转换模块					一块


	三、制作主要过程
-----------------------------------

	1、制作流程
---------------------------

		将按键用杜邦线接在PC4与地之间，是按下按键IO口变为低电平

		将LED的正极接在3.3V电源处，负极接在PC11上，当IO口变为低电平时LED灯亮起，当IO口为高电平时LED灯灭。

	2、主要代码
----------------------

	.. code-block:: c
		  
		#include "sys.h"
		#include "delay.h"
		#include "usart.h"
		  
		int main(void)
		{ 
		 
			u8 t;
			u8 len;	
			u16 times=0;  
			NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);//设置系统中断优先级分组2
			delay_init(168);		//延时初始化 
			uart_init(115200);	//串口初始化波特率为115200
			while(1)
			{
				if(USART_RX_STA&0x8000)
				{					   
					len=USART_RX_STA&0x3fff;//得到此次接收到的数据长度
					printf("\r\n您发送的消息为:\r\n");
					for(t=0;t<len;t++)
					{
						USART_SendData(USART1, USART_RX_BUF[t]);         //向串口1发送数据
						while(USART_GetFlagStatus(USART1,USART_FLAG_TC)!=SET);//等待发送结束
					}
					printf("\r\n\r\n");//插入换行
					USART_RX_STA=0;
				}else
				{
					times++;
					if(times%5000==0)
					{
						printf("\r\nTPBASIC STM32F407最小系统板 串口实验\r\n");
					}
					if(times%200==0)printf("请输入数据,以回车键结束\r\n");  
					delay_ms(10);   
				}
			}
		}
