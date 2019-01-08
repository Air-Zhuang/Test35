import time

def clock(func):
    '''一个简单的装饰器，输出函数的运行时间'''
    def clocked(*args):
        t0=time.perf_counter()
        result=func(*args)
        elapsed=time.perf_counter()-t0
        name=func.__name__
        arg_str=",".join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed,name,arg_str,result))
        return result
    return clocked
@clock
def snooze(seconds):
    time.sleep(seconds)
@clock
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)
print('*' * 40,'Calling snooze(.123)')
snooze(.123)
print('*' * 40, 'Calling factorial(6)')
print('6!=',factorial(6))
print(factorial.__name__) #现在factorial保存的是clocked函数的引用

import functools
def clock2(func):
    '''使用functools.wraps装饰器把相关的属性从func复制到clocked中，
    此外，这个新版还能正确处理关键字'''
    @functools.wraps(func)
    def clocked(*args,**kwargs):
        t0=time.perf_counter()
        result=func(*args,**kwargs)
        elapsed=time.perf_counter()-t0
        name=func.__name__
        arg_list = []
        if args:
            arg_list.append(','.join(repr(arg) for arg in args))
        if kwargs:
            pairs=['%s=%r' % (k,w) for k,w in sorted(kwargs.items())]
            arg_list.append(','.join(pairs))
        arg_str=','.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed,name,arg_str,result))
        return result
    return clocked
@clock2
def snooze(seconds):
    time.sleep(seconds)
@clock2
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)
print('*' * 40,'Calling snooze(.123)')
snooze(.123)
print('*' * 40, 'Calling factorial(6)')
print('6!=',factorial(6))
print(factorial.__name__)   #现在factorial保存的是自己的引用
