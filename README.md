# 用一个python项目文件夹结构说明掌握 PYTHONPATH作用的重要性

##1.项目目录说明
```
pythonpathdemo是这个项目的根目录，
d1/d2/d3/m3.py  有一个fun3函数，
d4/d5/run.py 里面导入和运行fun3函数
，这种目录的python项目就很容易验证懂PYTHONPATH的重要性了。
```

##2. 演示pyachrm完美运行，cmd和vscode报错
![](https://img2020.cnblogs.com/blog/1108990/202111/1108990-20211119103852120-953934616.png)

截图可以看出，在pycahrm运行run5.py正确调用fun3函数，在cmd命令行却不行，vscode也不行。

主要原因是pycahrm自动把项目根目录加到了 PYTHONPATH，如下图你把这两个勾选去掉就pycahrm运行run5.py也会和cmd命令行一样报错。

![](https://img2020.cnblogs.com/blog/1108990/202111/1108990-20211119104028204-1581286624.png)



## 3. 演示在cmd命令行设置临时会话环境变量 PYTHONPATH 后运行完美
```
如果在cmd窗口会话中临时设置PYTHONPATH为项目根目录再运行run5.py就不会报错了。

注意要在代码运行前临时设置环境变量，不要设置永久固定系统环境变量，因为你不可能只有一个python项目，一般每个人最少有七八个python项目吧。

如果嫌敲击两次命令麻烦，一句命令行可以运行多个命令，win是：      set PYTHONPATH=项目根目录 & python run.py

linux是：     export  PYTHONPATH=项目根目录 ； python run.py, 

vscode 也是可以学pycharm 设置PYTHONPATH的，只是不是像pycahrm那样默认自动添加，所以pycahrm专业ide就是比vscode好。
自己百度vscode PYTHONPATH 关键字。
```
![](https://img2020.cnblogs.com/blog/1108990/202111/1108990-20211119104340305-1438114681.png)


##4.演示不学习PYTHONPATH， 愚蠢的手动硬编码 sys.path
```
笨瓜喜欢手动操作sys.path,然后在cmd命令，cd 到d5目录下，
再运行 python run5.py，太笨了这样写，
如果别的文件夹层级有run6.py   run7.py,一个个脚本硬编码sys.path改到猴年马月。
```

![](https://img2020.cnblogs.com/blog/1108990/202111/1108990-20211119104757875-1491247839.png)

```
为什么老有笨瓜喜欢在很多python脚本硬编码 sys.path.insert或者append？
这种人主要是不懂 PYTHONPATH的作用，造成到处手动硬编码操作sys.path。

你不信去看看任意一个三方包python大神写的框架或者库，有谁那么愚蠢这么手动操作sys.path的？
手动sys.path.insert是一厢情愿一意孤行意淫的写法。

可以这么说，在控制台命令行部署运行任何项目，把PYTHONPATH设置为项目根目录路径是最合适的，
pycahrm默认帮我们这么做了。你这么做了，那么你的代码运行逻辑就和pycahrn运行代码保持一致了。
```

## 5 在win和linux，cmd和shell一句话怎么运行两条命令


###5.1 如果分开两次运行命令行
```
首先cd 到项目根目录，然后linux 上 是 export PYTHONPATH=./ 
如果是win上是 set PYTHONPATH=./  ，  
然后可以切换到任意文件夹，运行你需要运行的python xx.py

当然可以不先cd到项目根目录，那就 export PYTHONPATH=项目根目录的绝对路径 就行了。
```

###5.2 如果一句命令行同时设置环境变量和运行python脚本
```
首先cd 到项目根目录，
然后linux 上 是 export PYTHONPATH=./ ; python xx.py
如果是win上是 set PYTHONPATH=./ &  python xx.py

当然可以不先cd到项目根目录，那就 export PYTHONPATH=项目根目录的绝对路径 就行了。
```

## 6 需要非常非常重点的说明什么叫临时会话级环境变量和什么是永久性写死的环境变量，区别很大,

# 有的人非常之疑惑环境变量会不会混乱乱套的，一定看这个要。


这个知识点本来不应该在这里说，不属于pythonpath要讲解的。

但是很多人仍然不清楚临时环境变量和永久性环境变量的区别，导致很疑惑认为python项目如果有十几个，一台linux机器登录的人数如果很多，会不会互相干扰

```
实不相瞒本人多年前看dajngo也很疑惑，例如django的 os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WorkPlatFormApi.settings")，
我那时候一直在想，如果一台机器部署七八个django服务咋办，每个项目全都设置自己的 DJANGO_SETTINGS_MODULE 这个 环境变量，那不是乱套呀。
如果我设置这个环境变量会不会影响同事使用这个linux也使用django？会不会混了乱套了？需不需要提心吊胆呢？
那个时候，主要是没理解什么是临时环境变量和永久性环境变量。一直到现在 很多人在使用我的框架时候，我要求设置PYTHONPATH，他们一直疑惑这个问题。
```


### 6.1 什么是永久性环境变量
```
永久性环境变量就是你在win上，点电脑右键 高级里面设置环境变量 
在linux就是vim /etc/profile   ,或者 vim ~/.bashrc  ,
这种修改就是永久性固定写死的环境变量，会影响使用这台电脑的所有人，在这里写 PYHTONPATH 不仅会影响所有人也会影响所有python项目，
这种一般是配置java安装在哪里了，python安装在哪里了，但非常不适合设置 PYTHONPATH
```

### 6.1.2 写死 PYTHONPATH的非常坑人例子

```
公司我们测试环境只有一台服务器，都是登录同一个用户，有个ai硕士 他的项目根目录是 /codes/aiproj/，他的项目根目录下有个 requests.py
同时他在 /etc/profile 中设置了 export PYTHONPATH=/codes/aiproj/，当我们项目导入 import requests时候，运行出错，开发环境运行的好好地，测试环境总是报错，
这个永久性写死PYTHONPATH把我们坑得要死，因为import requests 优先import 到 这个 /codes/aiproj/ 下的requests.py了，而不是知名三方包requests。

```

### 6.1 什么是临时会话环境变量？
```
临时会话环境变量，只会影响你当前单开的cmd 或者 shell窗口，不会影响到其他会话窗口

例如你用xshell 打开两个标签窗口，你在一个设置的环境变量，在另一个窗口是获取不到的，你自己测试下就知道了。
你在窗口设置了环境变量，把窗口关了，下次再打开窗口，这个环境变量仍然获取不到，所以临时会话级环境变量只会影响当前的会话窗口，不会影响到其他项目和其他人。

了解这一点非常非常重要。你不要以为你随便在终端敲击 export PYTHONPATH 会影响其他人了。

```