:mod:`microphone` --- 板载麦克风
=============================================

.. module:: microphone
    :synopsis: 板载麦克风

``microphone`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: get_loudness(type)

  获取声音的响度，参数：
- *type* 字符串参数，一共有两个：average，获得一段时间内的响度平均值；maximum，获得一段时间内
  响度的最大值，为默认参数。返回值范围为0-100。

程序示例：
----------------------

.. code-block:: python

  import haloboard
  import time
  import event

  @event.start
  def on_start():
      while True:
          average = haloboard.microphone.get_loudness("average")
          maximum = haloboard.microphone.get_loudness("maximum")
          print("average:" + str(average), " ,maximum" + str(maximum))
          time.sleep(0.2)

  @event.greater_than(20, 'microphone')
  def on_greater_than():
      haloboard.led.show_all(10, 0, 0)
      time.sleep(0.2)
      haloboard.led.show_all(0, 0, 0)
