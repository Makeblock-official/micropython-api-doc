点亮LED和基本Python概念
=========================================

对TPYBoard 板上最容易实现的事情莫过于点亮板上附带的小灯，连接开发板，按照上篇教程中提到的登录方法，
就可与在解释器中开始点亮 LED 灯了，代码如下：
::
    >>> myled = pyb.LED(1)
    >>> myled.on()
    >>> myled.off()

这些命令将控制 LED 的亮和灭。

这种方式不错，不过我们将尝试让其更智能化。在你擅长的文本编辑器里打开 TPYBoard 里边的 main.py 文件，写入或粘贴如下的代码。
如果你是 python 新手，那么希望从现在开始你能对 python 有正确的认识。
::
    led = pyb.LED(2)
    while True:
        led.toggle()
        pyb.delay(1000)

当你保存了文件后，TPYBoard 上的红色 LED 将在约一秒后亮起。为运行脚本程序，先以 CTRL -D 进行软件复位。TPYBoard 将被重启且能够看到绿色的 LED 持续闪烁。
至此先恭喜你在“the army of evil robot”的路途上迈出了重要的一步！当需要关闭闪灯时，直接在终端界面按下 CLRT -C 即可。

那么这些代码做了什么呢?首先我们需要引用一些术语。Python 是一门面向对象语言（object-oriented），
Python中几乎所有的东西都是一个类（class），当你创建一个类的实例时，你得到一个对象（object）。类有与它们相关的方法（methods，也称为成员函数）。方法用于与对象进行交互或控制。

程序的第一行我们通过实例化了LED对象并命名为led，
当我们创建对象时, 它需要一个单一的参数，必须介于1和4之间，与开发板上四颗LED相呼应。
pyb.LED这个类有三个我们使用的重要成员函数：on(), off() 以及 toggle()。
另一个使用到的函数pyb.delay() 仅是一个简单的毫秒级别的延时。一旦我们创建了 LED 对象，while True 这个声明将创建一个无限循环等待一秒时间的 led亮灭翻转。

**练习：尝试改变切换LED和打开其他LED之间的时间。**

**练习：直接连接到TPYBoard，创建一个pyb.LED对象，并使用on()方法打开它。**

在 TPYBoard 板上的Disco
-------------------------

到目前我们使用了板上的单颗 LED 灯而实际上总共有四颗可供使用。我们可以为每颗 LED 灯创建一个对象并分别控制它们。我们将声明一个便于理解的列表（list）形式:
::
    leds = [pyb.LED(i) for i in range(1,5)]

如果没有用 1，2，3，4 的数字作为 pyb.LED()的形参，我们将会得到错误的信息。
接下来我们将添加每个 LED 亮灭的无限循环。
::
    n = 0
    while True:
        n = (n + 1) % 4
        leds[n].toggle()
        pyb.delay(50)

在这里，n 代表了当前的 LED 且每次循环执行后我们可以得到下一个 n 的值（求余符号%保证了 n 的值在0和3之间）。
然后我们就可以控制第 n 颗 led 灯的翻转亮灭了。执行该程序将可见一排的 led 同时亮和灭。

您可能会发现的一个问题是，如果您停止脚本，然后重新启动，
开发板上的 LED 灯将从之前运行的状态突然进入到我们精心设计的Disco。
可以通过在脚本初始化时关闭所有的 LED 灯并使用  try/finally 块的方式解决这个问题。
当打入 CTRL-C，MicroPython 将产生一个 VCP 中断异常。
异常通常意味着某事出了问题，所以你可以通过 try:command 指令“抓取”一个异常。
这种情况属于用户打断了脚本的运行，所以我们不需要抓取错误而是简单告诉 MicroPython 当我们退出时要做些什么。
最终的程序块如下所示，且我们确保了所有的 LED灯 熄灭。完整的代码如下所示：
::
    leds = [pyb.LED(i) for i in range(1,5)]
    for l in leds:
        l.off()
    n = 0
    try:
        while True:
            n = (n + 1) % 4
            leds[n].toggle()
            pyb.delay(50)
    finally:
        for l in leds:
            l.off()

特殊的第四颗灯
----------------------

蓝色的LED 灯比较特别。可以在让其亮灭的同时通过 iniensity()的方法控制其亮度。
其亮度值在 0 到 255 的值间决定。以下的脚本实现了蓝色的LED循环渐亮然后熄灭的功能。
::
    led = pyb.LED(4)
    intensity = 0
    while True:
        intensity = (intensity + 1) % 255
        led.intensity(intensity)
        pyb.delay(20)

你可以对其他LED灯调用 instensity() 的方法，不过其只能被熄灭或被点亮。0 值将使之熄灭而最多到达255的其他值只能点亮该LED。
