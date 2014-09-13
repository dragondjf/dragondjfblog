Title: PyQt/PySide 国际化实现  
Date: 2014-9-10 16:20  
Category: PyQt/PySide  
Tags: PyQt, PySide, Qt, Python  
Slug: PyQt/PySide   
Author: dragondjf  
Summary:  

###1.概述：
在程序是使用**self.tr**对需要进行翻译的字符串进行修饰,实质上这样做就是标定这些字符串是可以进行国际化操作的.
###2.步骤：
######第一步：
新建**main.pro**工程文件，文件格式如下：

    SOURCES += main.py
    SOURCES += app.py
    SOURCES += db.py
    SOURCES += help.py
    TRANSLATIONS += main.ts
######第二步:
利用pylupdate4(PyQt4)或者pyside-lupdate(PySide)进行翻译文件提取：
>PyQt4  

    pylupdate4 main.pro

>PySide  
    
    pyside-lupdate main.pro

这样会在当前目录生成一个main.ts(main.pro中**TRANSLATIONS**的值)

######第三步:
利用PyQt4或者是PySide安装目录下的linguist.exe打开main.ts，逐项进行翻译

#####第四步:
利用PyQt4或者是PySide安装目录下的lrelease进行翻译
    lrelease main.ts
这样会在当前目录下生成一个main.qm的翻译文件

###第五步：
    
    import sys
    app = QApplication(sys.argv)
    trans = QTranslator()
    trans.load("main.qm")
    app.installTranslator(trans)
    main = CenterWindow()
    main.show()
    sys.exit(app.exec_())

其中的   

    trans = QTranslator()
    trans.load("main.qm")
    app.installTranslator(trans)
就是将main.qm加载到程序当中去，这样即可实现程序国际化

<br>
<br>

PyQt/PySide 资源文件使用
=======================================
###步骤：
第一步： 利用QtDesigner进行资源文件的创建或者是手动创建**main.qrc**：  

        <!DOCTYPE RCC><RCC version="1.0">
        <qresource>
        <file alias="filenew.png">images/filenew.png</file>
        <file alias="fileopen.png">images/fileopen.png</file>
        <file alias="filesave.png">images/filesave.png</file>
        <file alias="filesaveas.png">images/filesaveas.png</file>
        <file alias="fileprint.png">images/fileprint.png</file>
        <file alias="filequit.png">images/filequit.png</file>
        <file alias="editinvert.png">images/editinvert.png</file>
        <file alias="editswap.png">images/editswap.png</file>
        <file alias="editzoom.png">images/editzoom.png</file>
        <file alias="editmirror.png">images/editmirror.png</file>
        <file alias="editunmirror.png">images/editunmirror.png</file>
        <file alias="editmirrorhoriz.png">images/editmirrorhoriz.png</file>
        <file alias="editmirrorvert.png">images/editmirrorvert.png</file>
        <file alias="back.png">images/back.png</file>
        <file alias="home.png">images/home.png</file>
        <file alias="icon.png">images/icon.png</file>
        </qresource>
        <qresource>
        <file>imagechanger.qm</file>
        </qresource>
        <qresource>
        <file alias="editmenu.html">help/editmenu.html</file>
        <file alias="filemenu.html">help/filemenu.html</file>
        <file alias="index.html">help/index.html</file>
        </qresource>
        <qresource lang="fr">
        <file alias="editmenu.html">help/editmenu_fr.html</file>
        <file alias="filemenu.html">help/filemenu_fr.html</file>
        <file alias="index.html">help/index_fr.html</file>
        </qresource>
        </RCC>

生成对应资源文件的xml数据结构。

第二步： 利用pyrcc4(PyQt4)或者是pyside-rcc(PySide)进行编译
        
        pyrcc4 resources.qrc -o qrc_resources.py
或者是  

        pysdie-rcc resources.qrc -o qrc_resources.py
这样即可生成一个**qrc_resources.py**资源文件py库

第三步：在主程序中导入**qrc_resources.py**库即可

        import qrc_resources
        app.setWindowIcon(QIcon(":/icon.png"))
注意： 必须加上**":/"**进行路径限定

利用好资源文件可以方便的对资源文件进行固化和程序发布。