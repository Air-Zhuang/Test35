'''
如何处理二进制文件
'''

import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import struct,array
# print(struct.unpack('h','\x01\x02'))

f=open(path+"\\file\\music.wav",'rb')   #rb需要以二进制方式打开
info=f.read(44)
print(info)

# f.seek(0,2) #将指针移动到队尾，用tell查看当前指针位置，从而得知文件大小
# size=f.tell()
# print(size)
#
# n=(size-44)/2
# buf=array.array('h',(0 for i in range(n)))
#
# f.seek(44)
# f.readinto(buf)
#
# for i in range(n): #将音量缩小
#     buf[i]/=8
#
# f2=open(path+"\\file\\music2.wav",'wb')
# f2.write(info)
# buf.tofile(f2)
# f2.close()



