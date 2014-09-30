Title: javascript 对象探索之 构造对象、原型对象 和 实例对象
Date: 2014-9-30 13:38  
Category: javascript 
Tags: javascript, 对象
Slug: javascript--object   
Author: dragondjf  
Summary:  


####1.什么是构造对象？
    
        function Point(x, y, z){
        	this.x = x;
        	this.y = y;
        	this.z = z;
        }
这样【`Point`】就是一个构造对象， ``可以实例化``；

**构造对象实际上就是构造函数， 构造函数与普通函数没有本质区别，但是构造函数拥有this关键字，并且只能够使用new运算符来调用函数。**

**从本质上来讲，构造对象就是类；**

构造对象同样拥有属性和方法，他们都是全局变量，只能被构造对象本身调用，无法被实例对象调用。


####2. 什么是实例对象？

        var p1 = new Point(1, 23);
        console.log(p1.constructor == Point) // true

这样【`p1`】就是Point类的实例化对象， `实例化对象不能继续实例化`

实例对象是通过构造函数创建的。

**当使用构造函数创建实例对象之后，每个对象之间都是独立的个体，就不再与构造对象保持关系。**

####3. 什么是原型对象?
拓展原型对象的两种写法：

        var p1 = new Point(1, 23);
        Point.prototype.name = "dsdsds"
        Point.prototype.sum = function(){
        	return this.x + this.y;
        }
或者是   

        Point.prototype.name = "dsdsds"
        Point.prototype.sum = function(){
        	return this.x + this.y;
        }
         var p1 = new Point(1, 23);

这两种写法没有本质区别，拓展原型对象在生成实例前后一样。

**Point.prototype 就是原型对象，javascript中所有函数都有prototype属性，它引用了一个对象，这个对象就是原型对象；**
**原型对象初始化时为空，但是当你在其中定义的任何属性和方法都会被构造函数所创建的实例对象继承。**


`实际上， 原型对象也是构造函数的一个实例对象；与普通的实例对象没有本质区别，只是它比较特殊而已，`
`原型对象的所有属性和方法能够为构造函数的所有实例共享，这就是其他语言的类继承，在javascript中简称【原型继承】`
       
      console.log(p1.constructor == Point) //ture
      console.log(Point.prototype.constructor == Point) //true
说明原型对象与实例对象都是通过同一个构造函数实例化的一个对象

重写原型对象：  

        Point.prototype = {
        	name : "yuanxiangduixiang",
        	sum : function(){
        	return this.x + this.y;
        	}
        }
        
        var p1 = new Point(1, 23);
        
        console.log(Point.prototype.constructor == Point) // false
        console.log(Point.prototype.constructor == Object) // true

这种写法表示重写了Point.prototype原型对象，这样原型对象不再由Point构建，而是由Object构建

下面这种写法是错误的：

        var p1 = new Point(1, 23);
        Point.prototype = {
            	name : "yuanxiangduixiang",
            	sum : function(){
            	return this.x + this.y;
            	}
            }
        console.log(p1.name) //报错
        
####4. 总结
+ **构建对象**  是**构造函数**；
+ **实例对象**  是由构造函数使用**new**关键字构建的实例化对象；
+ **原型对象**  默认也是由构造函数构建的实例化对象，**只是原型对象的所有属性和方法被构造函数的其他实例对象所共享**；   

demo:     


    function Point(x, y, z){
        this.x = x;
        this.y = y;
        this.z = z;
    }
    var p1 = new Point(1, 23);
    console.log(p1.constructor == Point); //true
    console.log(Point.prototype.constructor == Point); //true
    console.log(Point.prototype.isPrototypeOf(p1)); // true
    
