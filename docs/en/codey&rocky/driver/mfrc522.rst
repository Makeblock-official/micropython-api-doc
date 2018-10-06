:mod:`mfrc522` --- 射频卡关联功能函数
=============================================

.. module:: mfrc522
   :synopsis: 射频卡关联功能函数

``mfrc522`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: SeekCard(order)

   寻卡函数，搜索范围内指定的卡或者所有的卡，参数为0x26（未休眠的卡）或0x52（所有的卡）。
   返回值为：读卡状态，卡的类型

.. function:: Anticoll()

   读卡函数，读出卡ID号。
   返回值为：读卡状态，卡的ID

.. function:: init_spi(SPI,RC522_RST,RC522_SDA)

   MFRC522初始化函数，参数为SPI号，RST引脚，SDA引脚

MFRC522与开发板接线对应引脚：
------------------------------------

		+------------+---------+
		| TPYBoard   | MFRC522 |
		+============+=========+
		| X4         | SDA     |
		+------------+---------+
		| X6         | SCK     |
		+------------+---------+
		| X8         | MOSI    |
		+------------+---------+
		| X7         | MISO    |
		+------------+---------+
		| GND        | GND     |
		+------------+---------+
		| X2         | RST     |
		+------------+---------+
		| 3.3V       | 3V3     |
		+------------+---------+

程序示例：
------------

.. code-block:: python

  import pyb
  import mfrc522
  from machine import SPI,Pin

  def main():
  	SPI=pyb.SPI(1)                              #这里用的SPI1
  	RC522_SDA='X4'
  	RC522_RST='X2'
  	rc52=rc522.MFRC522()
  	rc52.init_spi(SPI,RC522_RST,RC522_SDA)      #设置rc522功能引脚
  	while True:
  		(status,backBits)=rc52.SeekCard(0x52)   #寻找区范围内所有能识别的卡
  		if(status==0):                          #判断是否找到卡
  			(status,id,)=rc52.Anticoll()        #读出卡ID号
  			print("card_id=",id)                #打印卡号
  		else :
  			print("NO_CARD")
  		pyb.delay(1000)
  main()