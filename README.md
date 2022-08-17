# 用一个python项目文件夹结构说明掌握 PYTHONPATH作用的重要性

这个readme要认真看，里面说明了pythonath的作用，

第6章还重点解释了永久性环境变量和临时环境变量的重大影响范围的区别

第7章说明了任何项目如果设置了 PYTHONPATH 的4大好处

第9章说明了设置 PYTHONPATH 达到多个项目复用公司公共工具类代码的妙用



## 1.项目目录说明
```
pythonpathdemo是这个项目的根目录，
d1/d2/d3/m3.py  有一个fun3函数，
d4/d5/run.py 里面导入和运行fun3函数
，这种目录的python项目就很容易验证懂PYTHONPATH的重要性了。
```

## 2. 演示pyachrm完美运行，cmd和vscode报错
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


## 4.演示不学习PYTHONPATH， 愚蠢的手动硬编码 sys.path
```
笨瓜喜欢手动操作sys.path,然后在cmd命令，cd 到d5目录下，
再运行 python run5.py，太笨了这样写，
如果别的文件夹层级有run6.py   run7.py,一个个脚本硬编码sys.path改到猴年马月。
```

![](https://img2020.cnblogs.com/blog/1108990/202111/1108990-20211119104757875-1491247839.png)

```
为什么老有笨瓜喜欢在很多python脚本硬编码 sys.path.insert或者append？
这种人主要是不懂 PYTHONPATH的作用，造成到处手动硬编码操作sys.path。

你不信去看看任意一个三方包python大神写的框架或者库，就算目录结果复杂有七八层文件夹，有谁那么愚蠢这么手动操作sys.path的？
手动sys.path.insert是一厢情愿一意孤行意淫的写法。

可以这么说，在控制台命令行部署运行任何项目，把PYTHONPATH设置为项目根目录路径是最合适的，
pycahrm默认帮我们这么做了。你这么做了，那么你的代码运行逻辑就和pycahrn运行代码保持一致了。
```

像这个深层级文件夹下的 d6/d7/d8/d9/d10/run10.py ，在cmd下运行，你不会设置 PYTHONPATH，手写sys.path真的是非常的想死的心都有了。

如果你的项目有有几百个深层级目录下的脚本都可以做为运行起点被直接python xx.py 启动，你为了cmd运行正常，一个一个的脚本里面加sys.path.insert加到口吐鲜血。

[![Txasbj.md.png](https://s4.ax1x.com/2022/01/06/Txasbj.md.png)](https://imgtu.com/i/Txasbj)



## 5 在win和linux，cmd和shell一句话怎么运行两条命令


### 5.1 如果分开两次运行命令行
```
首先cd 到项目根目录，然后linux 上 是 export PYTHONPATH=./ 
如果是win上是 set PYTHONPATH=./  ，  
然后可以切换到任意文件夹，运行你需要运行的python xx.py

当然可以不先cd到项目根目录，那就 export PYTHONPATH=项目根目录的绝对路径 就行了。
```

### 5.2 如果一句命令行同时设置环境变量和运行python脚本
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

WorkPlatFormApi.settings 说得是从 WorkPlatFormApi 文件夹下的 settings.py 作为配置文件来源，
如果你在测试linux环境想用不同的msqyl配置等，写个 settings_test.py,然后 export DJANGO_SETTINGS_MODULE="WorkPlatFormApi.settings_test",
再用uswgi部署django，那就自动使用指定的settings_test.py了。生产环境写个 settings_prod.py 设置环境变量同理。
```


### 6.1 什么是永久性环境变量
```
永久性环境变量就是你在win上，点电脑右键 高级里面设置环境变量 
在linux就是vim /etc/profile   ,或者 vim ~/.bashrc  ,
这种修改就是永久性固定写死的环境变量，会影响使用这台电脑的所有人，在这里写 PYHTONPATH 不仅会影响所有人也会影响所有python项目，
这种一般是配置java安装在哪里了，python安装在哪里了，但非常不适合设置 PYTHONPATH
```

### 6.1.2 在环境变量配置文件中写死永久性PYTHONPATH的非常坑人例子

```
公司我们测试环境只有一台服务器，都是登录同一个用户，有个ai硕士 他的项目根目录是 /codes/aiproj/，他的项目根目录下有个 requests.py
同时他在 /etc/profile 中设置了 export PYTHONPATH=/codes/aiproj/，当我们项目导入 import requests时候，运行出错，开发环境运行的好好地，测试环境总是报错，
这个永久性写死PYTHONPATH把我们坑得要死，因为import requests 优先import 到 这个 /codes/aiproj/ 下的requests.py了，而不是知名三方包requests。

```

### 6.2 什么是临时会话环境变量？
```
临时会话环境变量，只会影响你当前单开的cmd 或者 shell窗口，不会影响到其他会话窗口

例如你用xshell 打开两个标签窗口，你在一个设置的环境变量，在另一个窗口是获取不到的，你自己测试下就知道了。
你在窗口设置了环境变量，把窗口关了，下次再打开窗口，这个环境变量仍然获取不到，
你登录一台linux，在xshell窗口设置了环境变量，你同事也用相同账号登录这台linux服务器，你同事并不能获取到你设置的环境变量
所以临时会话级环境变量只会影响当前的会话窗口，不会影响到其他项目和其他人。

了解这一点非常非常重要。你不要以为你随便在终端敲击 export PYTHONPATH 会影响其他人了。每个项目的 PYTHONPATH都设置为自己是非常安全的，不会乱套

```


## 7 运行任何python项目设置 PYTHONPATH为当前项目根目录 是个好习惯，4个好处如下
```
1、设置后，任意项目目录下的任意深层级文件夹下的多个脚本都可以轻松作为python运行起点
2、绝对不需要low操作硬编码 sys.path.insert
3、使用从项目根目录往下寻找模块，用绝对导入，写的脚本位置可以四处移动，代码非常牢固，可靠性高
4、与pycahrm的运行行为保持了一致，大大避免了命令行调试和pycahrm运行需要单独分别调试
```

## 8 一个环境变量设置多个值

```
一个环境变量设置多个值这个和 PYTHONPATH无关，对任何环境变量适用，但有的人还是不知道

export PYTHONPATH=/codes/proj1:/codes/proj2

设置多个环境变量，linux是 : 隔开，win是 ; 隔开。

例如上面一下子设置了 PYTHONPATH 为两个路径，当我 import myutil 时候，
首先从/codes/proj1 下找myutil包或模块，如果没有再从 /codes/proj2 中查找，
如果还没找到就从python的三方包site_packegs目录找，还是找不到就会报错模块不存在

所以你可以设置 PYTHONPATH为当前项目根目录和另一个公司的通用公共库项目
```

### 8.2 pycharm中一个项目怎么使用另外一个项目的包或模块
```
因为pycahrm是点击右键run运行的，不太方便每次手动设置其他项目到当前脚本的 PYTHONPATH
看下图，可以选择denpendece，例如funboost项目中可以直接使用nb_log项目的函数，
这样当nb_log修改代码时候，并不需要把nb_log打包到pypi，然后安装到python目录下，pycahrm的这个功能非常的方便
如果在linux下就使用 PYTHONPATH 设置两个文件夹的方式就行了。
```
[![Tx8jBt.md.png](https://s4.ax1x.com/2022/01/06/Tx8jBt.md.png)](https://imgtu.com/i/Tx8jBt)


## 9 妙用 PYTHONPATH 达到非常方便的多个项目复用公司通用代码库的目的，暴击打包上传pypi再安装
```
一般公司可能有数十个python项目，每个python项目会复用写好的一部分函数和类。

low的人会把公用代码库复制到几十个项目的下面，但这样每次修改或者新增公共代码库要改几十个地方，非常的low。
完全是浪费生命。写代码如果这么麻烦，上班忙的吐血。

中等的程序员会搭建pypi私服，把公共代码库打包上传到公司私服。然后pip安装到python下面。
这样弊端也很明显，改一个字母都要打包上传，然后在几十台服务器和每隔python程序员的电脑操作 pip install -U，太蛋疼了，也是浪费时间和生命。
除非是你想做互联网到处通用的 python包才适合打包，否则仅仅在公司内部复用代码使用打包这种方式不理智。

高端python程序员，精通PYTHONPATH的 会 设按照8和8.2 设置多个PYTHONPATH，
只需要改了通用公共库代码，啥都不需要做，在十几个项目都自动生效。这才是节约生命的方式。
```

## 9.2 怎么确定设置了哪些PYTHONPATH

在代码中写下面的，就可以看到pythonpath了,当import 一个模块时候sys.path越靠前的文件夹路径越优先被查找
```python
import sys
print(sys.path)  

```
# 如果你看完了以上，精通了 PYTHONPATH ，写几十个项目代码能够如虎添翼。更不会抱怨 nb_log 和 funboost 要你 export PYTHONPATH 感到麻烦了。
