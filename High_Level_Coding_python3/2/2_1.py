from random import randint

'''
如何在列表，字典，集合中根据条件筛选数据
'''

#传统办法
data=[randint(-10,10) for _ in range(10)]
print(data)
res=[]
for i in data:
    if i>0:
        res.append(i)
print("传统方法:",res)

#列表：filter函数
data2=[randint(-10,10) for i in range(10)]
print(data2)
lf=list(filter(lambda x:x>=0,data2))  #在python3中，filter返回一个生成器对象
print("用filter:",lf)

#列表：列表列表解析
print("列表解析：",[i for i in data2 if i>=0])

#字典列表解析
data3={'student%d' % i:randint(50,100) for i in range(1,21)}
print(data3)
print("字典列表解析",{k:v for k,v in data3.items() if v>=90})
print("用filter:",list(filter(lambda x:x[1]>=90,data3.items())))

#集合列表解析
s=set(data2)
print("集合列表解析",{i for i in s if i%3==0})
