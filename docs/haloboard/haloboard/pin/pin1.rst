:mod:`pin1` --- Pin Port 1
=============================================

.. module:: pin1
    :synopsis: Pin Port 1

``pin1`` The main functionality and functions of the module

Function
----------------------

.. function:: is_touched()

   Gets the current state of the pin port.The result is either "True": the pin is touched, or "False": the pin is not touched.

.. function:: get_touchpad_value()

   Gets the value of the pin that is touched. Values range from 0 to 10000.

.. function:: set_touchpad_threshold(val)

   Set the touch trigger threshold of pin, parameters:
- *val* - The percentage of change, when the detected amplitude of change is greater than this percentage, 
          it is considered to be touched, and the value is 0.0-1.

.. function:: read_digital()

   Get the pin port numeric input with a value of 0 or 1.

.. function:: write_digital(val)

   Set pin digital output, parameters:
- *val* - The digital output value is 0 or 1.

.. function:: write_analog(val)

   Set analog output (PWM), parameters:
- *val* - Analog output values, values range from 0 to 1023.

.. function:: read_analog()

   Gets the simulated input value (PWM).Values range from 0 to 3300 in mv.

.. function:: servo_write(val)

   Set servo rotation angle, parameters:
- *val* - The angle of rotation of the servo, or the high level maintenance time of the servo control pulse, the value is 0-19999.
          When the value is less than 544, if the input data is less than 0, it will be converted to 0, if it is greater than 180, it will be converted to 180, which represents the rotation angle of the simulated steering gear;
          When the value is greater than or equal to 544, it means that the time width (in us) of the high level of 50Hz PWM wave is set, so the maximum value is 19999, which is nearly 20ms. If it is greater than 19999, it will be converted to 19999.

.. function:: analog_set_frequency(frequency)

   Set pin analog output (PWM) frequency, parameters:
- *frequency* - PWM frequency value, value range 0-5000.

Sample Code 1：
----------------------

.. code-block:: python

  import haloboard
  import event

  @event.start
  def on_start():
      global results
      if haloboard.pin0.is_touched():
          haloboard.led.show_all(126, 211, 33)

Sample Code 2：
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

Sample Code 3：
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

Sample Code 4：
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
