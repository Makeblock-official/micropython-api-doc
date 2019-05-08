:mod:`smartservo` --- 智能舵机
=============================================

.. module:: smartservo
    :synopsis: 智能舵机

``smartservo`` 模块的主要功能与函数

智能舵机说明
----------------------

mbuild模块的智能舵机模块如下图所示：

.. image:: ../img/smartservo.png


功能相关函数
----------------------

.. function:: set_zero()

   设置当前位置为零点。

.. function:: move_to(position, speed)

   按指定转速移动到绝对角度，参数：

    - *position* 目标角度，单位为度，范围 ``-2147483648~2147483647``
    - *speed* 转速，单位为rpm/min，范围 ``1~50``

.. function:: move(position, speed)

   按指定转速移动到相对角度，参数：

    - *position* 目标角度，单位为度，范围 ``-2147483648~2147483647``
    - *speed* 转速，单位为rpm/min，范围 ``1~50``

.. function:: set_power(pwm)

   设置电机以指定动力转动，开环控制，参数：

    - *pwm* 转速，单位为 ``无``，范围 ``-100~100``。

.. function:: get_value(type)

   获取电机数据，参数：

    - *type* 获取数据类型，字符串类型，参数可以选择为：

      "current"：电流，单位A

      "voltage"：电压，单位V

      "speed"：速度，单位rpm/min

      "angle"：角度，单位度

      "temperature"：温度，单位摄氏度

程序示例1：
----------------------

.. code-block:: python

  import novapi
  from mbuild.smartservo import smartservo_class

  #先初始化，定义智能舵机接在M1口的第1个
  __smartservo_1 = smartservo_class("M1", "INDEX1")

  while True:
      __smartservo_1.set_zero()
      time.sleep(0.1)

      __smartservo_1.move_to(360, 20)
      time.sleep(4)
      position = __smartservo_1.get_value("angle")
      print("position: " ,position)

      __smartservo_1.move(-360, 20)
      time.sleep(4)
      position = __smartservo_1.get_value("angle")
      print("position: ",position)

      __smartservo_1.set_power(50)
      time.sleep(1)

      param0 = __smartservo_1.get_value("current")
      print("current: " ,param0)

      param1 = __smartservo_1.get_value("voltage")
      print("voltage: " ,param1)

      param2 = __smartservo_1.get_value("speed")
      print("speed: " ,param2)

      param3 = __smartservo_1.get_value("angle")
      print("angle: " ,param3)

      param4 = __smartservo_1.get_value("temperature")
      print("temperature: ", param4)