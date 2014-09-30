Title: javascript 对象定义模式
Date: 2014-9-30 15:38  
Category: javascript 
Tags: javascript, 定义模式
Slug: javascript--object define  
Author: dragondjf  
Summary:  

####1.构造函数原型模式
        
        function Book(title, pages){
            this.title = title;
            this.pages = pages;
        }
        
        Book.prototype.what = function(){
            console.log(this.title + this.pages);
        }
        
        var book1 = new Book("javscript 高级编程", 200);
        var book2 = new Book("Qt 高级编程", 200);
        
        book1.what();
        book2.what();

**这种模式是ECMAScript 定义类的标准模式，使用最为广泛。**

####2. 动态原型模式
        
        
        function Book(title, pages){
            this.title = title;
            this.pages = pages;
            
            if (typeof Book.isLock == "undefined"){
                Book.prototype.what = function(){
                    console.log(this.title + this.pages);
                };
                Book.isLock = true;
            }
        
        }
        
        var book1 = new Book("javscript 高级编程", 200);
        var book2 = new Book("Qt 高级编程", 200);
        
        book1.what();
        book2.what();

**动态原型模式封装性更好，性能上与构造函数原型模式一样**
