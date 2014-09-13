Title: Qt--QThread之可重入和线程安全(Reentrancy and Thread-Safety) 
Date: 2014-9-13 20:53  
Category: Qt  
Tags: Qt, QThread
Slug: Qt--QThread   
Author: dragondjf  
Summary:  

1.概述
    Reentrancy（可重入） and Thread-Safety（线程安全）这两个术语用于标识类和方法在多线程程序中如何使用。
    
+ A thread-safe function can be called simultaneously from multiple threads, even when the invocations use shared data, because all references to the shared data are serialized.
    ``一个线程安全的方法可以被多个线程同时调用，甚至每次调用都使用了共享数据因为所有对共享数据的引用是序列化（时间轴）``。
+ A reentrant function can also be called simultaneously from multiple threads, but only if each invocation uses its own data.
    ``一个可重入的方法也可以被多个线程同时调用，但是每次调用使用的都是自己内部数据，互不干扰。``
    
    ``故，一个线程安全的方法总是可重入的，一个可重入的方法并不一定线程安全。``
+ By extension, a class is said to be reentrant if its member functions can be called safely from multiple threads, as long as each thread uses a different instance of the class. The class is thread-safe if its member functions can be called safely from multiple threads, even if all the threads use the same instance of the class.

    ``推而广之:``
    ``如果它的成员函数可以安全地从多个线程调用，只要每个线程使用的类的不同实例， 这个类被认为是可重入的;``
    ``如果它的成员函数可以安全地从多个线程调用，即使所有线程使用的类的同一个实例，这个类被认为是线程安全的.``

详情参见<a href="http://qt-project.org/doc/qt-5/threads-reentrancy.html">http://qt-project.org/doc/qt-5/threads-reentrancy.html</a>