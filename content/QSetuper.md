Title: QSetuper introduction
Date: 2014-9-28 14:04  
Category: QSetuper 
Tags: Qt, QSetuper
Slug: Qt--QSetuper   
Author: dragondjf  
Summary:  

####1.Introduction
QSetuper is an tool  application like  nsis or inno setup,  but this is an c++ application based in Qt. With this tool, you can make your custom installer by yourself.

####2.Feature

+ custom ppt show
+ custom output directory
+ custom progress bar
+ open application when finished
+ create desktop link
+ ....

####3.Build
It should build under Qt4.8.6 or Qt5.3.0 static release

####4.Screenshot
![6](../static/images/QSetuper.png)

####5 Download
+ `source:` <a href="https://github.com/dragondjf/QSetuper/archive/">https://github.com/dragondjf/QSetuper/archive/master.zip</a>

####6.How
1. move you application to example directory
2. python 7z-rcc.py
3. open QSetup.pro with Qt Creater, **you should work with Qt static release version**, Just do it as you know.
