<p align="center">
    <a href="https://hice.run" target="_blank" rel="noopener noreferrer">
        <img width="100" src="https://s1.ax1x.com/2023/01/13/pSK4gln.png" alt="Halo logo" />
    </a>
</p>

<p align="center"><b>Ice Shell</b> [aɪs ʃɛl]，一个Python编写的脚本运行框架，支持扩展模块</p>

<p align="center">
<a href="https://github.com/lanbinshijie/IceShell"><img alt="GitHub release" src="https://img.shields.io/github/release/lanbinshijie/IceShell.svg?style=flat-square&include_prereleases" /></a>
<a href="https://github.com/lanbinshijie/IceShell"><img alt="Docker pulls" src="https://img.shields.io/github/license/lanbinshijie/iceshell?style=flat-square&color=yellow" /></a>
<a href="https://github.com/lanbinshijie/IceShell"><img alt="GitHub Workflow Status" src="https://img.shields.io/github/issues-raw/lanbinshijie/iceshell?style=flat-square" /></a><a href="https://github.com/lanbinshijie/IceShell"><img alt="GitHub last commit" src="https://img.shields.io/github/stars/lanbinshijie/iceshell?label=Github%20Stars&style=flat-square" /></a>
</p>

---

# 介绍
Ice Shell（简称IShell，中文名“冰壳”），是一个Python编写的脚本运行框架，支持扩展模块。

**如果您不介意，可以先看看下面的碎语！**

## IShell设计初衷
往往我们在用Python完成某个小功能时，我们都会直接新建单个Python文件，写完之后就放在一个不知名的小角落，然后使用的时候直接双击运行。

但是这个操作往往会出现很多问题。如果你的程序很复杂，封装了很多的函数，用传统的方式就会造成一些困难，比如依赖问题或是变量问题。而且，当你想要将文件发布出去时，不仅孤零零的一小撮文件不太好看，而且如果他人要想使用这个Python，往往会因为依赖等的问题而无法运行。

同时，IShell也为Shell类程序提供了良好的开发平台。您可以给予IShell开发您自己的程序（如远控，木马）等。

**！如果您有开发远程控制、远程桌面、反弹shell等需求，您可以尝试使用IceShell**

## 碎语
Iceshell马上要出1.0版本了，还是很激动的。

Iceshell项目其实只是我一下心血来潮，主要目的是为接下来的项目打个基础，顺便学习一下git工作流，同时也方便自己日常生活和开发。

希望能够得到更多人的支持，也为有这方面想法的同学投石问路、抛砖引玉。欢迎大家Fork和Star，谢谢大家对我的鼓励！

—— Lanbin 2023年1月15日18:04:39

## IShell功能

- [X] 自定义模块功能与命令
- [ ] 捕获报错信息
- [X] 依赖检测与安装
- [ ] 一键配置程序信息
- [ ] 一键配置程序依赖
- [ ] 一键发布程序
- [X] 模块参数自定义

更多功能敬请期待~

有什么问题和建议可以直接提Issue或者PR

有意开发可以加我微信：lanbinleo 或者 QQ：271360178

## IShell自带功能
IShell本质上作为一个模块化Shell，装载了一些小工具。

- [X] print - 打印Helloworld
- [X] downlib - 自动下载所需的依赖库
- [X] dellib - 手动删除某个依赖库
- [X] scan - 端口扫描器，使用方法：scan host -st startPort -np endPort
- [ ] stress - 压力测试器
- [ ] demo - 内置98%API，可以作为开发手册使用

**！以上功能正在实现中**

## IShell插件

- [ ] remote - 集成远程控制电脑屏幕功能
- [ ] trojan - 集成生成木马程序、监听木马程序和控制电脑一体的工具
- [ ] airport - 搜索在线的clash节点池（待定）
- [ ] news - 获取今日新闻（有点鸡肋说实话）
- [ ] baidu - 我来帮你百度一下
- [ ] bigbug - 常见漏洞集成库
- [ ] spider - 可视化爬取网站页面（大工程！）

**！以上功能正在策划中**

## IShell亮点

- 模块化编程，更易拓展
- 更加完整的错误系统
- 主代码和模块分开
- 报错易寻找具体位置
......

# 使用方法

1. 下载最新版Release [点我前往Release](https://github.com/lanbinshijie/IceShell/releases)

2. 下载源代码并解压到本地

3. 运行`python main.py`

4. 添加拓展模块

**注意！不推荐直接在CMD里运行，推荐找专业终端体验全部功能（如VSCode的终端）**

运行效果如图所示

![Run Shell](./docs/img/runShell.png)

# 参与开发

您可以联系我的
- 微信：lanbinleo
- QQ：271360178
- 邮箱：[me@lanbin.top](mailto:me@lanbin.top)

或者直接提交issue

## 近期任务

- [X] 一键检测依赖并询问是否安装
- [X] 将模块部分从主程序中剥离出来
- [ ] 重构难看的Logo
- [ ] 完善报错信息
- [ ] 更新更多标准库

## 代码提交标准（给自己看的）
- feat：新功能
- fix：修补bug
- docs：修改文档
- style： 格式化代码结构（不影响代码运行的变动）
- refactor：重构（即不是新增功能，也不是修改bug的代码变动，比如重命名变量
- chore：构建过程或辅助工具的变动（不会影响代码运行）

# 后记

- Logo链接
    1. https://s1.ax1x.com/2023/01/13/pSK4gln.png
    2. https://s1.ax1x.com/2023/01/13/pSK42yq.png
