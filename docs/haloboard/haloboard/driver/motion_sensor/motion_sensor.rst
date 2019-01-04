:mod:`motion_sensor` --- 板载姿态传感器模块
=============================================

.. module:: motion_sensor
    :synopsis: 板载姿态传感器模块，实现反馈haloboard的姿态.

``motion_sensor`` 模块的主要功能与函数

板载姿态传感器模块说明：
  .. image:: img/1.png

如上图所示，roll，pitch（翻滚角，俯仰角）的方向以右手螺旋定则为标准。
光环板水平放置时roll和pitch都为0°
  - *roll* 的范围：-90° ~ 90°
  - *pitch* 的范围：-180° ~ 180°

功能相关函数
----------------------

.. function:: get_roll()

  获取姿态角的翻滚角，返回的数据范围是 -90 ~ 90

.. function:: get_pitch()

  获取姿态角的俯仰角，返回的数据范围是 -180 ~ 180

.. function:: get_yaw()

  获取姿态角的偏航角，返回的数据范围是0 ~ 360，由于没有电子罗盘,所以实际上偏航角只是使用了Z轴角速
  度的积分。它存在着积累误差。如果是想获得真实偏航角的，这个API不适合使用。

.. function:: get_acceleration(axis)

  获取三个轴的加速度值，单位是 m/s^2，参数：
- *axis* 字符串类型，以 x，y，z 代表光环板定义的坐标轴。

.. function:: get_gyroscope(axis)

  获取三个轴的角速度值，单位是 °/秒，参数
- *axis* 字符串类型，以 x，y，z 代表光环板定义的坐标轴。

.. function:: get_rotation(axis)

  获得光环板在三个轴上转动的角度，以逆时针转动方向为正方向，参数：
- *axis* 字符串类型，以 x，y，z 代表光环板定义的坐标轴。

.. function:: reset_rotation(axis = "all")

  初始化绕三个轴转动的当前角度为0，get_rotation() 函数将从 0 开始计算，参数：
- *axis* 字符串类型，以 x，y，z 代表光环板定义的坐标轴, all 代表全部的三个轴。也是这个函数的默认
  值。

.. function:: is_tilted_left()

  检测光环板是否向左倾斜，阈值15°，返回值是布尔值，其中 True 表示光环板向左倾斜了，False 表示光环板
  未向左倾斜。

.. function:: is_tilted_right()

  检测光环板是否向右倾斜，阈值15°，返回值是布尔值，其中 True 表示光环板向右倾斜了，False 表示光环板
  未向右倾斜。

.. function:: is_arrow_up()

  获取是否箭头是否朝上状态，阈值15°，返回值是布尔值，其中 True 表示箭头朝上，False 表示箭头没有朝
  上。

.. function:: is_arrow_down()

  获取是否箭头是否朝上状态，阈值15°,返回值是布尔值，其中 True 表示箭头朝下，False 表示箭头没有朝下。

.. function:: is_shaked()

  检测光环板是否有被摇晃，返回值是布尔值，其中 True 表示光环板被晃动了，False 表示光环板未被晃动。

.. function:: is_led_ring_up()

  检测LED灯环是否朝上状态，返回布尔值，其中True表示灯环朝上，False表示灯环未朝上。

.. function:: is_led_ring_down()

  检测LED灯环是否朝下状态，返回布尔值，其中True表示灯环朝下，False表示灯环未朝下。

.. function:: get_shake_strength()

  如果光环板被摇晃了，这个函数可以获得摇晃的强度，返回值的数值范围是 0 ~ 100， 数值越大，晃动的强度
  就越大。

程序示例一：
----------------------

.. code-block:: python

  import haloboard
  import time

  while True:
      acceleration_x = haloboard.motion_sensor.get_acceleration("x")
      acceleration_y = haloboard.motion_sensor.get_acceleration("y")
      acceleration_z = haloboard.motion_sensor.get_acceleration("z")
      print("acceleration_x:", end = "")
      print(acceleration_x, end = "")
      print("   ,acceleration_y:", end = "")
      print(acceleration_y, end = "")
      print("   ,acceleration_z:", end = "")
      print(acceleration_z)
      time.sleep(0.05)

程序示例二：
----------------------

.. code-block:: python

  import haloboard
  import time

  while True:
      roll = haloboard.motion_sensor.get_roll()
      pitch = haloboard.motion_sensor.get_pitch()
      yaw = haloboard.motion_sensor.get_yaw()
      print("roll:", end = "")
      print(roll, end = "")
      print("   ,pitch:", end = "")
      print(pitch, end = "")
      print("   ,yaw:", end = "")
      print(yaw)
      time.sleep(0.05)

程序示例三：
----------------------

.. code-block:: python

  import haloboard
  import time

  while True:
      gyroscope_x = haloboard.motion_sensor.get_gyroscope("x")
      gyroscope_y = haloboard.motion_sensor.get_gyroscope("y")
      gyroscope_z = haloboard.motion_sensor.get_gyroscope("z")
      print("gyroscope_x:", end = "")
      print(gyroscope_x, end = "")
      print("   ,gyroscope_y:", end = "")
      print(gyroscope_y, end = "")
      print("   ,gyroscope_z:", end = "")
      print(gyroscope_z)
      time.sleep(0.05)

程序示例四：
----------------------

.. code-block:: python

  import haloboard
  import time

  while True:
      if haloboard.motion_sensor.is_tilted_left():
          print("tilted_left")
      if haloboard.motion_sensor.is_tilted_right():
          print("tilted_right")
      if haloboard.motion_sensor.is_arrow_up():
          print("arrow_up")
      if haloboard.motion_sensor.is_arrow_down():
          print("arrow_down")

程序示例五：
----------------------

.. code-block:: python

  import haloboard
  import time

  while True:
      rotation_x = haloboard.motion_sensor.get_rotation("x")
      rotation_y = haloboard.motion_sensor.get_rotation("y")
      rotation_z = haloboard.motion_sensor.get_rotation("z")
      print("rotation_x:", end = "")
      print(rotation_x, end = "")
      print("   ,rotation_y:", end = "")
      print(rotation_y, end = "")
      print("   ,rotation_z:", end = "")
      print(rotation_z)
      time.sleep(0.05)

程序示例六：
----------------------

.. code-block:: python

  import haloboard
  import time

  while True:
      if haloboard.motion_sensor.is_shaked():
          print("shake_strength:", end = "")
          print(haloboard.motion_sensor.get_shake_strength())

程序示例七：
----------------------

.. code-block:: python

  import haloboard
  import time

  while True:
      if haloboard.motion_sensor.is_led_ring_up():
          print("led ring up")
      if haloboard.motion_sensor.is_led_ring_down():
          print("led ring down")

      time.sleep(0.3)