# Session

## 总结

session主要负责的功能是：

- 记录服务端运行着的攻击实例
- 为一个具有团队协作能力提供实例的协作
- 维持会话存活，管理心跳包

## cs

### 数据结构

两类：

- 标识session本身的特征：内部/外部、pid、最近连接时间、对应的客户端号、
- 与session处理的任务相关：对应监听器名称、启动的子进程

对所有的session，采用哈希表进行管理

cs的攻击中心在于客户端攻击而非漏洞攻击，因此其session更多的用于维持客户端攻击时产生的各种beacon。

### 方法

#### 创建

传入client对象，以及multipleselect参数(?)

#### 查

查session内的标识、通过ui库中的atable来获取gui的勾选

#### 删

获取数据后调用**unsubOnClose**，unsub清除窗口后将增加var2监听器(?)

### 调用关系

cs的session本身提供的功能不多，大部分功能都被封装在beacon或者attackclient里，和攻击具体相关的数据也都由它们负责。session在cs里更多承担的是一个记录的功能。

## msf

调用exp打进去以后，msf立刻创建一个session，用户可见的数据结构包括：

- id号
- session别名
- 会话类型，记录了会话两端的架构
- 目标信息，包括目录和ip
- 连接详情，源端和目的端的ip地址以及端口号



### 源码分析

#### lib/msf/core/session/interactive

定义了基本的与session的交互的模型

- 初始化、获取或返回(local_info/peer_info/comm_info)
- 运行命令
- 删除(关闭remote流)

#### lib/msf/core/sesson/provder

- single_command_shell和single_command_executiion 这俩应该是最简单的
  - 

#### lib/msf/base/sessions/mettle_config.rb

小型攻击载荷

#### lib/msf/base/sessions/meterpreter_options.rb



# proxy



## golang部分

可以参考这个代码

- [实战：150行Go实现高性能socks5代理 - SegmentFault 思否](https://segmentfault.com/a/1190000038247560)

- [Minimal socks5 proxy implementation in Golang (github.com)](https://gist.github.com/felix021/7f9d05fa1fd9f8f62cbce9edbdb19253)

## 编译部分



## todo

预想的工作流程是：

1. 通过参数的方式指明回连的攻击机ip和端口、受害者的ip和端口、肉鸡的操作系统
2. 修改go源码，上述参数写死并(混淆)编译出代理程序
3. 通过已有shell传代理程序
4. 验证生效，然后由攻击机发心跳包保活

其中第1、2步可以写个脚本完成，第3步可以集成到msf里当一个meterpreter，第4步可能由msf的session完成？
