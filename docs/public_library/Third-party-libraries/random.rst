:mod:`random` --- Get Random Number Module
=============================================

.. module:: random
    :synopsis: Get Random Number Module

``random`` The main functionality and functions of the module

Function
----------------------

.. function:: random()

   Used to generate a random number of characters from 0 to 1:0 <= n < 1.0

.. function:: uniform(a, b)

   Used to generate a random number of characters within a specified range, with two parameters, one upper and one lower.If a > b, 
   then the generated random number n: a <= n <= b.If a <b, then b <= n <= a.Parameters:
- *a* - Upper/lower limit
- *b* - Upper/lower limit

The reference code is as follows:

.. code-block:: python

  print random.uniform(10, 20)
  print random.uniform(20, 10)
  # 18.7356606526
  # 12.5798298022 

.. function:: randint(a, b)

   Used to generate an integer within a specified range.Where parameter "a" is the lower limit and parameter "b" is the upper limit, 
   the random number n generated is: a <= n <= b.
- *a* - Lower limit
- *b* - Upper limit

The reference code is as follows:

.. code-block:: python

  print random.randint(12, 20)
  print random.randint(20, 20)
  # print random.randint(20, 10)

.. function:: randrange([start], stop[, step])

   Gets a random number from a collection that is incremented by the specified cardinality within the specified range.
   Such as: random.randrange(10, 100, 2), the result is equivalent to obtaining a random number from the [10, 12, 14, 16... 96, 98] sequence.
- *start* - Specified cardinality
- *stop* - Upper limit
- *step* - Increasing unit

.. function:: choice(sequence)

   Gets a random element from a sequence. Parameters:
- *sequence* - Represents an ordered type.

The reference code is as follows:

.. code-block:: python

  print random.choice("Study Python")
  print random.choice(["JGood", "is", "a", "handsome", "boy"])
  print random.choice(("Tuple", "List", "Dict")) 

.. function:: shuffle(x[, random])

   Used to scramble elements in a list, parameters:
- *x* - Need a shuffled list.

The reference code is as follows:

.. code-block:: python

  p = ["Python", "is", "powerful", "simple", "and so on..."]
  random.shuffle(p)
  print p
  # ['powerful', 'simple', 'is', 'Python', 'and so on...'] 

.. function:: sample(sequence, k)

   Gets a random fragment of a specified length from a specified sequence, and the sample function does not modify the original sequence.Parameters:
- *sequence* - Sequence
- *k* - Fragment length

The reference code is as follows:

.. code-block:: python

  list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  slice = random.sample(list, 5)
  print slice
  print list

Sample Code：
------------

.. code-block:: python

  import time
  import random

  while True:
      x = int(random.randint(200, 600))
      print("x is:", x)
      time.sleep(1)