Title: linux 备忘
Date: 2014-11-12 17:30
Category: linux
Tags: linux, mongodb
Slug: linux
Author: dragondjf
Summary: 

####1. mongodb安装及自启动
    下载mongodb
    curl https://fastdl.mongodb.org/linux/mongodb-linux-i686-2.6.5.tgz?_ga=1.127915085.1772090675.1413895499 > mongodb.tgz
    tar xzf mongodb.tgz
    mv mongodb-linux-i686-2.6.5 /use/local/mongodb

    创建数据库文件存放目录和log
    mkdir -p /home/data/mongodb/mongodb_data
    mkdir -p /home/data/mongodb/mongodb_log
    sudo sublime /home/data/mongodb/mongodb_log/work.log

    sublime/gedit /etc/rc.loacl
    在末尾增加命令，这样即可实现开机自启动
    /usr/local/mongodb/bin/mongod -dbpath=/home/data/mongodb/mongodb_data --logpath=/home/data/mongodb/mongodb_log/work.log --logappend --journal


####2. 设置sublime text在终端启动
    sudo ln -s /opt/sublime_text/sublime_text /usr/bin/sublime

在sublime text中安装terminal插件
然后在Settings-Default中设置terminal字段，填写你所使用终端的路径即可

#####3. 为sublime text 创建桌面快捷方式

    sudo sublime /usr/share/applications/sublime.desktop

    [Desktop Entry]
    Version=1.0
    Type=Application
    Name=Sublime Text
    GenericName=Text Editor
    Comment=Sophisticated text editor for code, markup and prose
    Exec=/opt/sublime_text/sublime_text %F
    Terminal=false
    MimeType=text/plain;
    Icon=sublime-text
    Categories=TextEditor;Development;
    StartupNotify=true
    Actions=Window;Document;
    [Desktop Action Window]
    Name=New Window
    Exec=/opt/sublime_text/sublime_text -n
    OnlyShowIn=Unity;
    [Desktop Action Document]
    Name=New File
    Exec=/opt/sublime_text/sublime_text --command new_file
    OnlyShowIn=Unity;

    如果希望里面sublime 替换默认的gedit作为编辑器

    sudo sublime /usr/share/applications/defaults.list
替换文件中所有gedit.desktop为sublime.desktop，这样在打开文本文档的时候,直接双击就可以使用sublime打开。

如果你不愿意所有的文本文件都用它打开，就不要修改关联列表，对相应的文本文件（如cpp, py) 点击右键后选择打开方式，用sublime text打开即可～










