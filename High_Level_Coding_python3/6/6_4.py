# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/24 15:08'

def pretty(e,level=0):      #xml写入格式美化器
    if len(e)>0:
        e.text='\n'+'\t'*(level+1)
        for child in e:
            pretty(child,level+1)
        child.tail=child.tail[:-1]
    e.tail='\n'+'\t'*level

'''
构建xml文档
'''

from xml.etree.ElementTree import Element,ElementTree
from xml.etree.ElementTree import tostring
import csv
import os
pathcsv=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\file\\stock.csv"
pathxml=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\file\\stock.xml"

#构建xml元素
e=Element('Data')   #创建
e.set('name','abc') #创建属性
print(tostring(e))   #查看xml格式
e.text='123'        #属性赋值
print(tostring(e))

e2=Element('Row')
e3=Element('Open')
e3.text='8.80'
e2.append(e3)       #添加子节点
print(tostring(e2))
e.text=None
e.append(e2)
print()
print(tostring(e))

#创建ElementTree，写入文件
# et=ElementTree(e)
# et.write(pathxml)

#将stock.csv以xml格式写入到stock.xml中
def csvToXml(cpath):
    with open(cpath,'rb') as f:
        reader=csv.reader(f)
        header=reader.next()

        root=Element('Data')
        for row in reader:
            erow=Element('Row')
            root.append(erow)
            for tag,num in zip(header,row):
                e=Element(tag)
                e.text=num
                erow.append(e)
    pretty(root)
    return ElementTree(root)
et=csvToXml(pathcsv)
et.write(pathxml)

