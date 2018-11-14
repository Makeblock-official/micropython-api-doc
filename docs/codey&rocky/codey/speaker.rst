:mod:`speaker` --- Onboard Speaker
=============================================

.. module:: speaker
    :synopsis: Onboard Speaker

The main functionality and function of the ``speaker`` module

Function
----------------------

.. function:: stop_sounds()

   Stop all sounds.

.. function:: play_melody(file_name)

   Playing an audio file, the function will not block when playing, but if it is called continuously, the next playback will stop the previous playback, Parameters：

    - *file_name* String type, the audio file name of the wav format burned in Codey Rocky flash. When inputting, the format suffix ``.wav`` can also be omitted
     The optional sound file has
::

     hello.wav       ： hello
     hi.wav          ： hi
     bye.wav         ： bye
     yeah.wav        ： yeah
     wow.wav         ： wow
     laugh.wav       ： laugh
     hum.wav         ： hum
     sad.wav         ： sad
     sigh.wav        ： sigh
     annoyed.wav     ： annoyed
     angry.wav       ： angry
     surprised.wav   ： scared
     yummy.wav       ： pettish
     curious.wav     ： curious
     embarrassed.wav ： embarrassed
     ready.wav       ： ready
     sprint.wav      ： sprint
     sleepy.wav      ： snore
     meow.wav        ： meow
     start.wav       ： start
     switch.wav      ： switch
     beeps.wav       ： beeps
     buzzing.wav     ： buzz
     exhaust.wav     ： air-out
     explosion.wav   ： explosion
     gotcha.wav      ： gotcha
     hurt.wav        ： painful
     jump.wav        ： jump
     laser.wav       ： laser
     level up.wav    ： level-up
     low energy.wav  ： low-energy
     metal clash.wav ： metal-clash
     prompt tone.wav ： prompt-tone
     right.wav       ： right
     wrong.wav       ： wrong
     ring.wav        ： ringtone
     score.wav       ： score
     shot.wav        ： shot
     step_1.wav      ： step_1
     step_2.wav      ： step_2
     wake.wav        ： activate
     warning.wav     ： warning

.. function:: play_melody_until_done(file_name)

   The audio file is played until it stops, and the function blocks playback, that is, the next instruction cannot be executed until the sound is played, parameter：

    - *file_name* String type, the audio file name of the wav format burned in Codey Rocky flash. When inputting, the format name ``.wav`` can also be omitted. For specific optional parameters, see ``play_melody``.

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

   Play the setting frequency sound, parameters：

    - *frequency* Numerical data, the frequency of sound which is played, and its value range is ``0 ~ 5000``.
    - *time* Numerical data, indicating the playback time (in ``milliseconds - ms``) and its value range is ``0 ~ the value range limit``.

.. function:: rest(number)

   Stop the beat, parameters：

    - *number* Numerical data, the number of paused beats, its value range is ``0 ~ the value range limit``.

Constant
----------------------

.. data:: speaker.volume

   Numerical data, the property value of the volume, you can modify or read this value. Modify this value to control the volume. Its value range is ``0 ~ 100``.

.. data:: speaker.tempo

   Numerical data, indicating the nature of the playback speed, in ``bmp`` (beat per minute), which is the length of each beat.Its value range is ``6 ~ 600``. The default value is 60, which means that the duration of one beat is 1 second. The beats of the ``rest`` and ``play_note`` functions are affected by this constant.

Sample Code：
----------------------

.. code-block:: python

  import codey
  import time
  
  codey.speaker.play_melody("hello", True)
  codey.display.show("hello")
  codey.display.clear()
  
  codey.speaker.play_note(48, 1)
  codey.speaker.rest(1)
  codey.display.show("note")
  codey.display.clear()
  codey.speaker.play_note("C4", 1)
  codey.speaker.rest(1)
  codey.display.show("C4")
  codey.display.clear()
  codey.speaker.play_tone(1000, 2)
  codey.speaker.rest(1)
  codey.display.show("tone")
  codey.display.clear()
  print("tempo:", end = "")
  print(codey.speaker.tempo)
  codey.speaker.play_note("C4", 1)
  codey.speaker.rest(1)
  codey.speaker.tempo = 120
  codey.speaker.volume = 20
  codey.speaker.play_note("C4", 1)
  codey.speaker.rest(1)
