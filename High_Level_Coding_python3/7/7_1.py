'''
如何派生内置不可变类型并修改其实例化行为
'''

class IntTuple(tuple):  #跟原本的tuple是一样的
    def __init__(self,iterable):
        super(IntTuple,self).__init__(iterable)

'''翻译__new__和__init__'''
list('abc')                 #下面两句等于加起来等于list('abc')

l=list.__new__(list,'abc')
list.__init__(l,'abc')
print(l)

'''使用__new__方法'''
class IntTuple(tuple):
    def __new__(cls, iterable):
        g=(x for x in iterable if isinstance(x,int) and x>0)
        # return super().__new__(cls, g)
        return super(IntTuple,cls).__new__(cls,g)   #两句一样

t=IntTuple([1,-1,'abc',6,['x','y'],3])
print(t)