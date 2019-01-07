# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/24 14:15'

'''
解析简单的xml文档
'''
import os
from xml.etree.ElementTree import parse
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\file\\demo.xml"

f=open(path)
et=parse(f)

root=et.getroot() #得到根

print(root)
print(root.tag) #标签名
print(root.attrib) #属性

print(root.find('country'))  #找到第一个名字是'country'的子元素
print()

for child in root:  #获取子节点,root本身可迭代
    print(child.get('name'))
print()

for i in root.iterfind('country'):  #迭代名字是'country'的子元素
    print(i.get('name'))

for i in root.iter():   #迭代根下的所有，无论在第几层
    i.get('name')
root.iter('rank')

#高级用法
print(root.findall('country/*')) #查找country下的所有
print(root.findall('.//rank'))   #无论在哪一层都能找到
print(root.findall('.//rank/..'))    # .. 找父亲
print(root.findall('country[@name]'))    #当前属性
print(root.findall('country[@name="Singapore"]')) #查找当前属性等于
print(root.findall('country[rank="69"]'))    #子标签属性等于69
print()
print(root.findall('country[1]'))    #通过序号查找
print(root.findall('country[last()-1]'))

