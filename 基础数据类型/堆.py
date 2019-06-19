import heapq

"""
获取大量元素 topk 大个元素,固定内存
思路：
1、先放入元素前k个建立一个最小堆
2、迭代剩余元素：
    如果当前元素小于堆顶元素，跳过该元素(肯定不是前k大)
    否则替换堆顶元素为当前元素，并重新调整堆
"""

class TopK:
    def __init__(self,iterable,k):
        self.minheap=[]
        self.capacity=k
        self.iterable=iterable
    def push(self,val):
        if len(self.minheap)>=self.capacity:
            min_val=self.minheap[0]
            if val<min_val:
                pass
            else:
                heapq.heapreplace(self.minheap,val)     #将已有的堆根据新值重新生成一个堆
        else:
            heapq.heappush(self.minheap,val)    #前面k个元素直接放入minheap
    def get_topk(self):
        for val in self.iterable:
            self.push(val)
        return self.minheap

import random
l=list(range(1000))
random.shuffle(l)
t=TopK(l,10)
print(t.get_topk())