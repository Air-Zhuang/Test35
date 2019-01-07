'''
反向迭代
'''

#普通方法
l=[1,2,3,4,5]
print(l[::-1]) #占内存
l.reverse() #改变原来顺序
# reversed():生成一个反向迭代器，与iter()相反
ll=[11,22,33,44,55]
for i in reversed(ll):
    print(i)
print()

class FloatRange(object):
    def __init__(self,start,end,step):
        self.start=start
        self.end=end
        self.step=step
    def __iter__(self):
        s=self.start
        while s<=self.end:
            yield s
            s+=self.step
    def __reversed__(self):
        s=self.end
        while s>=self.start:
            yield s
            s-=self.step

# for i in iter(FloatRange(1, 5, 0.5)):
for i in FloatRange(1,5,0.5):
    print(i)
print()
for j in reversed(FloatRange(1,5,0.5)):
    print(j)