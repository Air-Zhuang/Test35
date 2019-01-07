'''
创建大量实例节省内存
'''

'''通过__slots__类属性，能节省大量内存，方法是让解释器在元组中存储实例属性，而不用字典'''
class Player(object):   #传统，占内存
    def __init__(self,uid,name,status=0,level=1):
        self.uid=uid
        self.name=name
        self.stat=status
        self.level=level

class Player2(object):  #省内存
    __slots__ = ('uid','name','stat','level') #book:我喜欢使用元祖，因为这样定义的__slots__中所含的信息不会变化
    def __init__(self,uid,name,status=0,level=1):
        self.uid=uid
        self.name=name
        self.stat=status
        self.level=level
p1=Player('001','Jim')
p2=Player2('001','Jim')
print(set(dir(p1))-set(dir(p2))) #传统比省内存之间多的属性，主要占内存的是__dict__