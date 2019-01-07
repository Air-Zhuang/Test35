from random import randint

'''
如何根据字典中值的大小，对字典中的项排序
'''
#将字典转换成元组列表
dict1={i:randint(0,100) for i in 'abcdef'}
print("原字典：",dict1)

print("按照姓名排序:",{i:dict1[i] for i in sorted(dict1)})

dict3=sorted([(v,k) for k,v in dict1.items()])
print("列表解析的形式生成元组列表：",dict3)
dict2=sorted(zip(dict1.values(),dict1.keys()))
print("zip的形式生成元组列表：",dict2)
print()

#使用sorted的key属性
from operator import itemgetter
print(sorted(dict1.items(),key=lambda x:x[1]))
print(sorted(dict1.items(),key=itemgetter(1)))  #itemgetter(1)=lambda x:x[1]
print()

#使用enumerate更新原字典
dict4=list(zip(dict1.values(),dict1.keys()))
print(dict4)
dict5={k:(i,v) for i,(k,v) in enumerate(dict4,1)}
print(dict5)