:mod:`microphone` --- Onboard Microphone
=============================================

.. module:: microphone
    :synopsis: Onboard Microphone

``microphone`` The main functionality and functions of the module

Function
----------------------

.. function:: get_loudness(type)

  Get the loudness of sound, parameter:
- *type* - String parameter, a total of two: average, obtain the average loudness in a period of time;Maximum, the maximum loudness over a period of time,
           is the default parameter.The return values range from 0 to 100.

Sample Code：
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
