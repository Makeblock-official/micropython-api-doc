:mod:`speaker` ---  板载扬声器
=============================================

.. module:: speaker
    :synopsis: 板载扬声器

``speaker`` 模块的主要功能与函数

常量
----------------------
- *speaker.volume* 数值数据，音量的大小的属性值，可以修改或者读取这个值。修改这个数值，可以控制音量的大小。其数值范围是 0 ~ 100。
- *speaker.tempo* 数值数据，表示播放速度的属性，单位是 bmp (beat per minute)，即每一个节拍的长度。 其数
  值范围是 6 ~ 600。 默认数值是60，即一个节拍的维持时间是1秒。 rest 和 play_note 函数的节拍会受该常量影响

功能相关函数
----------------------

.. function:: stop_sound()

  停止音频播放。

.. function:: play_melody_until_done(file_name)

   播放音频文件，该函数播放时阻塞，参数： 
- *file_name* 字符串类型，烧录在光环板flash中的wav格式的音频文件
  名，输入时，也可省略格式的后缀 .wav。

.. function:: play_melody(file_name)

  播放音频文件，该函数播放时不阻塞，参数： 
- *file_name* 字符串类型，烧录在光环板flash中的wav格式的音频文
  件名，输入时，也可省略格式的后缀 .wav。
   
.. function:: play_tone(frequency, time_ms=None)

  按频率播放音调，参数：
- *frequency* 数值数据，播放声音的频率，其数值范围是0-1000。
- *time_ms* 数值数据，表示播放时间(单位是 毫秒-ms )，不填此参数，则一直播放，否则阻塞播放。

.. function:: play_note(note, beat=None)

  播放音符， 数字音符定义请参考： scratch数字音符说明，参数：
- *note_num* 数值型，数值范围 48 - 72，或者字符串类型，如 C4，将自动识别。
- *beat* 数值数据，表示节拍数，如果不填，则一直播放。

  音符与频率的对应关系如下:
    .. image:: img/1.png

.. function:: rest(beat)

  扬声器停止/休息的节拍时间。
- *beat* 数值型，指节拍数。

程序示例：
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
