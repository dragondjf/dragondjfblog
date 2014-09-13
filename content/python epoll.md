Title:python epoll 解读
Date: 2014-9-13 20:27
Category: python 
Tags: python, epoll 
Slug:  python epoll  
Author: dragondjf  
Summary:  

######1. 水平触发
    只要某个socket处于readable/writable状态，无论什么时候进行epoll_wait都会返回该socket；
        对于non-blocking的socket，正确的读写操作为:
        读：忽略掉errno = EAGAIN的错误，下次继续读
        写：忽略掉errno = EAGAIN的错误，下次继续写
######2. 边缘触发
    只有某个socket从unreadable变为readable或从unwritable变为writable时，epoll_wait才会返回该socket；
        所以，在epoll的ET模式下，正确的读写方式为:
        读：只要可读，就一直读，直到返回0，或者 errno = EAGAIN
        写:只要可写，就一直写，直到数据发送完，或者 errno = EAGAIN

详情参见：http://fatezero.org/archives/