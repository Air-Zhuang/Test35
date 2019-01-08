import operator
from functools import reduce,partial

'''https://blog.csdn.net/felaim/article/details/71082031'''

'''operator.mul'''
def f(n):
    print(reduce(lambda a,b:a*b,range(1,n+1)))  #等同
    print(reduce(operator.mul,range(1,n+1)))
f(4)
print()

triple=partial(operator.mul,3)   #使用partial把一个两参数函数改编成需要单参数的可调用对象
print(triple(7))
print(list(map(triple,range(1,10))))
print()

'''operator.itemgetter'''
l=[
    (1,"d"),(2,"b"),(3,"c"),(4,"a"),
]
print(sorted(l,key=lambda x:x[1]))  #等同
print(sorted(l,key=operator.itemgetter(1)))
print()

'''operator.attrgetter'''
class Student(object):
    def __init__(self,name,grade,age):
        self.name=name
        self.grade=grade
        self.age=age
    def __repr__(self):
        return repr((self.name,self.grade,self.age))
students=[
    Student('jane','B',14),
    Student('john','A',12),
    Student('dave','B',10),
]
print(sorted(students,key=lambda o:o.age))  #等同
print(sorted(students,key=operator.attrgetter('age')))
print()

'''operator.methodcaller'''
'''7_8'''
s='The time has come'
upcase=operator.methodcaller('upper')
print(upcase(s))
hiphenate=operator.methodcaller('replace',' ','-')
print(hiphenate(s))
print()
s='abc123abc456'
s.find('abc',3)
operator.methodcaller('find','abc',3)
print(operator.methodcaller('find','abc',3)(s))
print()

