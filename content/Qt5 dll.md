Title: Qt5程序依赖解读  
Date: 2014-11-11 13:56  
Category: Qt  
Tags: Qt5,
Slug: Qt5_dll 
Author: dragondjf  
Summary:

#####一、依赖库一览


######
1.QT模块库

    Qt5Core.dll      #QT核心库
    Qt5Gui.dll       #QT Gui库
    Qt5Widgets.dll   #QT Widgets库，QT 5中GUI程序基本都需要此dll
    还有其他程序用到的Qt5XXX.dll

######
 2.ICU（International Component for Unicode，Unicode工具）依赖库

    icudt49.dll      
    icuin49.dll     
    icuuc49.dll    

######
3.QT插件库,Qt新增，有点坑爹，路径必须正确
根据不同的程序，需要不同的插件库
例如 QT_DIR/plugins/*/*.dll
需要将 platforms/*.dll,accessible/*.dll的文件结构保留
放在你所编译的程序所在目录
    plugins/platforms/qwindows.dll
    plugins/accessible/qtaccessiblewidgets.dll

######
 4.EGL依赖库，为OpenGL,OpenGL es提供接口
    libEGL.dll
    libGLESv2.dll

######
5.mingw依赖库(msvc编译则无需这些库)
    libgcc_s_sjlj-1.dll
    libstdc++-6.dll
    libwinpthread-1.dll

######
 6.VC运行库（mingw编译则无需这些库)

    msvcr110.dll(对应VS2012）
    msvcp110.dll

#####二、文件结构
    --platforms
           --qwindows.dll
           --*.dll
    --accessible
           --qtaccessiblewidgets.dll
           --*.dll
    --(other plugin folder)
           --*.dll
    --yourApp.exe
    --Qt5Core.dll 
    --Qt5Gui.dll      
    --Qt5Widgets.dll 
    --icudt49.dll      
    --icuin49.dll     
    --icuuc49.dll 
    --libEGL.dll
    --libGLESv2.dll
    --libgcc_s_sjlj-1.dll(mingw)
    --libstdc++-6.dll(mingw)
    --libwinpthread-1.dll(mingw)
    --msvcr110.dll(msvc)
    --msvcp110.dll(msvc)

#####三、总结
说实话，QT 5虽然有了ICU，Open GL的支持，还有c++11的支持，但是由于依赖的DLL实在是太多，着实有点不太方便。一个mingw编译的qt gui程序，光是依赖dll就有30-50M的依赖库，确实很不爽啊。不过7z压缩后有10M左右，还可以接受