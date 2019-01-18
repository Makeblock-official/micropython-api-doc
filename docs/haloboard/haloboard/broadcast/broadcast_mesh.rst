:mod:`haloboard.mesh` --- Mesh Broadcast Message
=============================================

.. module:: haloboard.mesh
    :synopsis: Mesh Broadcast Message

``haloboard.mesh`` The main functionality and functions of the module

Functional Description
----------------------
This module mainly introduces the function API based on mesh network module.

Function
----------------------

.. function:: start(type = "node")

  Start mesh communication，parameter：
- *type* - Refers to the type in the mesh network, which can be root or node by default.

# mesh boardcast

.. function:: get_number_of_nodes()

  Get the current number of nodes in the mesh network.

.. function:: on_mesh_message_come(msg)

  Process mesh messages.
- *msg* - Mesh messages that currently need to be processed.

.. function:: get_info(msg)

  Get the information of the mesh message.
- *msg* - Mesh messages that currently need to be processed.

.. function:: get_info_status(msg)

  Gets the current state of the mesh message.
- *msg* - Mesh messages that currently need to be processed.

# for online mode

.. function:: get_all_info_status()

  Gets the current state of all mesh messages

.. function:: get_info_once(msg)

  Get the information of the mesh message a single time.
- *msg* - Mesh messages that currently need to be processed.

Sample Code 1：
----------------------

.. code-block:: python

  # -*- coding: utf-8 -*-
  # as a node
  import haloboard
  import time
  import event

  count = 0

  @event.start
  def on_start():
      haloboard.mesh.start(type = "node")

  @event.button_pressed
  def on_button_a_pressed():
      global count
      print("button is pressed")
      haloboard.mesh.broadcast("hello", str(count))
      count += 1

  @event.mesh_message("hello")
  def received_cb():
      print("received message: hello")
      print("value:", haloboard.mesh.get_info("hello"))

Sample Code 2：
----------------------

.. code-block:: python

  # -*- coding: utf-8 -*-
  # as a root
  import haloboard
  import time
  import event

  @event.start
  def on_start():
      haloboard.mesh.start(type = "root")

  @event.button_pressed
  def on_button_a_pressed():
      print("button is pressed")
      haloboard.mesh.broadcast("hello", '123')

  @event.mesh_message("hello")
  def received_cb():
      print("received message: hello")
      print("value:", haloboard.mesh.get_info("hello"))
