Title:python的插件库
Date: 2014-12-07 21:44
Category: python 
Tags: python, pluginbase 
Slug:  python pluginbase  
Author: dragondjf  
Summary:  

#####1.pluginbase
    pluginbase是Flask的作者**Armin Ronacher**为python写的一个插件库，简单易用

#####2.基本使用方式

Step 1:

Create a “plugin base” object. It defines a pseudo package under which all your plugins will reside. For instance it could be yourapplication.plugins:

    from pluginbase import PluginBase
    plugin_base = PluginBase(package='yourapplication.plugins')
Step 2:

Now that you have a plugin base, you can define a plugin source which is the list of all sources which provide plugins:

    plugin_source = plugin_base.make_plugin_source(
        searchpath=['./path/to/plugins', './path/to/more/plugins'])
Step 3:

To import a plugin all you need to do is to use the regular import system. The only change is that you need to import the plugin source through the with statement:

    with plugin_source:
        from yourapplication.plugins import my_plugin
    my_plugin.do_something_cool()
Alternatively you can also import plugins programmatically instead of using the import statement:

    my_plugin = plugin_source.load_plugin('my_plugin')
详情参见：[http://pluginbase.pocoo.org/](http://pluginbase.pocoo.org/)