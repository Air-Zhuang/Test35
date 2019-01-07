from random import randint
from collections import Counter
import os,re

path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''
统计序列中元素的出现频率
'''


#使用dict.fromkeys方式生成dict
data1=[randint(0,20) for i in range(30)]
print("原始list：",data1)
dict1=dict.fromkeys(data1,0)
print("fromkeys:",dict1)
for i in data1:
    dict1[i]+=1
print("要排序的dict",dict1)

#使用列表推导选出数量前三(消耗空间)
print("使用列表推导选出数量前五:",list(sorted([(v,k) for k,v in dict1.items()],reverse=True))[:5])

#使用堆数据结构(省空间)
import heapq
print("使用堆数据结构选出数量前五:",heapq.nlargest(5,[(v,k) for k,v in dict1.items()]))
print("使用堆数据结构选出数量最小的五个:",heapq.nsmallest(5,[(v,k) for k,v in dict1.items()]))
print()


#用collections.Counter选出数量前三(推荐)
print(data1)
dict2=Counter(data1)    #生成一个频度字典

print(dict2)
dict2.update(data1)     #追加
print(dict2)

print("使用collections.Counter选出数量前五:",dict2.most_common(5))

print()

txt=open(path+"\\test\\test.txt").read()
txt2=re.split('\W+',txt)    #使用非字母字符切割文本
print(txt2)
txt3=Counter(txt2)          #生成一个频度字典
print(txt3)
print(txt3.most_common(3))

'''itertools.groupby(it,key=None)'''
'''产出由两个元素组成的元素，形成为(key,group)，
    其中key是分组标准，group是生成器，用于产出分组里的元素'''
import itertools
print('itertools.groupby------------------:')
print(list(itertools.groupby('LLLLAAGG')))
for char,group in itertools.groupby('LLLLAAGG'):
    print(char,'->',len(list(group)))


