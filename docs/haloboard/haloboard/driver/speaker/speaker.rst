:mod:`speaker` ---  Onboard Speaker
=============================================

.. module:: speaker
    :synopsis: Onboard Speaker

``speaker`` The main functionality and functions of the module

Constant
----------------------
- *speaker.volume* - Numerical data, the volume of the property value, can be modified or read this value, can modify this value to control the volume.
                     Its numerical range is 0 ~ 100。
- *speaker.tempo* - The numerical data represent the attributes of the playback speed in BMP (beat per minute), the length of each beat. 
                    The values range form 6 to 600, the default value is 60, which means the duration of a beat is 1 second.The beat of the rest and play_note functions is affected by this constant.

Function
----------------------

.. function:: stop_sound()

  Stop audio playback.

.. function:: play_melody_until_done(file_name)

   Play audio file, this function blocks when playing, parameters:
- *file_name*- String type, audio file name in wav format burned in haloboard flash, input, can also omit the format suffix. 

.. function:: play_melody(file_name)

  Play audio file, this function does not block when playing, parameters:
- *file_name* - String type, audio file name in wav format burned in haloboard flash, input, can also omit the format suffix.
   
.. function:: play_tone(frequency, time_ms=None)

  Play tone by frequency, parameters:
- *frequency* - Numerical data, the frequency at which the sound is played, and its numerical range is 0-1000.
- *time_ms* - Numerical data, indicating the playback time (in millisecond -ms). 
              If this parameter is not filled, the playback will continue; otherwise, the playback will be blocked.

.. function:: play_note(note, beat=None)

  Play notes, numerical note definitions refer to the scratch numerical note description，parameter：
- *note_num* - Numeric types, ranging from 48 to 72, or string types, such as C4, are automatically recognized.
- *beat* - Numerical data, representing the number of beats, if not filled, then play.

  The corresponding relationship between note and frequency is as follows:
    .. image:: img/1.png

.. function:: rest(beat)

  Speaker stop/rest beats time.
- *beat* - Numerical type , refers to the number of beats.

Sample Code：
----------------------

.. code-block:: python

  import haloboard
  import time

  haloboard.speaker.tempo = 60
  haloboard.speaker.volume = 100
  haloboard.speaker.play_melody_until_done("hello")
  haloboard.speaker.play_note(48, 1)
  haloboard.speaker.rest(1)
  haloboard.speaker.play_note("C4", 1)
  haloboard.speaker.rest(1)
  haloboard.speaker.play_tone(1000, 2)
  haloboard.speaker.rest(1)
  print("tempo:", end = "")
  print(haloboard.speaker.tempo)
  print("volume:", end = "")
  print(haloboard.speaker.volume)

  haloboard.speaker.play_note("C4", 3)
  haloboard.speaker.rest(1)
  haloboard.speaker.tempo = 120
  haloboard.speaker.volume = 20
  haloboard.speaker.play_note("C4", 3)
  haloboard.speaker.rest(1)
