# coding=utf-8
import os
import re
import urllib
from __builtin__ import exit
import webbrowser

def Schedule(a, b, c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per
    
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    local = os.getcwd() + os.sep + 'data' + os.sep + 'photo'
    if not os.path.exists(local) :
        os.makedirs(local)
    for imgurl in imglist:
        print imgurl
        urllib.urlretrieve(imgurl, local + os.sep + '%s.jpg' % x, Schedule)
        x += 1

html = getHtml("http://tieba.baidu.com/p/2460150866")
print getImg(html)

webbrowser.open_new("http://tieba.baidu.com/p/2460150866")
exit(0)
