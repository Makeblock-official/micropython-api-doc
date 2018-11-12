:mod:`codey_external_module_detect` --- External Module access Detection
=============================================

.. module:: codey
    :synopsis: External Module access Detection

The main functionality and function of the ``codey_external_module_detect`` module (you do not need to bring the module name when using due to it is a system function)

Function
----------------------

.. function:: has_neuron_connected()

   Check whether there is any neuron module connected to Codey, and the return value is a Boolean value, where ``True`` indicates that the neuron module is connected to Codey (including the connecting of the Rocky), and ``False`` indicates that there is no neuron module connected to the Codey.

.. function:: is_rocky_connected()

   Check if the Rocky is connected to the Codey, the return value is a Boolean value, where ``True`` means that there is a Rocky connected to the Codey, and ``False`` means no Rocky connected to Codey.

Sample Code：
----------------------

.. code-block:: python

  import codey
  import time
  
  while True:
      if codey.is_rocky_connected():
          print("rocky is in")
      else:
          print("rocky is out")
      time.sleep(1)