:mod:`AT24C0X` --- AT24C0X存储器关联功能函数
=============================================

.. module:: AT24C0X
   :synopsis: AT24C0X存储器关联功能函数

``AT24C0X`` 模块的主要功能与函数

功能相关函数
----------------------


.. function:: writeAT24C0x(self,addr,data)

   写入函数，输入参数addr为写入地址,data为写入数据

.. function:: readAT24C0x(self,add,bit_len)

   读取函数，输入参数addr为读取地址,bit_len为读取字节数

AT24C0X与开发板接线对应引脚：
-------------------------------

		+------------+---------+
		| TPYBoard   | AT24C0X |
		+============+=========+
		| 3V3        | VCC     |
		+------------+---------+
		| GND        | GND     |
		+------------+---------+
		| Y9         | SCL     |
		+------------+---------+
		| Y10        | SDA     |
		+------------+---------+

程序示例：
----------

.. code-block:: python

  # main.py -- put your code here!
  import at24c0x

  def main():
	at24c=at24c0x.AT24C(1)
	at24c.writeAT24C0x(0,'qxw')
	print(at24c.readAT24C0x(0,3))
	while True:
		a=0
  main()