:mod:`codey_timer` --- Counter
=============================================

.. module:: codey
    :synopsis: Counter

The main functionality and function of the ``codey_timer`` module (you do not need to bring the module name when using due to it is a system function)

Function
----------------------

.. function:: get_timer()

   Gets the current value of the timer (the timer runs from the time the user script starts), the return value is a floating point data. The unit is ``seconds``.

.. function:: reset_timer()

   Initialize the value of the timer.

程序示例：
----------------------

.. code-block:: python

  import codey
  
  codey.reset_timer()
  
  while True:
      print("time:", end = "")
      print(codey.get_timer())