'''
如何判断字符串a是否以字符串b开头或结尾
为文件添加可执行权限
'''

#判断文件以字符串开头或结尾   str.startswith() str.endswith()
l=['e.py','g.sh','d.java','h.c','f.cpp','a.sh','c.h','b.py']
ss='g.sh'
print(ss.endswith(('.sh','.py','.txt')))#必须是字符串或是元组
print([name for name in l if name.endswith(('.sh','.py'))])
print()

import os,stat
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(path)
print("读取某个文件下所有的文件名:",os.listdir(path))
print("读取某个文件的状态:",os.stat(path+'\\test\\4_2.txt'))
print("oct()转换成八进制,权限为666:",oct(os.stat(path+'\\test\\4_2.txt').st_mode))
#修改文件权限
os.chmod(path+'\\test\\4_2.txt',os.stat(path+'\\test\\4_2.txt').st_mode | stat.S_IXUSR) #修改文件权限
print(oct(os.stat(path+'\\test\\4_2.txt').st_mode))
print()






