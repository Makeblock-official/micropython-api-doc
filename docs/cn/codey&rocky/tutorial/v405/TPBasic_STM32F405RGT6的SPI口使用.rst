TPBasic_STM32F405RGT6的SPI口使用
==================================

	一、什么是TPBasic_STM32F405RGT6最小系统板
	-------------------------------------------------------

		TPBasic_STM32F405RGT6最小系统板是基于STM32F405RGT6芯片开发制作的最小系统板，方便开发与集成使用。
		

	二、利用TPBasic_STM32F405RGT6最小系统板利用按键控制W25Q128的写入和读取，并通过串口显示
--------------------------------------------------------------------------------------------------

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
			#include "lcd.h"
			#include "spi.h"
			#include "w25qxx.h"
			#include "key.h" 
			 
			const u8 TEXT_Buffer[]={"Explorer STM32F4 SPI TEST"};
			#define SIZE sizeof(TEXT_Buffer)	 
				
			int main(void)
			{ 
				u8 key;
				u16 i=0;
				u8 datatemp[SIZE];
				u32 FLASH_SIZE;
				NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);//设置系统中断优先级分组2
				delay_init(168);     //初始化延时函数
				uart_init(115200);	//初始化串口波特率为115200
				KEY_Init(); 				//按键初始化  
				W25QXX_Init();			//W25QXX初始化
				POINT_COLOR=RED; 
				while(W25QXX_ReadID()!=W25Q128)								//检测不到W25Q128
				{
					printf("W25Q128 Check Failed!\n");
					printf("Please Check!      \n");
				}
				printf("W25Q128 Ready!\n"); 
				FLASH_SIZE=16*1024*1024;	//FLASH 大小为16字节
				while(1)
				{
					key=KEY_Scan(0);
					if(key==KEY1_PRES)//KEY1按下,写入W25Q128
					{
						printf("Start Write W25Q128....\n");
						W25QXX_Write((u8*)TEXT_Buffer,FLASH_SIZE-100,SIZE);		//从倒数第100个地址处开始,写入SIZE长度的数据
						printf("W25Q128 Write Finished!"\n);	//提示传送完成
					}
					if(key==KEY0_PRES)//KEY0按下,读取字符串并显示
					{
						printf("Start Read W25Q128....\n");
						W25QXX_Read(datatemp,FLASH_SIZE-100,SIZE);					//从倒数第100个地址处开始,读出SIZE个字节
						printf("The Data Readed Is:   ");	//提示传送完成
						printf("%s"\n,datatemp);					//显示读到的字符串
					} 
					delay_ms(10);
				}       
			}

