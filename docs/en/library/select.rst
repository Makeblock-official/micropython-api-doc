:mod:`select` -- 等待流事件
========================================================================

.. module:: select
   :synopsis: 等待流事件

提供了在流上等待事件的功能（选择可操作的流）。

TPYBoard特性
-----------------

轮询是在多个对象上等待读/写活动的有效方法。 当前支持: :class:`pyb.UART`,:class:`pyb.USB_VCP`.

函数
---------

.. function:: poll()

   创建轮询类的实例。

.. function:: select(rlist, wlist, xlist[, timeout])

   等待激活一组对象。

   提供的兼容性和效率不高。 推荐使用 :class:`Poll`。

.. _class: Poll

类 ``Poll``
--------------

方法
~~~~~~~

.. method:: poll.register(obj[, eventmask])

   登记轮询对象 ``obj`` 。 ``eventmask`` 是以下逻辑:

   * ``select.POLLIN``  - 读取可用数据
   * ``select.POLLOUT`` - 写入更多数据
   * ``select.POLLERR`` - 发生错误
   * ``select.POLLHUP`` - 流结束/连接终止检测

   ``eventmask`` 默认 ``select.POLLIN | select.POLLOUT``.

.. method:: poll.unregister(obj)

   注销轮询对象 ``obj``。

.. method:: poll.modify(obj, eventmask)

   修改对象``obj``的 ``eventmask``。

.. method:: poll.poll([timeout])

   等待至少一个已注册的对象准备就绪。返回列表(``obj``, ``event``, ...) 元组, 
   ``event`` 元素指定了一个流发生的事件，是上面所描述的 `select.POLL*`常量组合。
   在元组中可能有其他元素，取决于平台和版本，所以不要假定它的大小是2。如果超时，则返回空列表。

   超时为毫秒。
