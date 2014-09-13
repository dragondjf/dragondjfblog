Title:c++之private、protect、public Inheritance（继承）
Date: 2014-9-13 19:56  
Category: c++  
Tags: c++  
Slug: Inheritance（继承）   
Author: dragondjf  
Summary:  

 + Protected and public members(data and function) of a base class are accessible from a derived class(for all three: public, protected and private inheritance). 

>无论哪种继承，子类内部均可访问protect 和 public成员

 + Objects of derived class with private and protected inheritance cannot access any data member of a base class.

>protect、private继承类的实例对象无法访问基类的任何数据

 + Objects of derived class with public inheritance can access only public member of a base class.
 
>public继承类的实例对象自能访问基类的public数据

![Alt text](../static/c++/inheritance.png)



详情参见http://www.programiz.com/cpp-programming/public-protected-private-inheritance