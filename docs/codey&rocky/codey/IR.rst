:mod:`ir` --- Onboard Infrared Transceiver
=============================================

.. module:: ir
    :synopsis: Onboard Infrared Transceiver

The main functionality and function of the ``ir`` module

Function
----------------------

.. function:: receive()

   Returns the string information received by the infrared receiver, so the data sent by the infrared sender must end with ``\n``. If it is a remote control command that receives the NEC encoding protocol, use another function ``receive_remote_code()``.

.. function:: receive_remote_code()

   Get the date from infrared remote controller. The data contains two parts: address and content, so it returns a list data which length 2. The first parameter is the address code, and the latter parameter is the data code.

.. function:: send(str)

   Send infrared string, parameters：

    - *str* The string data to be emitted, the function ``send`` will add the ``\n`` terminator at the end of the string automatically.

.. function:: start_learning()

   Start infrared learning and only support remote control commands that learn the standard NEC protocol.

.. function:: stop_learning()

   Stop infrared learning.

.. function:: save_learned_result(index)

   Save the learned infrared coding result to the corresponding area, parameters：

    - *index* the value range is ``0 ~ 15``, a total of 16 storage areas.

.. function:: send_learned_result(index = 1)

   Send infrared learning saved infrared code, the learning result of the area with index = 1 is set as default, parameters：

    - *index* The index value range is ``0 ~ 15``, a total of 16 storage areas.

.. function:: learn(time = 3)

   Infrared learning ``time`` seconds, after calling this API will save the infrared information learned in ``time`` seconds. Default saved to the area with index = 1, parameter：

    - *time*  learning time, in ``seconds``.

Sample Code 1：
----------------------

.. code-block:: python

  import codey
  import event
  
  @event.start
  def start_cb():
      print("start event succeeded")
      while True:
          codey.display.show(codey.ir.receive_remote_code()[1])

Sample Code 2：
----------------------

.. code-block:: python

  import codey
  import event
  
  @event.button_a_pressed
  def button_a_cb():
      print("button a event succeeded")
      codey.ir.learn()
      codey.led.show(0, 100, 0)
  
  @event.button_b_pressed
  def button_a_cb():
      print("button b event succeeded")
      while True:
          codey.ir.send_learned_result()
  
  @event.button_c_pressed
  def button_c_cb():
      print("button b event succeeded")
      while True:
          codey.display.show(codey.ir.receive())  