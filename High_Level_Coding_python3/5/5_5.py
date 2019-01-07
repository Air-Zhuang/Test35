# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/23 22:54'

'''
如何访问文件的状态
'''

import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\file\\file.txt"

#第一种方式
s=os.stat(path)
print(s)

import stat
print(stat.S_ISDIR(s.st_mode))    #判断是否为文件夹
print(stat.S_ISREG(s.st_mode))    #判断是否为普通文件

print(s.st_mode & stat.S_IXUSR)   #判断访问权限

print(s.st_atime)    #最后的访问时间
import time
print(time.localtime(s.st_atime))

print(s.st_size)    #文件大小
print()

#简便方式，使用os.path
print(os.path.isdir(path))   #判断是否是文件夹
print(os.path.isfile(path))  #判断是否是普通文件
print(os.path.getatime(path))  #获取最后访问时间
print(os.path.getsize(path))  #获取文件大小