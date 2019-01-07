'''
如何将多个小字符串拼接成一个大字符串
'''

pl=["<0112>","<32>","<1024x768>","<60>","<1>","<100.0>","<500.0>"]

#使用字符串的 +  缺点：开销巨大
s=''
for i in pl:
    s+=i
print(s)
print()

#使用reduce方法
from functools import reduce
from operator import add
print(reduce(str.__add__,pl))
print(reduce(lambda a,b:a+b,pl))
print(reduce(add,pl))
print()

#使用str.join()方法
print(''.join(pl))
print()

l=['abc',123,45,'xyz']
print(''.join([str(i) for i in l]))
print()
print(''.join(str(i) for i in l))    #这里使用生成器表达式，可以不加[]，更省资源

