电源控制
=============

:meth:`pyb.wfi` 用于在等待中断等事件时降低功耗。您将在以下情况下使用它：
::
    while True:
        do_some_processing()
        pyb.wfi()

控制频率 :meth:`pyb.freq`：
::
    pyb.freq(30000000) # set CPU frequency to 30MHz
