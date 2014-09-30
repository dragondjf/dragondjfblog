# -*- coding: utf-8 -*-
import os
from pyquery import PyQuery as pq


js = '''
var liElements = $("li.nav-header")
var category = $($("li.nav-header")[liElements.length - 3])
if (category.html().trim() == "Categories"){
    var startPos = location.pathname.search("category");
    var categoryID = location.pathname.slice(startPos)
    console.log(categoryID);
    var children = category.parent().children();
    for (var i=0 ,length=children.length; i < length; i++ ){
        var lihtml = children[i].innerHTML;
        console.log(lihtml.search(categoryID))
        if(lihtml.search(categoryID) > 0){
            var obj = $(children[i]).children()[0];
            obj.innerText = obj.innerText + "("+ $(".article").length.toString() + ")";
        }
    }
}
'''

def getfiles(path):
    '''
        获取指定path下的所有文件列表
    '''
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.sep.join([dirpath, filename]))
    return files

def addCountToCategory(filename):
    '''
        将相应的content写入filename中去
    '''
    fd = open(filename, "wr")
    fd.write(content)
    fd.close()


files = getfiles(os.sep.join([os.getcwd(), 'output', 'category']))

addCountToCategory(0)
