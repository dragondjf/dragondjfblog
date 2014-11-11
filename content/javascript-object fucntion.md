Title: javascript 对象探索之 基本方法
Date: 2014-9-30 14:38  
Category: javascript 
Tags: javascript, 基本方法
Slug: javascript--object function
Author: dragondjf  
Summary:  


####1. toString()
toString() 方法能够返回一个对象的字符串表示，但是返回的字符串比较灵活，可以是一个具体的值，也可能是一个对象的类型表示。

举个例子：
    由于toString()返回的内容比较简单，可以对其近扩展，让对象实例返回构造函数的源代码：
        
        Object.prototype.toString = function(){
            return this.constructor.toString();
        }
        function Point(x, y, z){
            this.x = x;
            this.y = y;
            this.z = z;
        }
        var p1 = new Point(1, 23, 5);
        console.log(p1.toString()); // 返回函数Point的源码

####2.valueOf()
    Objectd对象的默认valueOf()返回结果与toString()返回结果一样。
    对于String、 Number 、 Boolean对象具有明显原始值时，它们的valueOf()返回适合的原始值。

####3. hasOwnProperty()
对象的属性分为两大类：私有属性 和 继承属性
hasOwnProperty()只能判断指定名称的属性或者对象 是否 为该实例对象的私有属性；无法判断是否为继承属性。
    
        function Point(x, y, z){
            this.x = x;
            this.y = y;
            this.z = z;
        }
        var p1 = new Point(1, 23, 5);
        
        
        Point.prototype.a = 4;
        Point.prototype.b = 5;
        Point.prototype.c = 6;
        
        console.log(p1.hasOwnProperty("x")) // true
        console.log(p1.hasOwnProperty("a")) // false
        console.log(Point.prototype.hasOwnProperty("x")) // false
        console.log(Point.prototype.hasOwnProperty("a")) // true
    
####4.propertyIsEnumerable()
对于javascript对象而言， 我们可以枚举它的属性。但并不是对象的所有属性都可以枚举，只有满足以下两个条件的属性才可以：
+ 1.属性名是由一个字符串参数指定的，即对象的所有私有属性和原型属性。但是javascript又规定，只有对象直接定义的属性才可以枚举，继承属性不可以；即便用for/in循环可以枚举原型属性。
+ 2.属性可以使用for/in循环进行遍历读写。但是javascript核心对象的默认属性一般都是不允许枚举的。

        function Point(x, y, z){
            this.x = x;
            this.y = y;
            this.z = z;
        }
        var p1 = new Point(1, 23, 5);
        
        
        Point.prototype.a = 4;
        Point.prototype.b = 5;
        Point.prototype.c = 6;
        
        console.log(p1.propertyIsEnumerable("x")) // true
        console.log(p1.propertyIsEnumerable("a")) // false
        console.log(Point.prototype.propertyIsEnumerable("x")) // false
        console.log(Point.prototype.propertyIsEnumerable("a")) // true

####5. isPrototypeOf()
可以通过这个方法检测某一个对象是否为另外一个对象的原型对象

    
        function Point(x, y, z){
            this.x = x;
            this.y = y;
            this.z = z;
        }
        var p1 = new Point(1, 23, 5);
        
        
        Point.prototype.a = 4;
        Point.prototype.b = 5;
        Point.prototype.c = 6;
        
        console.log(Point.prototype.isPrototypeOf(p1)) // true

####6. javascript常用面试题
<a href="http://dramin.duapp.com/#masthead">javascript常用面试题</a>
