:mod:`codey_script_control` --- Script/thread Control
=============================================

.. module:: codey
    :synopsis: Script/thread Control

The main functionality and function of the ``codey_script_control`` module (you do not need to bring the module name when using due to it is a system function)

Function
----------------------

.. function:: stop_this_script()

   Stop the current script, consistent with the scratch stop script feature.

.. function:: stop_other_scripts()

   Stop other scripts, consistent with the scratch stop other scripts feature.

.. function:: stop_this_script()

   Stop all scripts, consistent with the scratch stop all scripts.

Sample Code：
----------------------

.. code-block:: python

  import codey
  import time
  import event
  
  @event.start
  def start_cb():
      while True:
          print("start cb executing...")
          time.sleep(1)
          print("stop this script")
          codey.stop_this_script()
  
  @event.button_a_pressed
  def button_a_cb():
      codey.stop_other_scripts()
      while True:
          print("button a event")
  
  @event.button_b_pressed
  def button_b_cb():
      codey.stop_other_scripts()
      while True:
          print("button b event")
  
  @event.button_c_pressed
  def button_c_cb():
      codey.stop_all_scripts()  