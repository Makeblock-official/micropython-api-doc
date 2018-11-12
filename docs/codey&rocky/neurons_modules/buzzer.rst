:mod:`buzzer` --- Buzzer
=============================================

.. module:: buzzer
    :synopsis: Buzzer

The main functionality and function of the ``buzzer`` module

Function
----------------------

.. function:: play_note(note_num, beat = None)

   Play note, digital note definitions please refer to： `scratch digital note description <https://en.scratch-wiki.info/wiki/Play_Note_()_for_()_Beats_(block)>`_, prameters：

    - *note_num* numeric value, range of values ``48 - 72``, or string type, such as ``C4``.
    - *beat* value data, indicates the number of beats, the default value is always playing.
     notes and frequency is as follows::

     ['C2','65'],   ['D2','73'],   ['E2','82'],   ['F2','87'],
     ['G2','98'],   ['A2','110'],  ['B2','123'],  ['C3','131'],
     ['D3','147'],  ['E3','165'],  ['F3','175'],  ['G3','196'],
     ['A3','220'],  ['B3','247'],  ['C4','262'],  ['D4','294'],
     ['E4','330'],  ['F4','349'],  ['G4','392'],  ['A4','440'],
     ['B4','494'],  ['C5','523'],  ['D5','587'],  ['E5','659'],
     ['F5','698'],  ['G5','784'],  ['A5','880'],  ['B5','988'],
     ['C6','1047'], ['D6','1175'], ['E6','1319'], ['F6','1397'],
     ['G6','1568'], ['A6','1760'], ['B6','1976'], ['C7','2093'],
     ['D7','2349'], ['E7','2637'], ['F7','2794'], ['G7','3136'],
     ['A7','3520'], ['B7','3951'], ['C8','4186'], ['D8','4699'],

.. function:: play_tone(frequency, time = None)

   Play the tone of setting frequency, prameters：

    - *frequency* Numerical data, the frequency of sound which is played, and its value range is ``0 ~ 5000``.
    - *time* Numerical data, indicating the playback time (in ``milliseconds - ms``) and its value range is ``0 ~ the value range limit``.

.. function:: rest(number)

   Stop the beat, parameters：

    - *number* Numerical data, the number of paused beats, its value range is ``0 ~ the value range limit``.

Constant
----------------------

.. data:: buzzer.tempo

   Numerical data, indicating the nature of the playback speed, in ``bmp`` (beat per minute), which is the length of each beat.Its value range is ``6 ~ 600``. The default value is 60, which means that the duration of one beat is 1 second. The beats of the ``rest`` and ``play_note`` functions are affected by this constant.

Sample Code：
----------------------

.. code-block:: python

  import codey
  import time
  import neurons
  
  codey.display.show("hello")
  
  neurons.buzzer.play_note(48, 1)
  neurons.buzzer.rest(1)
  codey.display.show("note")
  codey.display.clear()
  neurons.buzzer.play_note("C4", 1)
  neurons.buzzer.rest(1)
  codey.display.show("C4")
  codey.display.clear()
  neurons.buzzer.play_tone(1000, 2)
  neurons.buzzer.rest(1)
  codey.display.show("tone")
  codey.display.clear()
  
  while True:
      neurons.buzzer.tempo = 60
      print("tempo:", end = "")
      print(neurons.buzzer.tempo)
      neurons.buzzer.play_note("C4", 1)
      neurons.buzzer.rest(2)
      neurons.buzzer.tempo = 240
      neurons.buzzer.play_note("C4", 1)
      neurons.buzzer.rest(2)
