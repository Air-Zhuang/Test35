'''
如何实现用户的历史记录功能（最多n条）
'''
'''
collections.deque() 用于创建一个长度固定的双端队列
pickle 用于将内容存储到硬盘，即使关闭程序，结果依旧保留
'''
from collections import deque
from random import randint
import pickle
import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# q=list(range(10))
# pickle.dump(q,open(path+"\\file\\2_7.pkl",'wb+'))
# q2 = pickle.load(open(path+"\\2_7.pkl",'rb'))
# print(q2)
# print

N=randint(1,100)
history=deque([],5)

def guess(bb):
    if bb==N:
        print('right!!!')
        return True
    elif bb<N:
        print('too small')
        return False
    elif bb>N:
        print('too big')
        return False

while True:
    a=input("input number or h")
    if a.isdigit():#检测字符串是否只由数字组成
        b=int(a)
        history.append(b)
        pickle.dump(history,open(path+"\\2_7.pkl",'wb+'))   #pickle模块需要用2进制'wb'写入
        if guess(b):
            break
    elif a=='h':
        # print(list(history)
        print(pickle.load(open(path+"\\2_7.pkl",'rb')))