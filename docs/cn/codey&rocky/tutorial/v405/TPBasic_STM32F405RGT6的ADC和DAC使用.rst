TPBasic_STM32F405RGT6的ADC和DAC使用
===============================================

	一、什么是TPBasic_STM32F405RGT6最小系统板
-------------------------------------------------------------------------

		TPBasic_STM32F405RGT6最小系统板是基于STM32F405RGT6芯片开发制作的最小系统板，方便开发与集成使用。
		

	二、利用TPBasic_STM32F405RGT6最小系统板利用按键控制W25Q128的写入和读取，并通过串口显示
-------------------------------------------------------------------------------------------------------

	1、具体要求
----------------------

		通过KEY1按键来控制W25Q128的写入，通过另外一个按键KEY0来控制W25Q128的读取。
		可以通过USMART控制读取W25QXX的ID或者整片擦除。

	2、所需器件
------------------------

		- TPBasic_STM32F405RGT6最小系统板		一块

		- 杜邦线					若干根
		
		- 按键					两个

		- W25Q128					一片

	三、制作主要过程
-------------------------

	1、制作流程
----------------------

		PA9/PA10通过杜邦线连接在RXD/TXD上.
		按键KEY1(PA3)/KEY_UP(PA0,也称之为WK_UP)
		SPI1(PB3/4/5/14)
		W25Q128(SPI FLASH芯片,连接在SPI1上)
		

	2、主要代码
----------------------

	code-block::

		#include "sys.h"
		#include "delay.h"
		#include "usart.h"
		#include "led.h"
		#include "adc.h"
		#include "dac.h"
		#include "key.h"

		int main(void)
		{ 
			u16 adcx;
			float temp;
			u8 t=0;	 
			u16 dacval=0;
			u8 key;	
			NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);//设置系统中断优先级分组2
			delay_init(168);      //初始化延时函数
			uart_init(115200);		//初始化串口波特率为115200
			
			LED_Init();					//初始化LED 
			Adc_Init(); 				//adc初始化
			KEY_Init(); 				//按键初始化
			Dac1_Init();		 		//DAC通道1初始化	
			DAC_SetChannel1Data(DAC_Align_12b_R,dacval);//初始值为0	
			while(1)
			{
				t++;
				key=KEY_Scan(0);			  
				if(key==WKUP_PRES)
				{		 
					if(dacval<4000)dacval+=200;
					DAC_SetChannel1Data(DAC_Align_12b_R, dacval);//设置DAC值
				}else if(key==2)	
				{
					if(dacval>200)dacval-=200;
					else dacval=0;
					DAC_SetChannel1Data(DAC_Align_12b_R, dacval);//设置DAC值
				}	 
				if(t==10||key==KEY1_PRES||key==WKUP_PRES) 	//WKUP/KEY1按下了,或者定时时间到了
				{	  
					adcx=DAC_GetDataOutputValue(DAC_Channel_1);//读取前面设置DAC的值
					adcx=Get_Adc_Average(ADC_Channel_5,10);		//得到ADC转换值	  
					temp=(float)adcx*(3.3/4096);			        //得到ADC电压值
					adcx=temp;
					printf("%5.0",temp);     	  //显示电压值整数部分
					temp-=adcx;
					temp*=1000;
					printf(".%0.3d",temp); 	  //显示电压值的小数部分
					t=0;
				}	    
				delay_ms(10);	 
			}	
		}

