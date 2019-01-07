# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/23 23:18'

'''
如何使用临时文件(临时文件不用命名，且关闭后会被自动删除)
'''

from tempfile import TemporaryFile,NamedTemporaryFile

f=TemporaryFile()   #系统路径是找不到的,关闭之后会被自动删除
f.write('abcdef'*10)
f.seek(0)
print(f.read(100))

nf=NamedTemporaryFile() #可以用 .name 找到文件临时文件路径,但是关闭之后也会被自动删除,除非 NamedTemporaryFile(delete=False)
print(nf.name)