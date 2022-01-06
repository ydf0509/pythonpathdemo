from d1.d2.d3.m3 import fun3


# 这个文件在pychamr下完美运行，cmd命令行会报错 d1包找不到。除非在窗口会话设置PYTHONPATH环境变量
# 不用硬编码sys.path.insert
fun3()
