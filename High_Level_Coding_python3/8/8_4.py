# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/27 17:43'

'''
如何使用线程本地数据
threading.local函数可以创建线程本地数据空间，其下属性对每个线程独立存在
'''

import threading
l=threading.local()
l.x=1   #主线程下的本地数据，其他线程访问不到
def f():
    print(l.x)
f()

# threading.Thread(target=f).start()  #在子线程中访问不到x