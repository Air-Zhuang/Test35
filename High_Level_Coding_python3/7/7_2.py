'''
创建大量实例节省内存(关闭动态绑定)
'''

'''实例创建的属性都保存在__dict__'''
class Player(object):   #传统，其实例占内存
    def __init__(self,uid,name,status=0,level=1):
        self.uid=uid
        self.name=name
        self.stat=status
        self.level=level

class Player2(object):  #其实例更省内存,但是不能动态添加属性了
    __slots__ = ['uid','name','stat','level']
    def __init__(self,uid,name,status=0,level=1):
        self.uid=uid
        self.name=name
        self.stat=status
        self.level=level
p1=Player('001','Jim')
p2=Player2('001','Jim')
print(set(dir(p1))-set(dir(p2))) #传统比省内存之间多的属性，主要占内存的是__dict__

import tracemalloc      #这个模块是跟踪内存使用情况的
tracemalloc.start()
#start
la=[Player(1,2,3) for _ in range(100000)]
lb=[Player2(1,2,3) for _ in range(100000)]
#end
snapshot=tracemalloc.take_snapshot()
top_stats=snapshot.statistics('lineno')
for stat in top_stats[:10]:
    print(stat)