#闭包
def set_passline(passline):
    def cmp(val):
        if val>=passline:
            print("pass")
        else:
            print("faild")
    return cmp

f_100=set_passline(60)
f_150=set_passline(90)
f_100(89)
f_150(89)
'''------------------------------------------------------'''
#装饰器,例一
def deco(func):
    def inner():
        print("This is inner")
    return inner
@deco
def target():
    print("This is target")

target()
'''------------------------------------------------------'''

#装饰器,例三
def outside(func):  #这个装饰器用来计算所有入参的和
    def inside(*args):
        print(sum(args))
        return func(*args)
    return inside
@outside
def a(*args):
    print(args)
@outside
def b(*args):
    print(args)
a(1,2,3)
b(4,5,6)
'''------------------------------------------------------'''
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
'''------------------------------------------------------'''
#装饰器,例二
def dec(func):
    def in_dec(*args):
        if len(args)==0:
            return 0
        for val in args:
            if not isinstance(val,int):
                return 0
        return func(*args)
    return in_dec
@dec
def my_sum(*args):
    return sum(args)
@dec
def my_average(*args):
    return sum(args)/len(args)

# my_sum=dec(my_sum)    #省略了这一句
print(my_sum(1,2,3))
print(my_sum(1,2,'3'))
print()
'''------------------------------------------------------'''
