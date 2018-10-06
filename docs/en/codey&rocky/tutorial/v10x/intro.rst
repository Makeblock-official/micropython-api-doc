[Micropython]TPYBoard v10x 模拟红绿灯教程
===========================


实验目的
----------------------

- 学习在PC机系统中扩展简单I/O 接口的方法
- 进一步学习编制数据输出程序的设计方法
- 学习模拟交通灯控制的方法

所需器件
---------------------

- 1位共阴红色LED数码管(SM42056) 1个
- TPYBoard v102开发板 1块
- 红、绿、黄LED灯 各1个
- micro USB数据线 1条
- 220欧直插电阻 1个
- 杜邦线 若干
- 面包板 1块


点亮LED灯
---------------------------

1.将三个LED灯插在面包板上，LED负极插入面包板的负极（横向插孔），正极插入面包板的纵向插孔。
2.将222欧电阻插入面包板的负极上（横向插孔）和纵向插孔中，将LED灯的正极分别与TPYBoard v102的引脚连接。
3.将红、黄、绿3个LED灯的正极依次通过杜邦线连接到TPYBoard v102的Y1,、Y2、Y3的引脚上，然后将电阻纵向插孔用杜邦线接到TPYBoard v102的GND引脚。
4.在main.py文件中将Y1、Y2、Y3引脚的电平拉高，即可看到三个灯同时亮起来。

main.py 内容如下：
::
    # main.py -- put your code here!
    import pyb
    led1 = pyb.Pin("Y1",pyb.Pin.OUT_PP)
    led2 = pyb.Pin("Y2",pyb.Pin.OUT_PP)
    led3 = pyb.Pin("Y3",pyb.Pin.OUT_PP)
    While True:
        led1.value(1)
        led2.value(1)
        led3.value(1)

效果如图:

  .. image:: ../img/test_11.png

点亮数码管
------------------------------------
数码管是一种半导体发光器件，其基本单元是发光二极管。数码管按段数可分为七段数码管和八段数码管，八段比七段多一个发光二极管单元，也就是多一个小数点（DP）；按能显示可分为1位、2位、3位、4位、5位、6位、7位等数码管。 按使用类型可分为共阴数码管和共阳数码管。
数码管针脚图如下：

  .. image:: ../img/test_12.png

**共阴数码管**
共阴数码管是指将所有发光二极管的阴极接到一起形成公共阴极(COM)的数码管，在使用时公共端应接到地线GND上；若想点亮a段发光二极管，那么就把对应的a针脚设置为高电平，反之设置为低电平。

**共阳数码管**
共阳数码管是指将所有发光二极管的阳极接到一起形成公共阳极(COM)的数码管，在使用时公共端应接到3.3V~5V上，若想点亮a段发光二极管，那么就把对应的a针脚设置为低电平，反之设置为高电平。

具体接线方式如下表：

+--------------+--------+
| TPYBoardv10x | 数码管 |
+==============+========+
| X1           | a      |
+--------------+--------+
| X2           | b      |
+--------------+--------+
| X3           | c      |
+--------------+--------+
| X4           | d      |
+--------------+--------+
| X5           | e      |
+--------------+--------+
| X6           | f      |
+--------------+--------+
| X7           | g      |
+--------------+--------+
| 3V3          | COM    |
+--------------+--------+

*注意：因为我们用的是共阳数码管，所以公共端（COM）应接开发板的VIN（3V3），点亮需置低电平。本次实验没有用到小数点，故dp针脚悬空无需接线。*

定义7个引脚用于控制数码管中a~g段的发光二极管。
::

    #数码管a~g对应的开发板引脚X1~X7
    d_Pins=[Pin(i,Pin.OUT_PP) for i in ['X1','X2','X3','X4','X5','X6','X7']]


列举一下数码管要显示0~9之间的数，对应的每个针脚的高低电平的状态，便于程序的编写，如下图：

  .. image:: ../img/test_00.png

根据上面的对应关系表，我们新建一个列表number，用来存放显示每个数字时，7个引脚应设置的电平值。

.. code-block:: python

    number=[
    [0,0,0,0,0,0,1],#0
    [1,1,1,1,0,0,1],#1
    [0,0,1,0,0,1,0],#2
    [0,0,0,0,1,1,0],#3
    [1,0,0,1,1,0,0],#4
    [0,1,0,0,1,0,0],#5
    [0,1,0,0,0,0,0],#6
    [0,0,0,1,1,1,1],#7
    [0,0,0,0,0,0,0],#8
    [0,0,0,0,1,0,0],#9
    ]

添加一个函数display用于控制数码管显示数字，参数是要显示的数字。

.. code-block:: python

    def display(num):
      global number
      count=0
      for pin in d_Pins:#X1~X7分别设置电平值 动态显示num的值
        pin.value(number[num][count])
        count+=1

模拟红绿灯
------------------------------------

我们按照上面的步骤做完以后，然后通过准备的数据线给TPYBoard v102通电。

main.py 内容如下：

.. code-block:: python

    # main.py -- put your code here!
    import pyb
    from pyb import Pin
      
    r_LED=Pin('Y1',Pin.OUT_PP)#red
    y_LED=Pin('Y2',Pin.OUT_PP)#yellow
    g_LED=Pin('Y3',Pin.OUT_PP)#green
      
    #数码管a~g对应的开发板引脚X1~X7
    d_Pins=[Pin(i,Pin.OUT_PP) for i in ['X1','X2','X3','X4','X5','X6','X7']]
      
    number=[
    [0,0,0,0,0,0,1],#0
    [1,1,1,1,0,0,1],#1
    [0,0,1,0,0,1,0],#2
    [0,0,0,0,1,1,0],#3
    [1,0,0,1,1,0,0],#4
    [0,1,0,0,1,0,0],#5
    [0,1,0,0,0,0,0],#6
    [0,0,0,1,1,1,1],#7
    [0,0,0,0,0,0,0],#8
    [0,0,0,0,1,0,0],#9
    ]
      
    def display(num):
        global number
        count=0
        for pin in d_Pins:#X1~X7分别设置电平值 动态显示num的值
            pin.value(number[num][count])
            count+=1
      
    if __name__=='__main__':
        while True:
            #红灯亮10秒
            r_LED.value(1)
            for i in range(0,10):
                display(9-i)
                pyb.delay(1000)#1s
            r_LED.value(0)
            #黄灯亮3秒
            y_LED.value(1)
            for i in range(0,3):
                display(2-i)
                pyb.delay(1000)#1s
            y_LED.value(0)
            #绿灯亮10秒
            g_LED.value(1)
            for i in range(0,10):
                display(9-i)
                pyb.delay(1000)#1s
            g_LED.value(0)


效果演示
------------------------------------
    
效果图:

  .. image:: ../img/test_13.png


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v10x-master>`_
