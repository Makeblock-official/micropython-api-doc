:mod:`random` --- 获取随机数模块
=============================================

.. module:: random
    :synopsis: 获取随机数模块

``random`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: random()

   用于生成一个0到1的随机符点数: 0 <= n < 1.0

.. function:: uniform(a, b)

   用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a。参数：
- *a* 上限/下限
- *b* 上限/下限

参考代码如下:

.. code-block:: python

  print random.uniform(10, 20)
  print random.uniform(20, 10)
  # 18.7356606526
  # 12.5798298022 

.. function:: randint(a, b)

   用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b。
- *a* 下限
- *b* 上限

参考代码如下:

.. code-block:: python

  print random.randint(12, 20)  # 生成的随机数 n: 12 <= n <= 20
  print random.randint(20, 20)  # 结果永远是20     
  # print random.randint(20, 10)  # 该语句是错误的。下限必须小于上限

.. function:: randrange([start], stop[, step])

   从指定范围内，按指定基数递增的集合中 获取一个随机数。如：random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。
- *start* 指定的基数
- *stop* 上限
- *step*  递增单位

.. function:: choice(sequence)

   从序列中获取一个随机元素。 参数：
- *sequence* 表示一个有序类型。

参考代码如下:

.. code-block:: python

  print random.choice("学习Python")
  print random.choice(["JGood", "is", "a", "handsome", "boy"])
  print random.choice(("Tuple", "List", "Dict")) 

.. function:: shuffle(x[, random])

   用于将一个列表中的元素打乱。参数
- *x* 需要被打乱的列表。

参考代码如下:

.. code-block:: python

  p = ["Python", "is", "powerful", "simple", "and so on..."]
  random.shuffle(p)
  print p
  # ['powerful', 'simple', 'is', 'Python', 'and so on...'] 

.. function:: sample(sequence, k)

   从指定序列中随机获取指定长度的片断，同时sample函数不会修改原有序列。参数：
- *sequence* 序列
- *k* 片断长度

参考代码如下:

.. code-block:: python

  list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  slice = random.sample(list, 5)  # 从list中随机获取5个元素，作为一个片断返回
  print slice
  print list  # 原有序列并没有改变

程序示例：
------------

.. code-block:: python

  import time
  import random

  while True:
      x = int(random.randint(200, 600))
      print("x is:", x)
      time.sleep(1)