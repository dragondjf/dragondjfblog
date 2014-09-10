Title: tornado 之 ioloop模块解读
Date: 2014-8-31 16:20
Category: Python
Tags: tornado, python, web
Slug: ioloop
Author: dragondjf
Summary: tornado 之 ioloop模块解读

####1.ioloop是什么？
    
>**ioloop**是tornado事件驱动机制的核心模块，在linux下使用高效的**epoll**异步I/O模型, 在FreeBSD（mac）下使用高效的**kqueue**，在windows使用普通的**select**模型，正是基于epoll/kqueue/select, tornado在网络异步编程上表现优秀,下面就是对ioloop的个人理解。

####2.ioloop中使用的模块依赖一览表
+ **标准库：**

| 模块      |     作用 |   备注   |
| :-------- | --------:| :------: |
| [errno](https://docs.python.org/2/library/errno.html)    |   standard errno system symbols |  标准的系统错误符号库  |
| [functools](https://docs.python.org/2/library/functools.html)|  Higher-order functions and operations on callable objects|操作改变可调用的对象|
| [heapq](https://docs.python.org/2/library/heapq.html)| 最小堆算法| 有序列表从小到大|
|[itertools](https://docs.python.org/2/library/itertools.html)| Functions creating iterators for efficient looping| 生产迭代器的高效循环库|
|[select](https://docs.python.org/2/library/select.html)|异步I/O模型|提供异步机制的系统调用封装|
|[threading](https://docs.python.org/2/library/threading.html)| 高级接口的线程模块| 用于获取线程的基本信息
|[signal]()| Set handlers for asynchronous events|  为异步事件提供handlers |




+ **内部模块：**

| 模块      |     作用 |   备注   |
| :-------- | --------:| :------: |
|concurrent| |**Utilities** for working with threads and ``Futures``|
|stack_context|上下文库|**StackContext** allows applications to maintain threadlocal-like state that follows execution as it moves to other execution contexts|
|util|工具库，提供常用的工具函数|||


#####3 事件支持
**tornado.ioloop.IOLoop**同时提供了4种响应事件:

| 事件      |     描述 |
| :-------- | --------:|
|tornado.ioloop.IOLoop.NONE     |无事件
|tornado.ioloop.IOLoop.READ     |读事件
|tornado.ioloop.IOLoop.WRITE    |写事件
|tornado.ioloop.IOLoop.ERROR    |发生错误的事件

####4. 异步事件编程机制：

**tornado.ioloop.IOLoop** 提供了三个接口可以用于异步事件编程:

+ **add_handler**

        def add_handler(self, fd, handler, events):
            self._handlers[fd] = stack_context.wrap(handler)
            self._impl.register(fd, events | self.ERROR)
>add_handler用于添加socket到主循环中, 接受三个参数: fd 是socket的文件描述符 handler 是处理此socket的 callback函数 * events 是此socket注册的事件

+ **update_handler**

        def update_handler(self, fd, events):
            self._impl.modify(fd, events | self.ERROR)
>update_handler用于更新住循环中已存在的socket响应事件, 接受两个参数: fd 是socket对应的文件描述符 events 是注册的新事件

+ **remove_handler**
        
        def remove_handler(self, fd):
            self._handlers.pop(fd, None)
            self._events.pop(fd, None)
            try:
                self._impl.unregister(fd)
            except Exception:
                gen_log.debug("Error deleting fd from IOLoop", exc_info=True)
>remove_handler用于移除主循环中已存在的socket



####5.Demo echo server

根据上面的接口和事件我们就可以写出一个简单的 echo server

    #!/usr/bin/env python
    # -*- coding:utf-8 -*-
    #
    #   Author  :   cold
    #   E-mail  :   wh_linux@126.com
    #   Date    :   13/04/15 15:08:51
    #   Desc    :   Tornado Echo Server
    #   HOME    :   http://www.linuxzen.com
    #
    import Queue
    import socket
    
    from functools import partial
    
    from tornado.ioloop import IOLoop
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(0)              # 将socket设置为非阻塞
    
    server_address = ("localhost", 10000)
    
    sock.bind(server_address)
    sock.listen(5)
    
    fd_map = {}              # 文件描述符到socket的映射
    message_queue_map = {}   # socket到消息队列的映射
    
    fd = sock.fileno()
    fd_map[fd] = sock
    
    ioloop = IOLoop.instance()
    
    def handle_client(cli_addr, fd, event):
        s = fd_map[fd]
        if event & IOLoop.READ:
            data = s.recv(1024)
            if data:
                print "     received '%s' from %s" % (data, cli_addr)
                # 接收到消息更改事件为写, 用于发送数据到对端
                ioloop.update_handler(fd, IOLoop.WRITE)
                message_queue_map[s].put(data)
            else:
                print "     closing %s" % cli_addr
                ioloop.remove_handler(fd)
                s.close()
                del message_queue_map[s]
    
        if event & IOLoop.WRITE:
            try:
                next_msg = message_queue_map[s].get_nowait()
            except Queue.Empty:
                print "%s queue empty" % cli_addr
                ioloop.update_handler(fd, IOLoop.READ)
            else:
                print 'sending "%s" to %s' % (next_msg, cli_addr)
                s.send(next_msg)
    
        if event & IOLoop.ERROR:
            print " exception on %s" % cli_addr
            ioloop.remove_handler(fd)
            s.close()
            del message_queue_map[s]
    
    
    def handle_server(fd, event):
        s = fd_map[fd]
        if event & IOLoop.READ:
            conn, cli_addr = s.accept()
            print "     connection %s" % cli_addr[0]
            conn.setblocking(0)
            conn_fd = conn.fileno()
            fd_map[conn_fd] = conn
            handle = partial(handle_client, cli_addr[0])   # 将cli_addr作为第一个参数
            # 将连接和handle注册为读事件加入到 tornado ioloop
            ioloop.add_handler(conn_fd, handle, IOLoop.READ)
            message_queue_map[conn] = Queue.Queue()   # 创建对应的消息队列
    
    
    ioloop.add_handler(fd, handle_server, IOLoop.READ)
    
    ioloop.start()
上面代码就建立了一个非阻塞的高效的异步的echo server


