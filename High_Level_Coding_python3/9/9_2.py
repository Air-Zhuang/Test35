'''
如何为被装饰的函数保存元数据
使用标准库functools中的装饰器wraps装饰内部包裹函数，
可以指定将原函数的某些属性，更新到包裹函数上面
'''

def f(a,b=1,c=[]):
    '''f function'''
    return a*2
def f2():
    a=2
    return lambda k:a**k

print(f.__name__)    #函数名
print(f.__doc__)     #函数注释
print(f.__module__)  #函数所属模块
print(f.__defaults__)#函数默认参数
g=f2()
print(g.__closure__[0].cell_contents)    #闭包

from functools import wraps,update_wrapper

def mydecorator(func):
    @wraps(func)                    #第一种方式,装饰器的方式
    def wrapper(*args,**kwargs):
        '''wrapper function'''
        print('In wrapper')
        return func(*args,**kwargs)
    # update_wrapper(wrapper,func)  #第二种方式
    return wrapper

@mydecorator
def example():
    '''example function'''
    print('In example')

print(example.__name__)
print(example.__doc__)