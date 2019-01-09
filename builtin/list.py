'''
list的+=调用的是__iadd__,__iadd__实际调用的是extend方法,只要extend的是一个可迭代对象就可以
list的+调用的是__add__,假如+两边数据类型不一样则会报错
'''

''' +： __add__'''
a=[1,2]
print(a+[3,4])  # + 两边必须相同数据类型
print()

''' +=： __iadd__ 实际调用了下面的extend方法'''
a=[1,2]
a+=(3,4)        #只要是可迭代对象就可以
print(a)
a+=range(2)     #只要是可迭代对象就可以
print(a)
print()

'''extend'''
a=[1,2]
a.extend((3,4))        #只要是可迭代对象就可以
print(a)
a.extend(range(2))     #只要是可迭代对象就可以
print(a)
print()

'''append (append和extend不一样)'''
a=[1,2]
a.append([3,4])
print(a)

