:mod:`funny_touch` --- Funny Touch
=============================================

.. module:: funny_touch
    :synopsis: Funny Touch

The main functionality and function of the ``funny_touch`` module

Funny touch user Guide
----------------------

.. image:: img/1.png

Funny touch can be connected to any conductive object (such as bananas and water) and turn it into a touch switch. A simple and 
interesting interactive effect can be achieved by detecting the conducting state between funny switches and GND wire.

How to use?

1. Plug the funny switch to slot 1 and the GND wire to slot 2.

2. Clip a funny switch to a conductive object.

3. Hold the metal clip of the GND wire and touch the conductive object with the other hand, the relevant indicator will light up and the 
block will send out an on signal.

Tips: Alligator clip is sharp, please do not clip yourself with the funny switch or the clip of GND wire, it may hurt you.


Function
----------------------

.. function:: is_red_touched()

   Whether the red clip is touched or not, result will be ``True``: yes, it is touched, or ``False``: no, it isn't touched.

.. function:: is_green_touched()

   Whether the green clip is touched or not, result will be ``True``: yes, it is touched, or ``False``: no, it isn't touched.

.. function:: is_yellow_touched()

   Whether the yellow clip is touched or not, result will be ``True``: yes, it is touched, or ``False``: no, it isn't touched.

.. function:: is_blue_touched()

   Whether the blue clip is touched or not, result will be ``True``: yes, it is touched, or ``False``: no, it isn't touched.

Sample Code：
------------

.. code-block:: python

  import codey
  import time
  import event
  import neurons
  
  @event.start
  def start_cb():
      while True:
          if neurons.funny_touch.is_blue_touched():
              print("blue touched")
          if neurons.funny_touch.is_red_touched():
              print("red touched")
          if neurons.funny_touch.is_green_touched():
              print("green touched")
          if neurons.funny_touch.is_yellow_touched():
              print("yellow touched")
          
          time.sleep(0.1)
