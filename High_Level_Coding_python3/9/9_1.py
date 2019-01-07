'''
如何使用函数装饰器
'''

def memo(func):
    cache={}
    def wrap(*args):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]
    return wrap
#[题目1]斐波那契数列
@memo
def fibonacci(n):
    if n<=1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(50))
#[题目2]一共有10个台阶的楼梯，从下面走到上面，一次只能迈1-3个台阶，
#       并且不能后退，走完这个楼梯共有多少种方法
@memo
def climb(n,steps):
    count=0
    if n==0:
        count=1
    elif n>0:
        for step in steps:
            count+=climb(n-step,steps)
    return count
print(climb(10,(1,2,3)))