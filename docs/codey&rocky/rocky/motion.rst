:mod:`motion` --- Rocky Chassis Movement
=============================================

.. module:: rocky
    :synopsis: Rocky Chassis Movement

The main functionality and function of the ``motion`` module (you do not need to bring the module name when using due to it is a system function)

Function
----------------------

.. function:: stop()

   Rocky stops moving.

.. function:: forward(speed, t = None, straight = False)

   Rocky moves forward, parameters：

    - *speed* The value of motion speed, parameter range is ``-100 ~ 100``, negative numbers represent backwards, positive numbers represent forward.
    - *t* The value of the motion time, in ``seconds``, the parameter range is ``0 ~ the value range limit``. If set to 1, it means the rocky will move forward for 1s. If this parameter is not set, the forward state is maintained until there is the motion stop command or new motion command.
    - *straight* Enable the gyro sensor to correct the forward direction or not. If this parameter is not set, it is not enabled by default.

.. function:: backward(speed, t = None, straight = False)

   Rocky moves backward, parameters：

    - *speed* The value of motion speed, parameter range is ``-100 ~ 100``, negative numbers represent forward, positive numbers represent backward.
    - *t* The value of the motion time, in ``seconds``, the parameter range is ``0 ~ the value range limit``. If set to 1, it means the rocky will move backward for 1s. If this parameter is not set, the backward state is maintained until there is the motion stop command or new motion command.
    - *straight* Enable the gyro sensor to correct the backward direction or not. If this parameter is not set, it is not enabled by default.

.. function:: turn_left(speed, t = None)

   Rocky turns left, parameters：

    - *speed* The value of turn speed, parameter range is ``-100 ~ 100``, negative numbers represent turn right, positive numbers represent turn left.
    - *t* The value of the motion time, in ``seconds``, the parameter range is ``0 ~ the value range limit``. If set to 1, it means the rocky will turn left for 1s. If this parameter is not set, the turn left state is maintained until there is the motion stop command or new motion command.

.. function:: turn_right(speed, t = None)

   Rocky turns right, parameters：

   - *speed* The value of turn speed, parameter range is ``-100 ~ 100``, negative numbers represent turn left, positive numbers represent turn right.
   - *t* The value of the motion time, in seconds, the parameter range is ``0 ~ the value range limit``. If set to 1, it means the rocky will turn right for 1s. If this parameter is not set, the turn right state is maintained until there is the motion stop command or new motion command.

.. function:: drive(left_power, right_power)

   Rocky turns according to the set value for each motor, parameters：

    - *left_power* Motor speed of left wheel, parameter range is ``-100 ~ 100``, negative numbers represent the left wheel rotates backward, positive numbers represent the left wheel rotates forward.
    - *right_power* Motor speed of right wheel, parameter range is ``-100 ~ 100``, negative numbers represent the right wheel rotates backward, positive numbers represent the right wheel rotates forward.

.. function:: turn_right_by_degree(angle, speed = 40)

   Rocky turns right according to the set degree, parameters：

    - *angle* Angle of rotation, negative numbers represent turn left, positive numbers represent turn right.
    - *speed* Turning speed, parameter range is ``0 ~ 100``, if this parameter is not set, the default speed is 40. (Since the gyro sensor is used for turning specific angle, it is recommended not to modify the speed to avoid the turning angle being inaccurate).

.. function:: turn_left_by_degree(angle, speed = 40)

   Rocky turns left according to the set degree, parameters：

    - *angle* Angle of rotation, negative numbers represent turn right, positive numbers represent turn left.
    - *speed* Turning speed, parameter range is ``0 ~ 100``, if this parameter is not set, the default speed is 40. (Since the gyro sensor is used for turning specific angle, it is recommended not to modify the speed to avoid the turning angle being inaccurate).

Sample Code：
------------

.. code-block:: python

  import codey
  import rocky
  import time
  
  rocky.forward(50, 1)
  rocky.stop()
  rocky.backward(50, 1)
  rocky.turn_left(50, 1)
  rocky.turn_right(50, 1)
  rocky.drive(50, 80)
  time.sleep(2)
  while True:
      rocky.turn_right_by_degree(80, 40)
      rocky.turn_right_by_degree(80, 20)