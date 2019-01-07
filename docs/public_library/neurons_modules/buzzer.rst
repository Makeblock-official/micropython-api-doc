:mod:`buzzer` --- 蜂鸣器模块
=============================================

.. module:: buzzer
    :synopsis: 蜂鸣器模块

``buzzer`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: play_note(note_num, beat = None)

   播放音符， 数字音符定义请参考： `scratch数字音符说明 <https://en.scratch-wiki.info/wiki/Play_Note_()_for_()_Beats_(block)>`_，参数：

    - *note_num* 数值型，数值范围 ``48 - 72``，或者字符串类型，如 ``C4``。
    - *beat* 数值数据，表示节拍数，如果不填，则一直播放。
     音符与频率的对应关系如下::

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

   播放设定频率的声音，参数：

    - *frequency* 数值数据，播放声音的频率，其数值范围是 ``0 ~ 5000``。
    - *time* 数值数据，表示播放时间(单位是 ``毫秒-ms`` )，其数值范围是 ``0 ~ 数值范围极限``。

.. function:: rest(number)

   停止节拍，参数：

    - *number* 数值数据，暂停的节拍数，其数值范围是 ``0 ~ 数值范围极限``。

常量
----------------------

.. data:: buzzer.tempo

   数值数据，数值范围是 ``6 ~ 600``，表示播放速度的属性，单位是 ``bmp(beat per minute)``，即每一个节拍的长度。 默认数值是60，即一个节拍的维持时间是1秒。 ``rest`` 和 ``play_note`` 函数的节拍会受该常量影响。

程序示例：
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
