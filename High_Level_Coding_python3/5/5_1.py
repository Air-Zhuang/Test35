'''
如何读取文本文件
'''

import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#python3  写入读取
ff=open(path+"\\5_1.txt",'w',encoding='utf8')
ff.write('你好python3')
ff.close()
ff=open(path+"\\5_1.txt",'r',encoding='utf8')
ss=ff.read()
print(ss)

#python2  写入读取
# f=open(path+"\\file\\5_1.txt",'w')
# s=u'你好python2'
# f.write(s.encode('utf8'))
# f.close()
# f=open(path+"\\file\\5_1.txt",'r')
# t=f.read()
# print(t.decode('utf8'))
# f.close()

# a=u'你好'
# a1=a.encode('utf8')
# print(a.encode('gbk'))
# print(a1.decode('utf8'))
# print()

