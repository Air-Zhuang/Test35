'''
如何去掉字符串中不需要的字符
'''

import re

#使用str.strip()
s1='   abc   123   '
s2='+-*abc*-+'
print(s1.strip())
print(s1.rstrip())
print(s2.strip('+-*'))
print()

#切片加拼接
s3='abc:123'
print(s3[:3]+s3[4:])
print()

#使用str.replace()(只能替换一个) re.sub()
print(s1.replace(" ",""))
s4='\tabc\t123\txyz\ropq\r'
print(re.sub('[\t\r]','',s4))
print(re.sub('\s+','',s4))      #\s所有空白符号
print()

#使用str.translate()
s5='abc564654xyz'
d={}
print(s5.translate({ord('a'):'x',ord('b'):'y',ord('c'):'z',ord('x'):'a',ord('y'):'b',ord('z'):'c'}))
print(s5.translate({ord('a'):None,ord('b'):None,ord('c'):None,ord('x'):None,ord('y'):None,ord('z'):None}))
print(s5.translate(s5.maketrans('abcxyz','xyzabc')))
print(s5.translate({ord(i):None for i in 'abcxyz'}))
print(s5.translate(d.fromkeys([ord(i) for i in 'abcxyz'])))     #使用fromkeys
print()













