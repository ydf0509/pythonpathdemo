
import sys
sys.path.insert(1,'../')    # 这行代码是模仿不会pythonpath的，导致的笨瓜写代码方式。如果运行的起点脚本在20层级的深层级目录下，手动写这个，想死的心都有了。

from d1.d2.d3.m3 import fun3

fun3()