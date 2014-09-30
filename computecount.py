# -*- coding: utf-8 -*-
import os


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
    fd = open(filename, "r")
    content = fd.read()
    startPos = '''<div class="well" style="padding: 8px 0; background-color: #FBFBFB;">
            <ul class="nav nav-list">
                <li class="nav-header"> 
                Categories
                </li>'''
    endPos = ''' <div class="well" style="padding: 8px 0; background-color: #FBFBFB;">
            <ul class="nav nav-list">
                <li class="nav-header"> 
                Links
                </li>'''
    
    start =  content.find(startPos)
    end =  content.find(endPos)
    categoryContent = content[start:end]

    newContent = ''
    counts = getArticleCounts()

    lcontents = categoryContent.split("</a></li>")
    for index, i in enumerate(counts):
        newContent += lcontents[index] + "(" + str(i) + ")" + "</a></li>"
    newContent = content[0:start] + newContent + '''</ul>
            </div>''' + content[end:]
    fd.close()
    fd = open(filename, "w")
    fd.write(newContent)
    fd.close()


def getArticleCounts():
    counts = []
    categoryfiles = getfiles(os.sep.join([os.getcwd(), 'output', 'category']))
    for filename in categoryfiles:
        fd = open(filename, "r")
        content = fd.read()
        counts.append(content.count("<div class='article'>"))
        fd.close()
    return counts


files = getfiles(os.sep.join([os.getcwd(), 'output']))

htmlfiles = [f for f in files if f.endswith(".html")]

for filename in htmlfiles:
    addCountToCategory(filename)
