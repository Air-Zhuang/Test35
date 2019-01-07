from collections import defaultdict
from random import randint

#旧方法
user_dict={}
users=["bobby1","bobby2","bobby3","bobby1","bobby2","bobby2"]
for user in users:
    if user not in user_dict:
        user_dict[user]=1
    else:
        user_dict[user]+=1
print(user_dict)
print()

'''用法:dict.fromkeys(seq[, value]))，value默认是None 
    说明:创建并返回一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值(默认为None)'''
data1=[randint(0,20) for i in range(30)]
print("原始list：",data1)
dict1=dict.fromkeys(data1,0)
print("fromkeys:",dict1)
for i in data1:
    dict1[i]+=1
print("要排序的dict",dict1)
print()

'''setdefault()'''
'''setdefault为词典设置默认值'''
user_dict={}
users=["bobby1","bobby2","bobby3","bobby1","bobby2","bobby2"]
for user in users:
    user_dict.setdefault(user,0)
    user_dict[user]+=1
print(user_dict)
print()

'''defaultdict'''
'''dict =defaultdict(factory_function)
    这个factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值，比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0'''
default_dict=defaultdict(int)
users=["bobby1","bobby2","bobby3","bobby1","bobby2","bobby2"]
for user in users:
    default_dict[user]+=1
print(default_dict)
print(default_dict["bobby2"])
print(default_dict["air"])
print()

#defaultdict嵌套
def gen_default():
    return {
        "name":"",
        "num":0
    }
default_dict=defaultdict(gen_default)
print(default_dict["group1"])
default_dict["group1"]=1
print(default_dict)
print()