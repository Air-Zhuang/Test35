"""
使用OrderedDict实现LRUCache
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self,capacity=128):
        self.od=OrderedDict()
        self.capacity=capacity

    def get(self,key):  #每次访问更新最新使用的key
        if key in self.od:
            val=self.od[key]
            self.od.move_to_end(key)
            return val
        else:
            return -1

    def put(self,key,value): #更新k/v
        if key in self.od:
            del self.od[key]
            self.od[key]=value #更新key到表尾
        else:   #insert
            self.od[key]=value
            #判断当前容量是否已经满了
            if len(self.od)>self.capacity:
                self.od.popitem(last=False) #删除头

l=LRUCache()
l.put("a",1)
l.put("b",2)
l.put("c",3)
l.put("d",4)
print(l.od)
l.put("b",5)
print(l.od)
print(l.get("c"))
print(l.od)