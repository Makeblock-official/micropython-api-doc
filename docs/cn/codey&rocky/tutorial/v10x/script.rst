[Micropython]TPYBoard v10x 驱动LCD5110显示6x8字符
==================================================


实验目的
----------------------

  - 学习LCD5110的使用方法

  - 了解SPI接口的使用方法


所需器件
---------------------

  - TPYBoard v10X开发板 1块

  - LCD5110显示屏 1个

  - micro USB数据线 1条

  - 杜邦线 若干


LCD5110显示屏的针脚含义
---------------------------

  - **RST**:复位
  - **CE** :片选
  - **DC** :数据/指令选择
  - **DIN**:串行数据线
  - **CLK**:串行时钟线
  - **VCC**:电源输入（3.3v和5v均可）
  - **BL** :背光控制端
  - **GND**:地线


驱动LCD5110显示屏
------------------------------------

  TPYBoard v10x的针脚与LCD5110的针脚对应关系如下:

  .. image:: ../img/test_21.png


  main.py 内容如下::

    # main.py -- put your code here!
    import pyb
    import upcd8544
    from machine import SPI,Pin

    def main():
        SPI    = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
        #DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
        #CLK =>SPI(1).SCK  'X6' SPI clock

        RST    = pyb.Pin('Y10')
        CE     = pyb.Pin('Y11')
        DC     = pyb.Pin('Y9')
        LIGHT  = pyb.Pin('Y12')
        lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)

        lcd_5110.lcd_write_string('Hello Python!',0,0)
        lcd_5110.lcd_write_string('Micropython',6,1)
        lcd_5110.lcd_write_string('TPYBoard',12,2)
        lcd_5110.lcd_write_string('v102',60,3)
        lcd_5110.lcd_write_string('This is a test of LCD5110',0,4)
    if __name__ == '__main__':
        main()

  效果图:

  .. image:: ../img/test_22.png


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v10x-master>`_
