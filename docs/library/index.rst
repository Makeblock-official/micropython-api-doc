.. _micropython_lib:

microPython 官方类库
=====================

.. warning::

   本章节的重要摘要

   * MicroPython为每个模块实现了Python功能的子集。
   * 为了简化可扩展性，MicroPython版本的标准Python模块通常有``u``（“micro”）前缀。
   * 任何特定的MicroPython主板分支都可能遗漏本通用文档中描述的部分功能/函数（由于资源限制或其他限制）。


本章介绍了构成micropython的模块（函数和类库）。有几类模块:

* 内置模块：标准Python功能的子集，用户不能扩展。
* 扩展模块：实现了Python功能的一个子集，并提供用户扩展（通过Python代码）。
* 扩展模块：实现micropython的Python标准库。
* 硬件驱动模块:特定端口或者硬件驱动的模块，因此不可移植。

请注意模块及其内容的可用性：本文档通常所描述所有模块和函数/类在MicroPython项目中都会尽量实现。
但是，MicroPython具有高度可配置性，所以在特定主板/嵌入式系统中可能会仅提供一个子集MicroPython库。
对于官方支持的端口，我们会尽量过滤掉不适用的项目，或标记个别模块的“可用性：” 即使用子句描述主板提供的功能。

考虑到这一点，请仍然警告一些函数/类在本文档中描述的模块（甚至整个模块）中 **可能在特定系统上的特定MicroPython版本中不可用**。
该查找可用性/不可用性的一般信息的最佳位置特定功能的“通用信息”部分包含有关特定`MicroPython主板`的信息。

在某些端口上，可用的内置库的查询，可以通过在REPL中输入以下内容来导入:: REPL::

    help('modules')

除了本文档中描述的内置库之外，还有更多来自Python标准库的模块，它们可以提供更多的MicroPython
的扩展，可以github的 `micropython-lib`找到.

micropython 标准库
---------------------------------------------

标准的Python库被 “微型化”后，就是micropython标准库。它们仅仅提供了该模块的核心功能。一些模块没有直接使用标准的Python的名字，而是冠以"u"，例如``ujson``代替``json``。也就是说micropython标准库（=微型库），只实现了一部分模块功能。通过他们的名字不同，用户有选择的去写一个Python级模块扩展功能，也是为实现更好的兼容性。

在嵌入式平台上，可添加Python级别封装库从而实现命名兼容CPython，微模块即可调用他们的u-name，也可以调用non-u-name。根据non-u-name包路径的文件可重写。

例如，``import json``的话，首先搜索一个``json.py``文件或``json``目录进行加载。如果没有找到，它回退到加载内置``ujson``模块。

.. toctree::
   :maxdepth: 1

   builtins.rst
   array.rst
   cmath.rst
   gc.rst
   math.rst
   sys.rst
   ubinascii.rst
   ucollections.rst
   uerrno.rst
   uhashlib.rst
   uheapq.rst
   uio.rst
   ujson.rst
   uos.rst
   ure.rst
   uselect.rst
   usocket.rst
   ussl.rst
   ustruct.rst
   utime.rst
   uzlib.rst
   _thread.rst


microPython 特有类库
------------------------------

MicroPython的特有功能如下。

.. toctree::
   :maxdepth: 1

   btree.rst
   framebuf.rst
   machine.rst
   micropython.rst
   ucryptolib.rst
   uctypes.rst
