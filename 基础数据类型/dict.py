from _collections_abc import __all__    #源码查看字典类型协议
from collections.abc import MutableMapping

'''
dict的key必须是可哈希的,dict的内存花销大
(我们自定义的对象或者python内部的对象都是用dict包装的)
dict性能非常高,set和dict在查找元素时的时间复杂度都为1

dict原理：dict的key必须是可哈希的，通过对一个key的哈希计算得到value存储的位置。
    如果哈希计算的位置已经存在数据，会重新哈希计算出一个新的位置。
    dict一开始会申请一块内存空间，当剩余空间小于一个值时(一般为三分之一),
    dict会重新申请一块新的内存空间来减少新的哈希计算可能带来的存储位置冲突几率。
'''

'''dict属于mapping类型'''
a={}
print(isinstance(a,MutableMapping))


'''fromkeys()    iterable-->dict'''
data1=range(20)
dict1=dict.fromkeys(data1,{"data":0})
print(dict1)
print()


'''setdefault()  dict-->dict'''
user_dict={}
users=["bobby1","bobby2","bobby3","bobby1","bobby2","bobby2"]
for i in users:
    user_dict.setdefault(i,0)
    user_dict[i]+=1
print(user_dict)
print()

'''
pop()
删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
popitem()
随机返回并删除字典中的一对键和值(一般删除末尾对)。
'''