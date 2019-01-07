# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/24 13:21'

'''
如何读写json数据
'''

'''
语音识别！！！！！！！！！课上有
'''
import os
import json
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\test\\demo.json"


l=[1,2,'abc',{'name':'Bob','age':13}]
ll={'b':None,'a':5,'c':'abc'}

#将一个python对象，转换成json字符串
print(json.dumps(l))
print()
print(json.dumps(ll))
print(json.dumps(ll,separators=[',',':'])) #将json字符串中的空格去掉
print(json.dumps(ll,sort_keys=True)) #排序
print()

#将json，转换成python对象
print(json.loads('[1, 2, "abc", {"age": 13, "name": "Bob"}]'))
print(json.loads('{"a": 5, "c": "abc", "b": null}'))
print()

#将python对象，转换成json字符串,文件
# with open(path,'wb') as f:
#     json.dump(l,f)

#将json，转换成python对象,文件
# with open(path,'rb') as f:
#     print(json.load(f))
