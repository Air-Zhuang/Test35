# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/29 22:00'

'''
读取ini文件
'''

import os
import ConfigParser
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\file\\file.ini"

conf=ConfigParser.ConfigParser()
conf.read(path)
print(conf.get("login_element","username"))

class getini(object):
    def __init__(self,path=None):
        if path==None:
            self.path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\file\\file.ini"
        else:
            self.path=path
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(self.path)
    def getElement(self,head,element):
        return self.conf.get(head,element)

if __name__ == '__main__':
    a=getini()
    print(a.getElement("login_element","密码"))
    print(a.getElement("login_element", "元素").split('>')[0])
    print(a.getElement("login_element", "元素").split('>')[1])