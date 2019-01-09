from random import randint

def randGen(aList):
    while len(aList)>0:
        yield aList.pop(randint(0,len(aList))-1)

for i in randGen([1,2,3,4,5]):
    print(i)

print()
'''--------------------------'''
def gen_123():      #一个生成器函数
    yield 1
    yield 2
    yield 3
print(gen_123)
print(gen_123())
for i in gen_123():
    print(i)
g=gen_123()
print(next(g))
print(next(g))
print(next(g))
print()
'''------------best iter--------------'''
class M(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "%d,%d" % (self.a,self.b)
    __repr__=__str__
    def __iter__(self):
        for i in (self.a,self.b):
            yield i
m=M(1,2)
for i in m:
    print(i)
