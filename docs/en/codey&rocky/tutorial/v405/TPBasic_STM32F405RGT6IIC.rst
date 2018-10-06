TPBasic_STM32F405RGT6的IIC使用
===========================================

	一、什么是TPBasic_STM32F405RGT6最小系统板
----------------------------------------------------------

		TPBasic_STM32F405RGT6最小系统板是基于STM32F405RGT6芯片开发制作的最小系统板，方便开发与集成使用。

	二、利用TPBasic_STM32F405RGT6最小系统板完成24C02的读写操作
------------------------------------------------------------

	1、具体要求
----------------------

		按键KEY0接在PC0上/按键KEY1接在PC1
		
		24C02(IIC连接在PB8/PB9上面)
		
		通过KEY1按键来控制24C02的写入，通过另外一个按键KEY0来控制24C02的读取。

	2、所需器件
------------------------

		- TPBasic_STM32F405RGT6最小系统板		一块

		- 杜邦线					若干根

		- USB转TTL串口转换模块					一块


	三、制作主要过程
----------------------------------

	1、制作流程
----------------------

		按键KEY0接在PC0上/按键KEY1接在PC1

		通过KEY1按键来控制24C02的写入，通过另外一个按键KEY0来控制24C02的读取。

	2、主要代码
----------------------

	.. code-block:: c
		  
		#include "sys.h"
		#include "delay.h"
		#include "usart.h"
		#include "24cxx.h"
		#include "key.h"  
		  
		//要写入到24c02的字符串数组
		const u8 TEXT_Buffer[]={"Explorer STM32F4 IIC TEST"};
		#define SIZE sizeof(TEXT_Buffer)	 
			
		int main(void)
		{ 
			u8 key;
			u16 i=0;
			u8 datatemp[SIZE];	
			NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);//设置系统中断优先级分组2
			delay_init(168);    //初始化延时函数
			uart_init(115200);	//初始化串口波特率为115200
			KEY_Init(); 				//按键初始化  
			AT24CXX_Init();			//IIC初始化 
			while(1)
			{
				key=KEY_Scan(0);
				if(key==KEY1_PRES)//KEY1按下,写入24C02
				{
					AT24CXX_Write(0,(u8*)TEXT_Buffer,SIZE);
				}
				if(key==KEY0_PRES)//KEY0按下,读取字符串
				{
					AT24CXX_Read(0,datatemp,SIZE);
				}
				i++;
				delay_ms(10);
				if(i==20)
				{
					LED0=!LED0;//提示系统正在运行	
					i=0;
				}		   
			} 	    
		}
