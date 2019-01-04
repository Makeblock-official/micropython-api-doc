:mod:`pin1` --- pin口1
=============================================

.. module:: pin1
    :synopsis: pin口1

``pin1`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: is_touched()

   获取pin口当前状态。返回的结果是True：pin口被触摸，或者False：pin口未被触摸。

.. function:: get_touchpad_value()

   获取pin口被触摸的值。数值范围为0-10000。

.. function:: set_touchpad_threshold(val)

   设置pin口触摸触发阈值，参数：
- *val* 变化的百分比，检测到变化的幅值大于该百分比时认为被触摸，数值为0.0-1。

.. function:: read_digital()

   获取pin口数字输入，值为0或1。

.. function:: write_digital(val)

   设置pin口数字输出，参数：
- *val* 数字输出值为0或1。

.. function:: write_analog(val)

   设置模拟输出（pwm），参数：
- *val* 模拟输出值，数值范围为0-1023。

.. function:: read_analog()

   获取模拟输入值（pwm）。数值范围为0-3300，单位为mv。

.. function:: servo_write(val)

   设置舵机转动的角度，参数：
- *val* 舵机转动的角度，或者舵机控制脉冲的高电平的维持时间，数值为0-19999。
  当数值小于544 的时候，输入数据如果小于0，会转换为0，如果大于180会转化为180，代表设置
  的是模拟舵机的转动角度；
  当数值大于或等于544时，表示设置的是50Hz PWM波的高电平的时间宽度(单位是 us)，所以最大
  值是 19999， 将近20ms，如果大于19999的，则转化为19999。

.. function:: analog_set_frequency(frequency)

   设置pin模拟输出（pwm）频率，参数：
- *frequency* PWM频率值，数值范围为0-5000

程序示例一：
----------------------

.. code-block:: python

  import haloboard
  import event

  @event.start
  def on_start():
      global results
      if haloboard.pin1.is_touched():
          haloboard.led.show_all(126, 211, 33)

程序示例二：
----------------------

.. code-block:: python

  import haloboard
  import event

  PIN_MODE_TOUCH            = 1
  PIN_MODE_READ_DIGITAL     = 2
  PIN_MODE_WRITE_DIGITAL    = 3
  PIN_MODE_WRITE_ANALOG     = 4
  PIN_MODE_READ_ANALOG      = 5
  PIN_MODE_WRITE_SERVO      = 6

  pin_mode = PIN_MODE_TOUCH
  pin_index = 0

  @event.button_pressed
  def on_button_pressed():
      global pin_mode, pin_index
      pin_index = (pin_index + 1) % 10

      if pin_index % 2 == 0:
          pin_mode = PIN_MODE_TOUCH
          print("*****", "in tp mode")
      elif pin_index == 1:
          pin_mode = PIN_MODE_WRITE_ANALOG
          print("*****", "in write analog mode")
      elif pin_index == 3:
          pin_mode = PIN_MODE_READ_DIGITAL
          print("*****", "in read digital mode")
      elif pin_index == 5:
          pin_mode = PIN_MODE_WRITE_DIGITAL
          print("*****", "in write digital mode")
      elif pin_index == 7:
          pin_mode = PIN_MODE_READ_ANALOG
          print("*****", "in read analog mode")

      elif pin_index == 9:
          pin_mode = PIN_MODE_WRITE_SERVO
          print("*****", "in servo mode")

      print("pin mode is: " + str(pin_mode))

  @event.start
  def on_start():
      global pin_mode
      while True:
          if pin_mode == PIN_MODE_TOUCH:
              time.sleep(0.1)
              if haloboard.pin0.is_touched():
                  print("pin0 is touched")
              if haloboard.pin1.is_touched():
                  print("pin1 is touched")
              if haloboard.pin2.is_touched():
                  print("pin2 is touched")
              if haloboard.pin3.is_touched():
                  print("pin3 is touched")
          if pin_mode == PIN_MODE_READ_DIGITAL:
              print("pin0:", end = "")
              print(haloboard.pin0.read_digital(), end = "")
              print(" ,pin1:", end = "")
              print(haloboard.pin1.read_digital(), end = "")
              print(" ,pin2:", end = "")
              print(haloboard.pin2.read_digital(), end = "")
              print(" ,pin3:", end = "")
              print(haloboard.pin3.read_digital())
              time.sleep(1)
          if pin_mode == PIN_MODE_WRITE_DIGITAL:
              print("write_digital HIGH")
              haloboard.pin0.write_digital(1)
              haloboard.pin1.write_digital(1)
              haloboard.pin2.write_digital(1)
              haloboard.pin3.write_digital(1)
              time.sleep(1)
              print("write_digital LOW")
              haloboard.pin0.write_digital(0)
              haloboard.pin1.write_digital(0)
              haloboard.pin2.write_digital(0)
              haloboard.pin3.write_digital(0)
              time.sleep(1)
          if pin_mode == PIN_MODE_WRITE_ANALOG:
              print("write_analog 512")
              haloboard.pin0.write_analog(512)
              haloboard.pin1.write_analog(512)
              haloboard.pin2.write_analog(512)
              haloboard.pin3.write_analog(512)
              time.sleep(1)

          if pin_mode == PIN_MODE_WRITE_SERVO:
              print("write_servo 150")
              haloboard.pin2.servo_write(150)
              haloboard.pin3.servo_write(150)
              time.sleep(2)
              print("write_servo 10000")
              haloboard.pin2.servo_write(10000)
              haloboard.pin3.servo_write(10000)
              time.sleep(2)

          if pin_mode == PIN_MODE_READ_ANALOG:
              print("pin2:", end = "")
              print(haloboard.pin2.read_analog(), end = "")
              print("pin3:", end = "")
              print(haloboard.pin3.read_analog())
              time.sleep(1)

程序示例三：
----------------------

.. code-block:: python

  import haloboard
  import event

  pin_mode = 0

  @event.button_pressed
  def on_button_pressed():
      global pin_mode
      pin_mode = pin_mode + 1
      print("pin mode is: " + str(pin_mode))

  @event.start
  def on_start():
      global pin_mode
      while True:
          pin_mode %= 8
          if pin_mode < 4:
              if pin_mode == 0:
                  print("pin write servo 0")
                  haloboard.pin0.servo_write(0)
              elif pin_mode == 1:
                  print("pin write servo 90")
                  haloboard.pin0.servo_write(90)
              elif pin_mode == 2:
                  print("pin write servo 120")
                  haloboard.pin0.servo_write(120)
              elif pin_mode == 3:
                  print("pin write servo 180")
                  haloboard.pin0.servo_write(180)

程序示例四：
----------------------

.. code-block:: python

  import haloboard
  import event

  PIN_MODE_TOUCH            = 1
  PIN_MODE_READ_DIGITAL     = 2
  PIN_MODE_WRITE_DIGITAL    = 3
  PIN_MODE_WRITE_ANALOG     = 4
  PIN_MODE_READ_ANALOG      = 5

  pin_mode = PIN_MODE_TOUCH

  @event.button_pressed
  def on_button_pressed():
      global pin_mode
      pin_mode = pin_mode + 1
      if pin_mode > PIN_MODE_READ_ANALOG:
          pin_mode = PIN_MODE_TOUCH

      print("pin mode is: " + str(pin_mode))

  @event.start
  def on_start():
      global pin_mode
      while True:
          if pin_mode == PIN_MODE_TOUCH:
              if haloboard.pin0.is_touched():
                  print("pin0 is touched")
              if haloboard.pin1.is_touched():
                  print("pin1 is touched")
              if haloboard.pin2.is_touched():
                  print("pin2 is touched")
              if haloboard.pin3.is_touched():
                  print("pin3 is touched")
          if pin_mode == PIN_MODE_READ_DIGITAL:
              print("pin0:", end = "")
              print(haloboard.pin0.read_digital(), end = "")
              print(" ,pin1:", end = "")
              print(haloboard.pin1.read_digital(), end = "")
              print(" ,pin2:", end = "")
              print(haloboard.pin2.read_digital(), end = "")
              print(" ,pin3:", end = "")
              print(haloboard.pin3.read_digital())
              time.sleep(1)
          if pin_mode == PIN_MODE_WRITE_DIGITAL:
              print("write_digital HIGH")
              haloboard.pin0.write_digital(1)
              haloboard.pin1.write_digital(1)
              haloboard.pin2.write_digital(1)
              haloboard.pin3.write_digital(1)
              time.sleep(1)
              print("write_digital LOW")
              haloboard.pin0.write_digital(0)
              haloboard.pin1.write_digital(0)
              haloboard.pin2.write_digital(0)
              haloboard.pin3.write_digital(0)
              time.sleep(1)
          if pin_mode == PIN_MODE_WRITE_ANALOG:
              print("write_analog 512")
              haloboard.pin0.write_analog(512)
              haloboard.pin1.write_analog(512)
              haloboard.pin2.write_analog(512)
              haloboard.pin3.write_analog(512)
              time.sleep(1)
          if pin_mode == PIN_MODE_READ_ANALOG:
              print("pin2:", end = "")
              print(haloboard.pin2.read_analog(), end = "")
              print("pin3:", end = "")
              print(haloboard.pin3.read_analog())
              time.sleep(1)
