'''
用__next__和yield和__getitem__三种方式表示斐波那契
'''
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1#初始化两个计数器a,b
    def __iter__(self):
        return self#实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b#计算下一个值
        if self.a>100000:#退出循环的条件
            raise StopIteration()
        return self.a#返回下一个值
for i in Fib():
    print(i,end=" ")
print()

class Fib2(object):
    def __init__(self,end):
        self.a, self.b = 0, 1
        self.end=end
    def __iter__(self):
        for i in range(self.end):
            self.a, self.b = self.b, self.a + self.b
            yield self.a
for i in Fib2(30):
    print(i,end=" ")
print()

class Fib3(object):
    def __getitem__(self, item):
        a,b=1,1
        for i in range(item):
            a,b=b,a+b
        return a
f=Fib3()
for i in range(30):
    print(f[i],end=" ")